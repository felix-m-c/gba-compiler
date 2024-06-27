from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

"""
    # Elements that are removed when building the AST
    (prog) -> (context) -> Block
    (brackets) -> Exp

    Assignment(target:IDENT, value:Exp)
        # move value of Exp into target

    Exp
        # Has a getValue (possibly known at compiletime)
        ArithmeticExpression(left, ?right)
            Addition
            Subtraction
            Multiplication
            Division
        BooleanExpression(left, ?right)
            Equals
            NotEquals
        FunctionCall(param1, param2, ...)
        IDENT(word)
        INT(num)
        BOOL()

    FunctionDeclaration(name:ident, lines:Block)

    IfStatement(ex:BooleanExpression)

    IfElseStatement()

    WhileLoop
"""

def rprint(obj):
    if isinstance(obj, TerminalNodeImpl):
        print(obj)
    else:
        print(obj.toStringTree(recog=SlangParser))

class Exp(): pass

def getValue(value:SlangParser.ValueContext):
    val = value.children[0]
    match type(val).__name__:
        case "IdentContext":
            return getIDENT(val)
        case "S_intContext":
            return getINT(val)
        case "BracketsContext":
            return getBrackets(val)
        case "S_boolContext":
            return getBOOL(val)
        case _:
            raise NotImplementedError(f"unknown type in getValue {type(val)} '{val.getText()}'")

def getINT(s_int:SlangParser.S_intContext):
    assert isinstance(s_int, SlangParser.S_intContext)
    return INT(int(s_int.getText()))
class INT(Exp):
    def __init__(self, value:int):
        self.value = value  
    def __repr__(self):
        return f"INT({self.value})"

def getBOOL(s_bool:SlangParser.S_boolContext):
    assert isinstance(s_bool, SlangParser.S_boolContext)
    text = s_bool.getText()
    b = False
    if text=="True":
        b = True
    elif text=="False":
        b = False
    else:
        raise NameError(f"unknown boolean literal '{text}'")
    return BOOL(b)
class BOOL(Exp):
    def __init__(self, value:bool):
        assert isinstance(value, bool)
        self.value = int(value) #to 0/1
    def __repr__(self):
        return f"BOOL({self.value})"

def getIDENT(ident:SlangParser.IdentContext):
    assert isinstance(ident, SlangParser.IdentContext)
    if ident.children[0].getText()=="global":
        return IDENT(ident.children[1].getText(), isGlobal=True)
    else:
        return IDENT(ident.children[0].getText())
class IDENT(Exp):
    def __init__(self, name, isGlobal=False):
        self.name = name
        self.value = None
        self.isGlobal = isGlobal
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if type(other)!=type(self): return False
        return self.__hash__()==other.__hash__()

    def __repr__(self):
        return f"{'GLOB:' if self.isGlobal else ''}ID({self.name})"

def getAssignment(assignment:SlangParser.AssignmentContext):
    assert isinstance(assignment, SlangParser.AssignmentContext)
    elements = assignment.children
    target = getIDENT(elements[0])
    assert isinstance(elements[1], TerminalNodeImpl)
    value = getExpression(elements[2])
    return Assignment(target, value)
class Assignment():    
    def __init__(self, target:IDENT, value:Exp):
        assert isinstance(value, Exp)
        assert isinstance(target, IDENT)
        self.target = target
        self.value = value
    
    def __repr__(self):
        return f"ASS({self.target} = {self.value})"

def getProg(prog:SlangParser.ProgContext):
    assert isinstance(prog, SlangParser.ProgContext)
    return getContext(prog.children[0])

def getContext(context:SlangParser.ContextContext):
    assert type(context)==SlangParser.ContextContext
    elements = []
    for child in context.children:
        match type(child).__name__:
            case "LineContext":
                l = getLine(child)
                if l!=None: 
                    elements.append(l)
                else:
                    #print(f"{type(child.children[0])} has no representation in the AST")
                    pass
            case "NewlineContext":
                pass #ignore newlines
            case _:
                raise NotImplementedError(f"unknown element in context: {type(child)}, '{child.getText()}'")
    return Context(elements)
class Context():
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self):
        return 'CTX{'+f"\n{'\n'.join(x.__repr__() for x in self.elements)}\n"+'}'

