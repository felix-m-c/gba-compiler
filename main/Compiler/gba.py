from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, Token
from abstractTree import *
from transformAST import getTempName
from dataclasses import dataclass
from optimize import optimizeAsm

DEBUG = False

"""
add SP, -1      # platz machen
ld a, 10        # wert in a laden
ld HL, SP+0     # neuen stack pointer nach HL laden
ld (HL), a      # a nach (HL) auf dem stack speichern

außerdem: symbol table nachschlagen
"""


REGISTER_ORDER = ['a', 'c', 'b', 'e', 'd']
REGISTER_16_ORDER = ['hl', 'de', 'bc']
REGISTERS = ['a', 'c', 'b', 'e', 'd', 'hl', 'de', 'bc']

class GlobalManager():
    def __init__(self):
        self.globalVars:dict[str,IDENT] = {} #name:var
        self.arrays:list[Bytearray] = []
    
    def add(self, newVar:IDENT):
        if newVar.name in self.globalVars.keys():
            oldSize = self.globalVars[name].size
            if newVar.size != oldSize:
                raise RuntimeError(f"global var {newVar.name} was already defined with size {oldSize}, not {newVar.size}")
        else:
            self.globalVars[newVar.name] = newVar
    
    def addArray(self, byteArray:Bytearray):
        assert isinstance(byteArray, Bytearray)
        if byteArray.name in [x.name for x in self.arrays]:
            raise RuntimeError(f"global array with name '{byteArray.name}' already exists")
        self.arrays.append(byteArray)

    def exists(self, var:IDENT):
        if var.name in self.globalVars.keys():
            return True
        if var.name in [x.name.name for x in self.arrays]:
            return True
        return False

    def buildAsm(self):
        return ["TODO: build start section"]

class ContextManager():
    def __init__(self, name:str, globalManager:GlobalManager, parentContext=None, isFunctionContext=False):
        if DEBUG: print(f"creating new context: '{name}'")
        self.name = name
        self.vars:list[IDENT] = [IDENT("StackPointer", 2)]
        self.globalManager = globalManager
        self.parent = parentContext
        self.isFunctionContext = isFunctionContext

    def getVarOffset(self, newVar:IDENT):
        offset = 0
        if DEBUG: print(f" > looking in stack for var '{newVar.name}'@'{self.name}', parent:{self.parent}")
        for v in reversed(self.vars):
            if newVar.name == v.name:
                if DEBUG: print("found var")
                # var exists on stack -> calculate pos
                if v.size!=newVar.size: raise RuntimeError(f"var {v.name} was already defined with size {v.size}, not {newVar.size}")
                return offset
            offset += v.size
        # var does not exist on own stack -> check parents
        if self.parent is None:
            # no parents :(
            if DEBUG: print("  > couldn't find var")
            return -1
        else:
            return self.getTotalSize()+self.parent.getVarOffset(newVar)-2 #ignore own return pointer (i think?, this is bad lol) 
    
    def addVar(self, newVar:IDENT):
        for v in self.vars:
            if newVar.name == v.name:
                # var already exists on stack
                raise RuntimeError(f"var {v.name} was already defined with size {v.size}, not {newVar.size}")
        if DEBUG: print(f"   > adding var {newVar.name} to stack")
        self.vars.append(newVar)
    
    def createChild(self, nameExtension:str, isFunctionContext=False):
        return ContextManager(f"{self.name}_{nameExtension}", self.globalManager, parentContext=self, isFunctionContext=isFunctionContext)

    def getTotalSize(self):
        #print (f"size: {sum([v.size for v in self.vars])}")
        return sum([v.size for v in self.vars])

    def removeFunctionFromStack(self)->list:
        """
        similar to removeFromStack, but looks for a functionContext in its parents
        """
        # find closest parent that is a function context
        ctx = self
        totalSize = 0
        depth = 1
        while not ctx is None:
            totalSize += ctx.getTotalSize()
            if ctx.isFunctionContext: break
            ctx = ctx.parent
            depth += 1
            if ctx is None:
                raise RuntimeError(f"tried to return from outside of a function")
        asm = []
        asm.append([f";; remove function ctx {ctx.name}"])
        asm.append(["add", "SP", f"{totalSize-(2*depth)}"]) #-2 because we don't want to delete the return address
        if DEBUG: print(f"removing function stack: {ctx.name}")
        return asm

    def removeFromStack(self)->list:
        asm = []
        asm.append([f";; remove ctx {self.name}"])
        asm.append(["add", "SP", f"{self.getTotalSize()-2}"]) #-2 because we don't want to delete the return address
        if DEBUG: print(f"removing stack: {self}")
        return asm

    def __repr__(self):
        ret = []
        for v in reversed(self.vars):
            ret.extend([f"{v.name}"]*v.size)
        return f"{self.name}[\n  {'\n  '.join(ret)}\n]"

