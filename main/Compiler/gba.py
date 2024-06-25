from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, Token
from abstractTree import *

REGISTERS = ['a', 'c', 'b', 'e', 'd']

def getVars(lines):
    vars = set()
    for l in lines:
        if isinstance(l, Assignment):
            vars.add(l.target)
        else:
            continue
    return vars

def varPrinter(vars):
    pre = [
        ".ramsection \"Definitions\" slot 1"
    ]
    post = [
        ".ends"
    ]
    out = []
    indent = 1
    for v in vars:
        if v.name == '_': continue #skip reserved null reference
        out.append(f"{'  '*indent}{v.name} db ; uint8 {v.name};")
    full = pre+out+post
    return full

def toGBA(lines):
    asmLines = []
    vars = getVars(lines)
    #print(f"vars: {vars}")
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
    return vars, asmLines

def asmPrinter(vars:list, asm:list):
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
    for i in asm:
        if i==[]: 
            out.append("")
            continue
        out.append(f"{'  '*indent}{i[0]} {', '.join(i[1:])}")
    varStrings = varPrinter(vars)
    full = head+varStrings+pre+out+post
    text = "\n".join(full)
    return text