def getLine(line:SlangParser.LineContext):
    assert isinstance(line, SlangParser.LineContext)
    elem = line.children[0]
    match type(elem).__name__:
        case "AssignmentContext":
            return getAssignment(elem)
        case "FunctionDeclContext":
            return getFunctionDecl(elem)
        case "IfStatementContext":
            return getIfStatement(elem)
        case "WhileLoopContext":
            return getWhileLoop(elem)
        case "CommentContext":
            return None # no representation in the AST
        case _:
            raise NotImplementedError(f"unknown element in Line: {type(child)}, '{child.getText()}'")

def getBlock(block:SlangParser.BlockContext):
    assert isinstance(block, SlangParser.BlockContext)
    for c in block.children: #search the single context inside the block (might have newlines etc around it)
        if type(c)==SlangParser.ContextContext:
            return getContext(c)
    return Context([])

def getFunctionCall(ctx:SlangParser.FunctionCallContext):
    name = None
    params = []
    for c in ctx.children:
        if type(c) == TerminalNodeImpl: continue #skip and '()'
        if name==None:
            name = c
        else:
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
    return getExpression(child)

def getExpression(expression:SlangParser.ExpressionContext):
    assert isinstance(expression, SlangParser.ExpressionContext)
    exp = expression.children[0]
    match type(exp):
        case SlangParser.ValueContext:
            ex = getValue(exp)
        case SlangParser.FunctionCallContext:
            ex = getFunctionCall(exp)
        case SlangParser.ArithmeticExpressionContext:
            ex = getArithmeticExp(exp.children[0])
        case SlangParser.BoolExpressionContext:
            ex = getBoolExpression(exp.children[0])
        case _:
            raise NotImplementedError(f"unknown type in Expression {type(exp)}")
    if not ex.value is None:
        return INT(ex.value)
    return ex
def getArithmeticExp(exp):
    if isinstance(exp, SlangParser.ArithmeticExpressionContext):
        exp = exp.children[0]
    match type(exp):
        case SlangParser.AdditionContext:
            return getAddition(exp)
        case SlangParser.SubtractionContext:
            return getSubtraction(exp)
        case SlangParser.MultiplicationContext:
            return getMultiplication(exp)
        case SlangParser.DivisionContext:
            return getDivision(exp)
        case _:
            raise NotImplementedError(f"not a known arithmetic expression: {type(exp)}")

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
            return f"{self.name}({self.left} {self.opStr} {self.right} = {self.value})"
        return f"{self.name}({self.left} {self.opStr} {self.right})"

def getAddition(expression:SlangParser.AdditionContext):
    assert isinstance(expression, SlangParser.AdditionContext)
    return Addition(getValue(expression.children[0]), getValue(expression.children[2]))
class Addition(ArithmeticExp):
    def __init__(self, left, right):
        self.name = "ADD"
        self.op = int.__add__
        self.opStr = "+"
        self.type = SlangParser.AdditionContext
        self.gba = "add"
        super().__init__(left, right)

def getSubtraction(expression:SlangParser.SubtractionContext):
    assert isinstance(expression, SlangParser.SubtractionContext)
    return Subtraction(getValue(expression.children[0]), getValue(expression.children[2]))
class Subtraction(ArithmeticExp):
    def __init__(self, left, right):
        self.name = "SUB"
        self.op = int.__sub__
        self.opStr = "-"
        self.type = SlangParser.SubtractionContext
        self.gba = "sub"
        super().__init__(left, right)

def getMultiplication(expression:SlangParser.MultiplicationContext):
    assert isinstance(expression, SlangParser.MultiplicationContext)
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

def getDivision(expression:SlangParser.DivisionContext):
    assert isinstance(expression, SlangParser.DivisionContext)
    return Division(getValue(expression.children[0]), getValue(expression.children[2]))
class Division(ArithmeticExp):
    def __init__(self, left, right):
        self.name = "DIV"
        self.op = int.__floordiv__
        self.opStr = "/"
        self.type = SlangParser.DivisionContext
        self.gba = None
        super().__init__(left, right)

