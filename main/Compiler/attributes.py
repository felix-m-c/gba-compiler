from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, Token
from abstractTree import *

class Evaluator():
    def __init__(self, prog:Prog):
        prog.print()
        self.c = {}
        for ass in prog.lines:
            if type(ass)!=Assignment: continue #skip function calls #TODO change this once actual functions have been implemented
            res = self.eval(ass.value)
            self.c[ass.target] = res
            t = Token(); t._text = str(res)
            if not res is None:
                ass.value = INT(TerminalNodeImpl(t))
        prog.print()

    def get(self, ident):
        if not ident in self.c.keys():
            self.c[ident]=None
        return self.c[ident]

    def eval(self, exp):
        match type(exp).__name__:
            case "INT":
                return exp.value
            case "IDENT":
                exp.value = self.get(exp.name)
                return exp.value
            case "Addition":
                lConst = self.eval(exp.left)
                rConst = self.eval(exp.right)
                if lConst!=None and rConst!=None:
                    print(f"const: {lConst}+{rConst}")
                    return lConst+rConst
            case "Subtraction":
                lConst = self.eval(exp.left)
                rConst = self.eval(exp.right)
                if lConst!=None and rConst!=None:
                    print(f"const: {lConst}-{rConst}")
                    return lConst-rConst
            case "Multiplication":
                lConst = self.eval(exp.left)
                rConst = self.eval(exp.right)
                if lConst!=None and rConst!=None:
                    print(f"const: {lConst}*{rConst}")
                    return lConst*rConst
            case "Division":
                lConst = self.eval(exp.left)
                rConst = self.eval(exp.right)
                if lConst!=None and rConst!=None:
                    print(f"const: {lConst}/{rConst}")
                    return lConst/rConst
            case _:
                print(type(exp))
