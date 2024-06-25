from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

def rprint(obj):
    if isinstance(obj, TerminalNodeImpl):
        print(obj)
    else:
        print(obj.toStringTree(recog=SlangParser))

class Exp(): pass

class INT(Exp):
    @staticmethod
    def fromTerminal(terminal:TerminalNodeImpl):
        return INT(int(terminal.getText()))

    def __init__(self, value:int):
        self.value = value
        
    def __repr__(self):
        return f"INT({self.value})"

class IDENT(Exp):
    @staticmethod
    def fromTerminal(ident:TerminalNodeImpl):
        return IDENT(ident.getText())
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

class Assignment():
    def fromContext(assignment:SlangParser.AssignmentContext):
        if isinstance(assignment, SlangParser.LineContext): 
            #line contexts are equivalent to assignments because they only ever have exactly one of them
            assignment = assignment.children[0]
        target = IDENT.fromTerminal(assignment.children[0])
        value = Expression(assignment.children[2])
        return Assignment(target, value)

    def __init__(self, target:IDENT, value:Exp):
        assert isinstance(value, Exp)
        assert isinstance(target, IDENT)
        self.target = target
        self.value = value
    
    def __repr__(self):
        return f"ASS({self.target}={self.value})"

class Prog():
    @staticmethod
    def fromContext(prog:SlangParser.ProgContext):
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
                    lines.append(Assignment.fromContext(line))
                case _:
                    pass
        return Prog(lines)

    def __init__(self, lines):
        self.lines = lines
    
    def print(self):
        for a in self.lines:
            print(a)

class FunctionCall(Exp):
    @staticmethod
    def fromContext(ctx:SlangParser.FunctionCallContext):
        params = []
        for c in ctx.children:
            if type(c)==TerminalNodeImpl: continue #skip ','
            params.append(Value(c))
        return FunctionCall(ctx.children[0].getText(), params)
    def __init__(self, name:str, params:list):
        self.name = name
        self.params = params
        self.value = None
    def __repr__(self): #jesus this is weird code
        return f"FUN_{self.name}({','.join(x.__repr__() for x in self.params)})"

def Expression(expression):
    exp = expression.children[0]
    match type(exp):
        case SlangParser.ValueContext:
            ex = Value(exp)
        case SlangParser.AdditionContext:
            ex = Addition.fromExpression(exp)
        case SlangParser.SubtractionContext:
            ex = Subtraction.fromExpression(exp)
        case SlangParser.MultiplicationContext:
            ex = Multiplication.fromExpression(exp)
        case SlangParser.DivisionContext:
            ex = Division.fromExpression(exp)
        case SlangParser.FunctionCallContext:
            ex = FunctionCall.fromContext(exp)
        case _:
            raise NotImplementedError(f"unknown type in Expression {type(exp)}")
    if not ex.value is None:
        return INT(ex.value)
    return ex

def Value(expression:SlangParser.ValueContext):
    assert type(expression)==SlangParser.ValueContext
    e = expression.children[0]
    match type(e).__name__:
        case "TerminalNodeImpl":
            text = e.getText()
            try: #TODO this is super ugly
                return INT.fromTerminal(e)
            except ValueError:
                return IDENT.fromTerminal(e)
        case "BracketsContext":
            return Brackets(e)
        case _:
            raise NotImplementedError(f"unknown type in Value {type(e)}")
    print("val", type(expression.children[0]))
    rprint(expression)

def Brackets(brackets:SlangParser.BracketsContext):
    child = brackets.children[1]
    return Expression(child)

class ArithmeticExp(Exp):
    @staticmethod
    def fromExpression(expression:SlangParser.ExpressionContext):
        raise NotImplementedError()

    def __init__(self, left, right):
        self.left = left
        self.right = right

        #try to resolve constant/known values stuff
        self.value = None
        if self.left.value!=None and self.right.value!=None:
            self.value = self.op(self.left.value, self.right.value)
    """
    def __init__(self, expression):
        self.left = Value(expression.children[0])
        self.right = Value(expression.children[2])

        #try to resolve constant/known values stuff
        self.value = None
        if self.left.value!=None and self.right.value!=None:
            self.value = self.op(self.left.value, self.right.value)
    """
    def __repr__(self):
        if not self.value is None:
            return f"{self.name}({self.left}{self.opStr}{self.right}={self.value})"
        return f"{self.name}({self.left}{self.opStr}{self.right})"

class Addition(ArithmeticExp):
    @staticmethod
    def fromExpression(expression:SlangParser.ExpressionContext):
        return Addition(Value(expression.children[0]), Value(expression.children[2]))
    
    def __init__(self, left, right):
        self.name = "ADD"
        self.op = int.__add__
        self.opStr = "+"
        self.type = SlangParser.AdditionContext
        self.gba = "add"
        super().__init__(left, right)

class Subtraction(ArithmeticExp):
    @staticmethod
    def fromExpression(expression:SlangParser.ExpressionContext):
        return Subtraction(Value(expression.children[0]), Value(expression.children[2]))
    
    def __init__(self, left, right):
        self.name = "SUB"
        self.op = int.__sub__
        self.opStr = "-"
        self.type = SlangParser.SubtractionContext
        self.gba = "sub"
        super().__init__(left, right)

class Multiplication(ArithmeticExp):
    @staticmethod
    def fromExpression(expression:SlangParser.ExpressionContext):
        return Multiplication(Value(expression.children[0]), Value(expression.children[2]))
    
    def __init__(self, left, right):
        #raise NotImplementedError("multiplication is not available ATM")
        self.name = "MUL"
        self.op = int.__mul__
        self.opStr = "*"
        self.type = SlangParser.MultiplicationContext
        self.gba = None
        super().__init__(left, right)

class Division(ArithmeticExp):
    @staticmethod
    def fromExpression(expression:SlangParser.ExpressionContext):
        return Division(Value(expression.children[0]), Value(expression.children[2]))
    
    def __init__(self, left, right):
        #raise NotImplementedError("division is not available ATM")
        self.name = "DIV"
        self.op = int.__floordiv__
        self.opStr = "/"
        self.type = SlangParser.DivisionContext
        self.gba = None
        super().__init__(left, right)
