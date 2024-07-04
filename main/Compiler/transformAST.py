from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, Token
from abstractTree import *
import uuid

DEBUG = False

def getTempName():
    return f"temp_{uuid.uuid4().hex[:6]}"

def flattenExp(exp):
    if DEBUG: print(f"  exp: {exp}")
    if type(exp) in [INT, BOOL, IDENT, Bytearray]:
        if DEBUG: print(f"    ignoring {exp}")
        return [], exp
    elif isinstance(exp, FunctionCall):
        newElements = []
        idents = []
        for p in exp.params:
            nel, ident = flattenExp(p)
            newElements.extend(nel)
            idents.append(ident)
        return newElements, FunctionCall(exp.name, idents)
    else:
        if DEBUG: print(f"   working {exp}")
        el = []
        targetIdent = IDENT(getTempName())

        if isinstance(exp, BoolExpression) or isinstance(exp, ArithmeticExp):
            lEl, lIdent = flattenExp(exp.left)
            rEl, rIdent = flattenExp(exp.right)
            el.extend(lEl)
            el.extend(rEl)
            el.append(Assignment(targetIdent, type(exp)(lIdent, rIdent)))
        return el, targetIdent

def flattenBlock(block:Block):
    assert isinstance(block, Block)
    newElements = []
    for el in block.elements:
        if DEBUG: print(f"flattening: {el}")

        if isinstance(el, Assignment):
            nel, identLeft = flattenExp(el.target)
            newElements.extend(nel)
            nel, identRight = flattenExp(el.value)
            newElements.extend(nel)
            newElements.append(Assignment(identLeft, identRight))
        elif isinstance(el, FunctionCall):
            idents = []
            for p in el.params:
                nel, ident = flattenExp(p)
                newElements.extend(nel)
                idents.append(ident)
            newElements.append(FunctionCall(el.name, idents))
        elif isinstance(el, ReturnStatement):
            nel, ident = flattenExp(el.exp)
            newElements.extend(nel)
            newElements.append(ReturnStatement(ident))
        elif isinstance(el, FunctionDecl):
            el.block = flattenBlock(el.block)
            newElements.append(el)
        elif isinstance(el, IfStatement):
            el.block = flattenBlock(el.block)
            if not el.elseBlock is None:
                el.elseBlock = flattenBlock(el.elseBlock) 
            newElements.append(el)
        elif isinstance(el, WhileLoop):
            el.block = flattenBlock(el.block)
            newElements.append(el)
        elif isinstance(el, Bytearray):
            newElements.append(el)
        else:
            if DEBUG: print(f"skipping {el}")

    block.elements = newElements
    return block

def optimizeBlock(block:Block):
    return block