def globalPrinter(globalManager:GlobalManager):
    preRam = [
        ";;globals\n",
        ".ramsection \"Definitions\" slot 1"
    ]
    preArrays = [
        ";;arrays\n",
        ".section \"arrays\""
    ]
    post = [
        ".ends"
    ]
    out = []
    indent = 1
    for v in globalManager.globalVars:
        out.append(f"{'  '*indent}{v} db ; uint8 {v};")
    
    arrays = []
    for a in globalManager.arrays:
        arrays.append(f"{a.name.name}:")
        for el in a.byteList:
            val = "%"+"{0:b}".format(el.value).zfill(8)
            arrays.append(f"{'  '*indent}.db {val}")
    full = preRam+out+post+preArrays+arrays+post
    return "\n".join(full)

def functionsPrinter(globalManager:GlobalManager, functions:list[FunctionDecl]):
    text = ";;functions\n"
    while(len(functions) > 0):
        if DEBUG: print(f"building functions: {len(functions)} left")
        f = functions.pop()
        ctx = ContextManager(name=f"{f.name}", globalManager=globalManager, isFunctionContext=True)
        name = f"{f.name}"
        if DEBUG: print(f"creating function: {f.name}({f.params})")
        # save params from registers onto stack
        asm = []
        asm.append([f";; function {f.name}({f.params})"])
        asm.append([f".section \"{name}\""])
        asm.append([f"{name}:"])
        for i in range(len(f.params)-1, -1, -1): #do backwards to set register a last
            p = f.params[i]
            r = REGISTER_ORDER[i]
            asm.extend(saveRegtoVar(p, ctx, r))
        # create block
        blockAsm, newFuncs = buildBlock(f.block, startContext=ctx, name="main")
        asm.extend(blockAsm)
        if DEBUG: print(f"building functions: found {len(newFuncs)} new Functions")
        functions.extend(newFuncs)

        # remove block

        # TODO: make sure return value stays in register a

        # return 
        asm.append(["ret"])

        text = text + "\n" + asmPrinter(asm) + "\n.ends"

    return text

def asmPrinter(asm:list, indent=2):
    out = []
    asm = optimizeAsm(asm)
    for i in asm:
        #if DEBUG: print(f"line: {i}")
        if i==[]: out.append(""); continue #empty line
        out.append(f"{'  '*indent}{i[0]} {', '.join(i[1:])}")
    text = "\n".join(out)
    return text

def buildMain(block:Block)->list:
    globalManager = GlobalManager()
    ctx = ContextManager("main", globalManager)
    mainBlockAsm, functions = buildBlock(block, startContext=ctx, name="main")

    head = ".include \"../framework.asm\""
    pre = "\n;; --- main section --- \n.section \"main\"\n  main:"
    post = "\n    ret\n.ends"
    glo = globalPrinter(globalManager)
    fun = functionsPrinter(globalManager, functions)
    asmText = asmPrinter(mainBlockAsm)
    #if DEBUG: print(ctx)
    return "\n".join([head, glo, fun, pre, asmText, post])

def saveRegtoVar(var:IDENT, ctx:ContextManager, register="a"):
    reg = register.lower()
    if reg not in REGISTER_ORDER:
        raise RuntimeError(f"register '{register}' does not exist")
    """
    saves register 'reg' into var
    """
    if DEBUG: print(f"save register 'reg' into {var}")
    asm = []

    # move reg into a
    if reg != "a":
        asm.append(["ld", "a", reg])

    if var.name=="_":
        if DEBUG: print(f"ignoring save target because I don't like its name: \"_\"")
    elif var.isGlobal:
        ctx.globalManager.add(var)
        asm.append(["ld", f"({var.name})", "a"]) #load from heap
    elif ctx.globalManager.exists(var):
        asm.append(["ld", f"({var.name})", "a"]) #load from heap
    else:
        # calculate offset on stack
        offset = ctx.getVarOffset(var)
        if offset==-1: #does not exist yet
            ctx.addVar(var)
            if var.size==2:
                asm.append(["push", "af"])
            else:
                raise NotImplementedError(f"currently unable to save stuff larger than 2Bytes on the stack")
        else:
            asm.append(["ld", "hl", f"SP+{offset+1}"]) #save stackPointer into HL
            asm.append(["ld", "(hl)", "a"]) #load A into position HL
    return asm

