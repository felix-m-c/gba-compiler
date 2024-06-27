from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, Token
from abstractTree import *
import uuid

def getTempName():
    return f"temp_{uuid.uuid4().hex[:6]}"

def flat(exp:Exp)->tuple[list, IDENT]:
    assert isinstance(exp, Exp)
    if isinstance(exp, ArithmeticExp):
        newLines = []
        left = exp.left
        right = exp.right
        if isinstance(left, ArithmeticExp) or isinstance(left, FunctionCall):
            newIdent = IDENT(getTempName())
            nl, ident = flat(left)
            newLines += nl
            newLines.append(Assignment(newIdent, ident))
            left = newIdent
        if isinstance(right, ArithmeticExp) or isinstance(right, FunctionCall):
            newIdent = IDENT(getTempName())
            nl, ident = flat(right)
            newLines += nl
            newLines.append(Assignment(newIdent, ident))
            right = newIdent
        return newLines, type(exp)(left, right)
    elif isinstance(exp, FunctionCall):
        #print("flattening function call", exp)
        newLines = []
        idents = []
        for p in exp.params:
            newIdent = p
            if isinstance(p, ArithmeticExp) or isinstance(p, FunctionCall):
                newIdent = IDENT(getTempName())
                nl, ident = flat(p)
                newLines += nl
                newLines.append(Assignment(newIdent, ident))
            idents.append(newIdent)
        return newLines, FunctionCall(exp.name, idents)
    else:
        return [], exp

def flatten(context:Context):
    #print("flatten:", type(context))
    assert isinstance(context, Context)
    newElements = []
    for el in context.elements:
        #print(f"line: {type(el)}")
        if isinstance(el, Assignment):
            val = el.value
            newNewElements, tVar = flat(val)
            newElements += newNewElements
            newElements.append(Assignment(el.target, tVar))
        elif isinstance(el, FunctionDecl):
            el.context = flatten(el.context)
            newElements.append(el)
        elif isinstance(el, IfStatement):
            el.context = flatten(el.context)
            newElements.append(el)
        elif isinstance(el, WhileLoop):
            el.context = flatten(el.context)
            newElements.append(el)
        else:
            newElements.append(el)
    #print("---")
    context.elements = newElements
    return context