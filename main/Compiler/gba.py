from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, Token
from abstractTree import *
from flatten import getTempName

"""
add SP, -1      # platz machen
ld a, 10        # wert in a laden
ld HL, SP+0     # neuen stack pointer nach HL laden
ld (HL), a      # a nach (HL) auf dem stack speichern

außerdem: symbol table nachschlagen
"""


REGISTERS = ['a', 'c', 'b', 'e', 'd']

class GBAconverter():
    def __init__(self, startContext):
        self.vars = set()
        self.funcs = set()
        self.globs = []
        self.asm = []
        self.convertContext(startContext)

    def convertContext(self, context:Context, nameSpace=[]):
        for el in context.elements:
            match type(el).__name__:
                case "Assignment":
                    self.convertAssignment(el)
                case "FunctionDecl":
                    self.convertFunctionDecl(el)
                case "WhileLoop":
                    self.convertWhileLoop(el)
                case "IfStatement":
                    self.convertIfStatement(el)
            self.asm.append([])

    def loadValue(self, val, register:str):
        if isinstance(val, INT):
            self.asm.append(["ld", "a", f"{val.value}"])
        elif isinstance(val, IDENT):
            if not val.name in self.vars:
                raise NameError(f"'{val.name}' not defined in vars")
            if val.isGlobal:
                self.asm.append(["ld", "a", f"({val.name})"])
            else:
                # load from stack
                self.asm.append(["ld", "a", f"({val.name})"]) #TODO remove this because not everything is supposed to be global
        else:
            raise ValueError(f"unknown value value type: {type(val)}")
        if register!="a": # move into correct reg
            self.asm.append(["ld", register, "a"])

    def saveValue(self, register:str, target:IDENT):
        name = target.name

        if (not name in self.vars) and (name in self.funcs):
            raise NameError(f"tried to define '{name}' which is already the name of a function")
        assert isinstance(target, IDENT)
        
        if name == '_': return #skip reserved null reference
        self.vars.add(name)
        
        if register!="a":
            self.asm.append(["ld", "a", register])
        self.asm.append(["ld", f"({name})", "a"])

    def convertAssignment(self, assignment:Assignment):
        print(f"converting {assignment}")
        self.asm.append([f";; {assignment}"])
        target = assignment.target
        source = assignment.value
        # prepare parameters and do calculation
        if isinstance(source, INT) or isinstance(source, IDENT):
            self.loadValue(source, "a")
        elif isinstance(source, ArithmeticExp):
            inst = source.gba
            if inst is None:
                raise NotImplementedError(f"unable to convert expression of type {type(target).__name__} to asm at this time")
            
            self.loadValue(source.right, "b")
            self.loadValue(source.left, "a")
            self.asm.append([inst, "b"])
        
        elif isinstance(source, BoolExpression):
            self.loadValue(source.right, "b")
            self.loadValue(source.left, "a")
            if isinstance(source, Equals):
                tempName = getTempName()
                self.asm.append(["cp", "b"])
                self.asm.append(["ld", "a", "1"])
                self.asm.append(["jr", "z", tempName])
                self.asm.append(["ld", "a", "0"])
                self.asm.append([f"{tempName}:"])
            if isinstance(source, NotEquals):
                tempName = getTempName()
                self.asm.append(["cp", "b"])
                self.asm.append(["ld", "a", "0"])
                self.asm.append(["jr", "nz", tempName])
                self.asm.append(["ld", "a", "1"])
                self.asm.append([f"{tempName}:"])

        elif isinstance(source, FunctionCall):
            name = source.name
            params = source.params
            #print(f"call {name}({params})")
            if len(params)>len(REGISTERS):
                raise NotImplementedError(f"tried to call function with too many parameters: {len(params)} (max: {len(REGISTERS)})")
            for i in range(len(params)-1, -1, -1): #do backwards to set register a last
                p = params[i]
                r = REGISTERS[i]
                self.loadValue(p, r)
            self.asm.append(["call", name])
        else:
            raise NotImplementedError(f"unknown assignment right hand: {type(source).__name__}")        
        # save result
        self.saveValue("a", target)

    def convertFunctionDecl(self, functionDecl:FunctionDecl):
        name = functionDecl.name
        params = functionDecl.params
        ctx = functionDecl.context

        afterPos = getTempName()

        self.asm.append(["jp", afterPos])
        self.asm.append([f";; function {name}({params})"])

        if name in self.vars or name in self.funcs:
            raise NameError(f"tried to define function '{name}' while the name already exists")
         
        self.asm.append([f"{functionDecl.name}:"])
        self.convertContext(functionDecl.context)
        self.asm.append(["ret"])
        self.asm.append([f"{afterPos}:"])
        # we can ignore params for now, because everything is global anyways
        # #TODO move params onto stack

    def conditionalSkip(self, exp:BoolExpression, target:str):
        if isinstance(exp, Equals):
            self.loadValue(exp.right, "b")
            self.loadValue(exp.left, "a")
            self.asm.append(["cp", "b"])
            self.asm.append(["jr", "nz", target])  #skip block if equal
        elif isinstance(exp, NotEquals):
            self.loadValue(exp.right, "b")
            self.loadValue(exp.left, "a")
            self.asm.append(["cp", "b"])
            self.asm.append(["jr", "z", target])  #skip block if not equal
        elif isinstance(exp, IDENT):
            self.loadValue(exp, "b")
            self.loadValue(INT(1), "a")
            self.asm.append(["cp", "b"])
            self.asm.append(["jr", "nz", target])
        else:
            raise NotImplementedError(f"expression '{type(exp)}' not implemented for jumps")


    def convertWhileLoop(self, whileLoop:WhileLoop):
        self.asm.append([f";; WHILE ({whileLoop.exp}) do"])
        start = getTempName()
        end = getTempName()

        self.asm.append([f"{start}:"])           # start:
        self.conditionalSkip(whileLoop.exp, end) # if (exp) goto end
        self.convertContext(whileLoop.context)   # content...
        self.asm.append(["jp", start])           # goto start
        self.asm.append([f"{end}:"])             # end

    def convertIfStatement(self, ifStatement:IfStatement):
        end = getTempName()
        self.conditionalSkip(ifStatement.exp, end) # if (exp) goto end
        self.convertContext(ifStatement.context)   # content...
        self.asm.append([f"{end}:"])             # end

    @staticmethod
    def toGBAOLD(context):
        asmLines = []
        var = getVars(lines)
        #print(f"vars: {var}")
        for l in lines:
            if isinstance(l, Assignment):
                #print(l)
                target = l.target
                source = l.value
                asmLines.append([])
                asmLines.append([f";; {l}"])
                if isinstance(source, INT):
                    asmLines.append(["ld", "a", str(source.value)])
                    asmLines.append(["ld", f"({target.name})", "a"])
                elif isinstance(source, IDENT):
                    asmLines.append(["ld", "a", f"({source.name})"])
                    asmLines.append(["ld", f"({target.name})", "a"])
                elif isinstance(source, ArithmeticExp):
                    inst = source.gba
                    if inst is None:
                        raise NotImplementedError(f"unable to convert expression of type {type(target).__name__} to asm at this time")
                    left = source.left
                    if isinstance(left, INT): left = f"{left.value}"
                    else: left = f"({left.name})"
                    right = source.right
                    if isinstance(right, INT): right = f"{right.value}"
                    else: right = f"({right.name})"
                    #print(left, right)

                    asmLines.append(["ld", "a", right])
                    asmLines.append(["ld", "b", "a"])
                    asmLines.append(["ld", "a", left])
                    asmLines.append([inst, "b"])
                    asmLines.append(["ld", f"({target.name})", "a"])
                elif isinstance(source, FunctionCall):
                    name = source.name
                    params = source.params
                    #print(f"call {name}({params})")
                    if len(params)>len(REGISTERS):
                        raise NotImplementedError(f"tried to call function with too many parameters: {len(params)} (max: {len(REGISTERS)})")
                    for i in range(len(params)-1, -1, -1):
                        p = params[i]
                        if isinstance(p, INT): p = f"{p.value}"
                        else: p = f"({p.name})"
                        r = REGISTERS[i]
                        #print(p, r)
                        #ugly workaround because <ld reg (var)> only works for reg='a' 
                        asmLines.append(["ld", "a", p])
                        if r != "a": 
                            asmLines.append(["ld", r, "a"])
                    asmLines.append(["call", name])
                else:
                    raise NotImplementedError(f"unknown assignment right hand: {type(source).__name__}")
            else:
                raise NotImplementedError(f"unknown line type: {type(l)}")
        return var, asmLines

    def varPrinter(self):
        pre = [
            ".ramsection \"Definitions\" slot 1"
        ]
        post = [
            ".ends"
        ]
        out = []
        indent = 1
        for v in self.vars:
            out.append(f"{'  '*indent}{v} db ; uint8 {v};")
        full = pre+out+post
        return full

    def asmPrinter(self):
        print("-"*20)
        #for l in self.asm:
        #    print(l)
        
        head = [
            ".include \"../framework.asm\""
        ]
        pre = [
            ".section \"main\"",
            "  main:"
        ]
        post = [
            "    ret",
            ".ends"
        ]
        out = []
        indent = 2
        for i in self.asm:
            if i==[]: 
                out.append("")
                continue
            out.append(f"{'  '*indent}{i[0]} {', '.join(i[1:])}")
        varStrings = self.varPrinter()
        full = head+varStrings+pre+out+post
        text = "\n".join(full)
        return text