def functionCall(call:FunctionCall, ctx)->list:            
    asm = []
    name = call.name
    params = call.params
    if DEBUG: print(f"call {name}({params})")
    if len(params)>len(REGISTER_ORDER):
        raise NotImplementedError(f"tried to call function with too many parameters: {len(params)} (max: {len(REGISTER_ORDER)})")

    if name in ["loadTiles1bpp", "setTiles"]:
        print(params)
        asm.append(["ld", "hl", f"{params[0].name}"])
        params = params[1:]

    for i in range(len(params)-1, -1, -1): #do backwards to set register a last
        p = params[i]
        r = REGISTER_ORDER[i]
        asm.extend(loadValue(p, ctx, r))
    asm.append(["call", f"{name}"])
    
    return asm

def loadValue(value, ctx:ContextManager, register="a")->list:
    register = register.lower()
    if register not in REGISTERS:
        raise RuntimeError(f"register '{register}' does not exist")
    """
    creates asm to calculate the value and leaves the result in register A
    """
    if DEBUG: print(f"write {value} into register A")
    asm = []
    asm.append([f";; load {value} into {register}"])
    if isinstance(value, INT):
        asm.append(["ld", "a", f"{value.value}"])
    elif isinstance(value, IDENT):
        # check if var is global
        if ctx.globalManager.exists(value):
            value.isGlobal = True
            if DEBUG: print(f"loading global value {value.name}")
            asm.append(["ld", "a", f"({value.name})"])
        else:
            # calculate offset on stack
            offset = ctx.getVarOffset(value)
            if offset==-1:
                # did not find var on stack
                raise RuntimeError(f"unable to load var '{value.name}' because it does not exist in the stack")
            else:
                # found var on stack
                asm.append(["ld", "hl", f"SP+{offset+1}"]) #save stackPointer into HL
                asm.append(["ld", "a", "(hl)"]) #load from position into register A
    elif isinstance(value, FunctionCall):
        asm.extend(functionCall(value, ctx))
    elif isinstance(value, ArithmeticExp):
        inst = value.gba
        if inst is None:
            raise NotImplementedError(f"unable to convert expression of type {type(value).__name__} to asm at this time")
        asm.extend(loadValue(value.right, ctx, "b"))
        asm.extend(loadValue(value.left, ctx, "a"))
        asm.append([inst, "b"])
    elif isinstance(value, BoolExpression):
        if DEBUG: print("# building bool expression")
        asm.extend(loadValue(value.right, ctx, "b"))
        asm.extend(loadValue(value.left, ctx, "a"))
        if isinstance(value, Equals):
            if DEBUG: print("# equals expression")
            tempName = getTempName()
            asm.append(["cp", "b"])
            asm.append(["ld", "a", "1"])
            asm.append(["jr", "z", tempName])
            asm.append(["ld", "a", "0"])
            asm.append([f"{tempName}:"])
        elif isinstance(value, NotEquals):
            if DEBUG: print("# notEquals expression")
            tempName = getTempName()
            asm.append(["cp", "b"])
            asm.append(["ld", "a", "1"])
            asm.append(["jr", "nz", tempName])
            asm.append(["ld", "a", "0"])
            asm.append([f"{tempName}:"])
        elif not value.gba is None:
            if DEBUG: print(f"# bool expression {value} with op code {value.gba}")
            # known op code
            asm.append([f";; {value.name}({value.left}{value.right})"])
            asm.append([f"{value.gba}", "b"])
        else:
            raise NotImplementedError(f"boolean expression {type(value).__name__} is not yet implemented")
    elif isinstance(value, BOOL):
        asm.append(["ld", "a", f"{value.value}"])
    else:
        raise NotImplementedError(f"unknown value of type '{type(value)}' in context ({ctx.name})")
    if register != "a":
        if DEBUG: print(f"moving result to new register {register}")
        #asm.append([f";; -> move to register {register}"])
        asm.append(["ld", f"{register}", "a"])
    return asm

def buildSkipIfFalse(exp:Exp, target:str, ctx:ContextManager)->list:
    asm = []
    if isinstance(exp, Equals):
        asm.append([f";; ({exp.left} == {exp.right})"])
        asm.extend(loadValue(exp.right, ctx, "b"))
        asm.extend(loadValue(exp.left, ctx, "a"))
        asm.append([f";; compute equals"])
        asm.append(["cp", "b"])
        asm.append(["jr", "nz", target])  #skip block if equal
    elif isinstance(exp, NotEquals):
        asm.append([f";; ({exp.left} != {exp.right})"])
        asm.extend(loadValue(exp.right, ctx, "b"))
        asm.extend(loadValue(exp.left, ctx, "a"))
        asm.append([f";; compute not-equals"])
        asm.append(["cp", "b"])
        asm.append(["jr", "z", target])  #skip block if not equal
    elif isinstance(exp, IDENT):
        asm.append([f";; ({exp})"])
        asm.extend(loadValue(exp, ctx, "b"))
        asm.append([f";; compare IDENT to 0"])
        asm.append(["ld", "a", "0"])
        asm.append(["cp", "b"])
        asm.append(["jr", "z", target])
    elif isinstance(exp, BoolExpression) and not exp.gba is None:
        op = exp.gba
        if DEBUG: print(f"boolean expression: {op}")
        asm.extend(loadValue(exp.right, ctx, "b"))
        asm.extend(loadValue(exp.left, ctx, "a"))
        asm.append([f";; compute result"])
        asm.append([f"{op}", "b"])
        asm.append([f";; compare result to 0"])
        asm.append(["ld", "b", "a"])
        asm.append(["ld", "a", "0"])
        asm.append(["cp", "b"])
        asm.append(["jr", "nz", target])  #skip block if equal
        if DEBUG: print("asm", asm)
    elif isinstance(exp, BOOL):
        if exp.value==1:
            asm.append([f";; (true) <- no skip check, just do it"])
            return asm
        else:
            asm.append([f";; (false) <- no skip check, just jump"])
            asm.append(["jp", target])
    else:
        raise NotImplementedError(f"expression '{type(exp)}' not implemented for jumps")
    return asm

