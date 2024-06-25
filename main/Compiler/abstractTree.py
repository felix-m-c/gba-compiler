from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

def rprint(obj):
    if isinstance(obj, TerminalNodeImpl):
        print(obj)
    else:
        print(obj.toStringTree(recog=SlangParser))

class Exp(): pass

def getValue(expression:SlangParser.ValueContext):
    print(type(expression))
    assert type(expression)==SlangParser.ValueContext
    e = expression.children[0]
    match type(e).__name__:
        case "TerminalNodeImpl":
            text = e.getText()
            try: #TODO this is super ugly
                return getINT(e)
            except ValueError:
                return getIDENT(e)
        case "BracketsContext":
            return Brackets(e)
        case _:
            raise NotImplementedError(f"unknown type in Value {type(e)}")
    print("val", type(expression.children[0]))
    rprint(expression)

def getINT(terminal:TerminalNodeImpl):
    assert isinstance(terminal, TerminalNodeImpl)
    return INT(int(terminal.getText()))
class INT(Exp):
    def __init__(self, value:int):
        self.value = value  
    def __repr__(self):
        return f"INT({self.value})"

def getIDENT(terminal:TerminalNodeImpl):
    assert isinstance(terminal, TerminalNodeImpl)
    return IDENT(terminal.getText())
class IDENT(Exp):
    def __init__(self, name):
        self.name = name
        self.value = None
    
    def __hash__(self):
        #print(f"hash: {self.name} {hash(self.name)}")
        return hash(self.name)
    
    def __eq__(self, other):
        if type(other)!=type(self): return False
        return self.__hash__()==other.__hash__()

    def __repr__(self):
        return f"ID({self.name})"

def getLine(line:SlangParser.LineContext):
    assert isinstance(line, SlangParser.LineContext)
    return getAssignment(line.children[0])

def getAssignment(assignment:SlangParser.AssignmentContext):
    target = getIDENT(assignment.children[0])
    value = getExpression(assignment.children[2])
    return Assignment(target, value)
class Assignment():    
    def __init__(self, target:IDENT, value:Exp):
        assert isinstance(value, Exp)
        assert isinstance(target, IDENT)
        self.target = target
        self.value = value
    
    def __repr__(self):
        return f"ASS({self.target}={self.value})"

def getProg(prog:SlangParser.ProgContext):
    lines = []
    assert type(prog)==SlangParser.ProgContext
    for line in prog.children:
        #print(type(line))
        if isinstance(line, ErrorNodeImpl):
            print(f"Parser error at object: '{line.getText()}'")
            continue
        if isinstance(line, TerminalNodeImpl): 
            continue #ignore newlines, EOF etc.
        line = line.children[0]
        match type(line).__name__:
            case "AssignmentContext":
                lines.append(getAssignment(line))
            case _:
                pass
    return Prog(lines)
class Prog():

    def __init__(self, lines):
        self.lines = lines
    
    def print(self):
        for a in self.lines:
            print(a)

def getFunctionCall(ctx:SlangParser.FunctionCallContext):
    params = []
    for c in ctx.children:
        if type(c)==TerminalNodeImpl: continue #skip ','
        params.append(getValue(c))
    return FunctionCall(ctx.children[0].getText(), params)
class FunctionCall(Exp):
    def __init__(self, name:str, params:list):
        self.name = name
        self.params = params
        self.value = None
    def __repr__(self): #jesus this is weird code
        return f"FUN_{self.name}({','.join(x.__repr__() for x in self.params)})"

def getBrackets(brackets:SlangParser.BracketsContext):
    child = brackets.children[1]
    return Expression(child)

def getExpression(expression:SlangParser.ExpressionContext):
    assert isinstance(expression, SlangParser.ExpressionContext)
    exp = expression.children[0]
    match type(exp):
        case SlangParser.ValueContext:
            ex = getValue(exp)
        case SlangParser.AdditionContext:
            ex = getAddition(exp)
        case SlangParser.SubtractionContext:
            ex = getSubtraction(exp)
        case SlangParser.MultiplicationContext:
            ex = getMultiplication(exp)
        case SlangParser.DivisionContext:
            ex = getDivision(exp)
        case SlangParser.FunctionCallContext:
            ex = getFunctionCall(exp)
        case _:
            raise NotImplementedError(f"unknown type in Expression {type(exp)}")
    if not ex.value is None:
        return INT(ex.value)
    return ex
class ArithmeticExp(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

        #try to resolve constant/known values stuff
        self.value = None
        if self.left.value!=None and self.right.value!=None:
            self.value = self.op(self.left.value, self.right.value)
    def __repr__(self):
        if not self.value is None:
            return f"{self.name}({self.left}{self.opStr}{self.right}={self.value})"
        return f"{self.name}({self.left}{self.opStr}{self.right})"

def getAddition(expression:SlangParser.ExpressionContext):
    assert isinstance(expression, SlangParser.ExpressionContext)
    return Addition(Value(expression.children[0]), Value(expression.children[2]))
class Addition(ArithmeticExp):
    def __init__(self, left, right):
        self.name = "ADD"
        self.op = int.__add__
        self.opStr = "+"
        self.type = SlangParser.AdditionContext
        self.gba = "add"
        super().__init__(left, right)

def getSubtraction(expression:SlangParser.ExpressionContext):
    assert isinstance(expression, SlangParser.ExpressionContext)
    return Subtraction(Value(expression.children[0]), Value(expression.children[2]))
class Subtraction(ArithmeticExp):
    def __init__(self, left, right):
        self.name = "SUB"
        self.op = int.__sub__
        self.opStr = "-"
        self.type = SlangParser.SubtractionContext
        self.gba = "sub"
        super().__init__(left, right)
    
def getMultiplication(expression:SlangParser.ExpressionContext):
    assert isinstance(expression, SlangParser.ExpressionContext)
    return Multiplication(getValue(expression.children[0]), getValue(expression.children[2]))
class Multiplication(ArithmeticExp):
    def __init__(self, left, right):
        #raise NotImplementedError("multiplication is not available ATM")
        self.name = "MUL"
        self.op = int.__mul__
        self.opStr = "*"
        self.type = SlangParser.MultiplicationContext
        self.gba = None
        super().__init__(left, right)

def getDivision(expression:SlangParser.ExpressionContext):
    assert isinstance(expression, SlangParser.ExpressionContext)
    return Division(getValue(expression.children[0]), getValue(expression.children[2]))
class Division(ArithmeticExp):
    def __init__(self, left, right):
        #raise NotImplementedError("division is not available ATM")
        self.name = "DIV"
        self.op = int.__floordiv__
        self.opStr = "/"
        self.type = SlangParser.DivisionContext
        self.gba = None
        super().__init__(left, right)