def getBoolExpression(exp):
    if isinstance(exp, SlangParser.BoolExpressionContext):
        exp = exp.children[0]
    match type(exp):
        case SlangParser.EqualsContext:
            return getEquals(exp)
        case SlangParser.NotEqualsContext:
            return getNotEquals(exp)
        case SlangParser.S_boolContext:
            return getBOOL(exp)
        case SlangParser.IdentContext:
            return getIDENT(exp)
        case _:
            raise NotImplementedError(f"not a known boolean expression: {type(exp)}")
class BoolExpression(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

        #try to resolve constant/known values stuff
        self.value = None
    def __repr__(self):
        if not self.value is None:
            return f"{self.name}({self.left} {self.opStr} {self.right} = {self.value})"
        return f"{self.name}({self.left} {self.opStr} {self.right})"

def getEquals(expression:SlangParser.EqualsContext):
    assert isinstance(expression, SlangParser.EqualsContext)
    return Equals(getValue(expression.children[0]), getValue(expression.children[2]))
class Equals(BoolExpression):
    def __init__(self, left, right):
        self.name = "EQ"
        self.op = int.__eq__
        self.opStr = "=="
        self.type = SlangParser.EqualsContext
        self.gba = None
        super().__init__(left, right)
        self.smartEval()
    def smartEval(self):
        if self.left.value!=None and self.right.value!=None:
            val = self.left.value == self.right.value
            self.value = 1 if val else 0
        if isinstance(self.left, IDENT) and isinstance(self.right, IDENT):
            if self.left.name == self.right.name:
                self.value = 1

def getNotEquals(expression:SlangParser.NotEqualsContext):
    assert isinstance(expression, SlangParser.NotEqualsContext)
    return NotEquals(getValue(expression.children[0]), getValue(expression.children[2]))
class NotEquals(BoolExpression):
    def __init__(self, left, right):
        self.name = "NEQ"
        self.op = lambda a, b: not int.__eq__(a, b)
        self.opStr = "!="
        self.type = SlangParser.NotEqualsContext
        self.gba = None
        super().__init__(left, right)
        self.smartEval()
    def smartEval(self):
        if self.left.value!=None and self.right.value!=None:
            val = self.left.value != self.right.value
            self.value = 1 if val else 0
        if isinstance(self.left, IDENT) and isinstance(self.right, IDENT):
            if self.left.name != self.right.name:
                self.value = 1

def getFunctionDecl(decl:SlangParser.FunctionDeclContext):
    assert isinstance(decl, SlangParser.FunctionDeclContext)
    children = decl.children
    ident = getIDENT(children[0])
    context = getBlock(children[-1])
    params = [getValue(x) for x in children[2:-2]]
    return FunctionDecl(ident, params, context)
class FunctionDecl():
    def __init__(self, ident:IDENT, params:list, context:Context):
        self.name = ident.name
        self.params = params
        self.context = context
    def __repr__(self):
        return f"FUNC[{self.name}]({', '.join([x.__repr__() for x in self.params])})({self.context})"

def getWhileLoop(loop:SlangParser.WhileLoopContext):
    assert isinstance(loop, SlangParser.WhileLoopContext)
    boolExp, ctx = None, None
    for el in loop.children:
        if isinstance(el, SlangParser.BoolExpressionContext):
            boolExp = getBoolExpression(el)
        elif isinstance(el, SlangParser.BlockContext):
            ctx = getBlock(el)
        else:
            #print(f"ignored {type(el)} in while loop")
            pass
    return WhileLoop(boolExp, ctx)
class WhileLoop():
    def __init__(self, exp:BoolExpression, context:Context):
        self.exp = exp
        self.context = context
    def __repr__(self):
        return f"WHILE ({self.exp}) {self.context}"
    
def getIfStatement(statement:SlangParser.IfStatementContext):
    assert isinstance(statement, SlangParser.IfStatementContext)
    boolExp, ctx = None, None
    for el in statement.children:
        if isinstance(el, SlangParser.BoolExpressionContext):
            boolExp = getBoolExpression(el)
        if isinstance(el, SlangParser.BlockContext):
            ctx = getBlock(el)
    return IfStatement(boolExp, ctx)
class IfStatement():
    def __init__(self, exp:BoolExpression, context:Context):
        self.exp = exp
        self.context = context
    def __repr__(self):
        return f"IF ({self.exp}) {self.context}"