def buildWhile(whileLoop:WhileLoop, ctx:ContextManager)->list:
    asm = []
    asm.append([f";; WHILE ({whileLoop.exp}) do"])
    start = getTempName()
    end = getTempName()

    if whileLoop.exp.value==0: #while (False)
        asm.append([f";; removed entire block because it is never executed"])
        return asm, []

    asm.append([f"{start}:"])                       # start:
    asm.extend(buildSkipIfFalse(whileLoop.exp, end, ctx)) # if (exp) goto end
    asmTemp, functions = buildBlock(whileLoop.block, parentCtx=ctx, name="while")
    asm.extend(asmTemp)       # content...
    asm.append(["jp", start])                       # goto start
    asm.append([f"{end}:"]) 
    return asm, functions

def buildIf(ifStatement:IfStatement, ctx:ContextManager)->tuple[list, list]:
    asm = []
    functions = []
    asm.append([f";; IF ({ifStatement.exp}) do"])

    if ifStatement.exp.value==0: #while (False)
        asm.append([f";; removed entire block because it is never executed"])
        return asm, []
    
    hasElse = not ifStatement.elseBlock is None

    endLabel = getTempName()
    elseLabel = getTempName()

    asm.extend(buildSkipIfFalse(ifStatement.exp, elseLabel, ctx)) # if (exp) goto end
    asmTemp, funcTemp = buildBlock(ifStatement.block, parentCtx=ctx, name="if")         # build content
    asm.extend(asmTemp)         # content...
    functions.extend(funcTemp)
    if hasElse: asm.append(["jp", f"{endLabel}"])

    asm.append([f"{elseLabel}:"])

    if hasElse:
        asm.append([";; ELSE do"])
        asmTemp, funcTemp = buildBlock(ifStatement.elseBlock, parentCtx=ctx, name="else")         # build content
        asm.extend(asmTemp)         # content...
        functions.extend(funcTemp)
        asm.append([f"{endLabel}:"]) # end
    
    return asm, functions

def buildBlock(block:Block, parentCtx=None, startContext=None, name="?")->list:
    asm = []
    functions = []
    ctx = None
    if parentCtx is None:
        if startContext is None: raise RuntimeError(f"cannot build block without context")
        ctx = startContext
    else:
        ctx = parentCtx.createChild(f"{name}")

    for elem in block.elements:
        #if DEBUG: print(f"building \"{type(elem).__name__}\" in ({ctx.name})")
        match type(elem).__name__:
            case "Assignment":
                asm.append([f";; {elem}"])
                # calculate value into a
                asm.extend(loadValue(elem.value, ctx))
                asm.extend(saveRegtoVar(elem.target, ctx))
            case "FunctionDecl":
                functions.append(elem)
            case "WhileLoop":
                asmTemp, funcs = buildWhile(elem, ctx)
                asm.extend(asmTemp)
                functions.extend(funcs)
            case "IfStatement":
                asmTemp, funcs = buildIf(elem, ctx)
                asm.extend(asmTemp)
                functions.extend(funcs)
            case "ReturnStatement":
                # eval expression into register a
                if not elem.exp is None: asm.extend(loadValue(elem.exp, ctx))
                #return
                asm.extend(ctx.removeFunctionFromStack())
                asm.append(["ret"])
            case "FunctionCall":
                asm.extend(loadValue(elem, ctx))
            case "Bytearray":
                ctx.globalManager.addArray(elem)
            case _:
                raise NotImplementedError(f"unknown element of type '{type(elem)}' in context ({ctx.name})")
        asm.append([]) #add empty line
    
    # return pointer to original position
    asm.extend(ctx.removeFromStack())

    return asm, functions