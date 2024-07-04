from out.SlangParser import SlangParser
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

"""
    # Elements that are removed when building the AST
    (prog) -> (context) -> ClosedBlock
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

    FunctionDeclaration(name:ident, lines:ClosedBlock)

    IfStatement(ex:BooleanExpression)

    IfElseStatement()

    WhileLoop
"""
TAB = "  "


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
    return INT(int(s_int.getText(), 0))
class INT(Exp):
    def __init__(self, value:int):
        self.value = value  
    def __repr__(self, indent=0):
        return f"{TAB*indent}INT({self.value})"

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
    def __repr__(self, indent=0):
        return f"{TAB*indent}BOOL({self.value})"

def getIDENT(ident:SlangParser.IdentContext):
    assert isinstance(ident, SlangParser.IdentContext)
    if ident.children[0].getText()=="global":
        return IDENT(ident.children[1].getText(), isGlobal=True)
    else:
        return IDENT(ident.children[0].getText())
class IDENT(Exp):
    def __init__(self, name, size=2, isGlobal=False):
        self.name = name
        self.value = None
        self.isGlobal = isGlobal
        self.size = size
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if type(other)!=type(self): return False
        return self.__hash__()==other.__hash__()

    def __repr__(self, indent=0):
        return f"{TAB*indent}{'GLOB:' if self.isGlobal else ''}ID({self.name})"

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
    
    def __repr__(self, indent=0):
        return f"{TAB*indent}ASS({self.target} = {self.value})"

def getProg(prog:SlangParser.ProgContext):
    assert isinstance(prog, SlangParser.ProgContext)
    return getBlock(prog.children[0])

def getBlock(block:SlangParser.BlockContext):
    assert type(block)==SlangParser.BlockContext
    elements = []
    for child in block.children:
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
                raise NotImplementedError(f"unknown element in block: {type(child)}, '{child.getText()}'")
    return Block(elements)
class Block():
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self, indent=0):
        return 'BLOCK{'+f"\n{'\n'.join(x.__repr__(indent=indent+1) for x in self.elements)}\n"+TAB*indent+'}'

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
        case "ReturnStatementContext":
            return getReturnStatement(elem)
        case "FunctionCallContext":
            return getFunctionCall(elem)
        case "ByteArrayContext":
            return getByteArray(elem)
        case _:
            raise NotImplementedError(f"unknown element in Line: {type(elem)}, '{elem.getText()}'")

def getByteArray(byteArray:SlangParser.ByteArrayContext):
    assert isinstance(byteArray, SlangParser.ByteArrayContext)
    children = list(filter(lambda x: type(x) not in [TerminalNodeImpl, SlangParser.NewlineContext], byteArray.children))
    ident = getIDENT(children[0])
    byteList = getByteList(children[1])
    return Bytearray(ident, byteList)
class Bytearray():
    def __init__(self, ident:IDENT, byteList:list):
        self.name = ident
        self.byteList = byteList
        self.value = None
    def __repr__(self, indent=0):
        return f"{TAB*indent}BYTES({self.name})[{self.byteList}]"

def getByteList(byteList:SlangParser.ByteListContext)->list[INT]:
    assert isinstance(byteList, SlangParser.ByteListContext)
    children = list(filter(lambda x: type(x) not in [TerminalNodeImpl, SlangParser.NewlineContext], byteList.children))
    
    byteList = []
    for c in children:
        if isinstance(c, SlangParser.S_intContext):
            byteList.append(getINT(c))
        elif isinstance(c, SlangParser.S_boolContext):
            boo = getBOOL(c)
            byteList.append(INT(c.value))
        else:
            raise NotImplementedError(f"cannot build byte from {type(c).__name__}")
    return byteList

def getReturnStatement(statement:SlangParser.ReturnStatementContext):
    assert isinstance(statement, SlangParser.ReturnStatementContext)
    params = statement.children[1:-1]
    exp = None
    if params != []:
        exp = getExpression(statement.children[1])
    return ReturnStatement(exp)
class ReturnStatement():
    def __init__(self, exp:Exp):
        self.exp = exp
    def __repr__(self, indent=0): #jesus this is weird code
        return f"{TAB*indent}RETURN({self.exp.__repr__()})"

def getClosedBlock(closedBlock:SlangParser.ClosedBlockContext):
    assert isinstance(closedBlock, SlangParser.ClosedBlockContext)
    for c in closedBlock.children: #search the single block inside the closedBlock (might have newlines etc around it)
        if type(c)==SlangParser.BlockContext:
            return getBlock(c)
    return Block([])

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
    def __repr__(self, indent=0): #jesus this is weird code
        return f"{TAB*indent}FUN_{self.name}({','.join(x.__repr__() for x in self.params)})"

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
    def __repr__(self, indent=0):
        if not self.value is None:
            return f"{TAB*indent}{self.name}({self.left} {self.opStr} {self.right} = {self.value})"
        return f"{TAB*indent}{self.name}({self.left} {self.opStr} {self.right})"

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
        case SlangParser.Equals_opContext:
            return getEquals(exp)
        case SlangParser.NotEquals_opContext:
            return getNotEquals(exp)
        case SlangParser.S_boolContext:
            return getBOOL(exp)
        case SlangParser.IdentContext:
            return getIDENT(exp)
        case SlangParser.And_opContext:
            return getAnd(exp)
        case SlangParser.Or_opContext:
            return getOr(exp)
        case SlangParser.Xor_opContext:
            return getXor(exp)
        case _:
            raise NotImplementedError(f"not a known boolean expression: {type(exp)}")
class BoolExpression(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

        #try to resolve constant/known values stuff
        self.value = None
    def __repr__(self, indent=0):
        if not self.value is None:
            return f"{TAB*indent}{self.name}({self.left} {self.opStr} {self.right} = {self.value})"
        return f"{TAB*indent}{self.name}({self.left} {self.opStr} {self.right})"

def getEquals(expression:SlangParser.Equals_opContext):
    assert isinstance(expression, SlangParser.Equals_opContext)
    return Equals(getValue(expression.children[0]), getValue(expression.children[2]))
class Equals(BoolExpression):
    def __init__(self, left, right):
        self.name = "EQ"
        self.op = int.__eq__
        self.opStr = "=="
        self.type = SlangParser.Equals_opContext
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

def getNotEquals(expression:SlangParser.NotEquals_opContext):
    assert isinstance(expression, SlangParser.NotEquals_opContext)
    return NotEquals(getValue(expression.children[0]), getValue(expression.children[2]))
class NotEquals(BoolExpression):
    def __init__(self, left, right):
        self.name = "NEQ"
        self.op = lambda a, b: not int.__eq__(a, b)
        self.opStr = "!="
        self.type = SlangParser.NotEquals_opContext
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

def getAnd(exp:SlangParser.And_opContext):
    assert isinstance(exp, SlangParser.And_opContext)
    return AndOp(getValue(exp.children[0]), getValue(exp.children[2]))
class AndOp(BoolExpression):
    def __init__(self, left, right):
        self.name = "AND"
        self.op = lambda a, b: int.__and__(a, b)
        self.opStr = "&"
        self.type = SlangParser.And_opContext
        self.gba = "and"
        super().__init__(left, right)
        #print(f"AndOp Value: {self.value}")
        self.smartEval()
        #print(f"AndOp smart Value: {self.value}")
    def smartEval(self):
        if self.left.value!=None and self.right.value!=None:
            val = self.left.value & self.right.value
            self.value = int(val)
        if isinstance(self.left, IDENT) and isinstance(self.right, IDENT):
            if self.left.name == self.right.name:
                self.value = 0

def getOr(exp:SlangParser.Or_opContext):
    assert isinstance(exp, SlangParser.Or_opContext)
    return OrOp(getValue(exp.children[0]), getValue(exp.children[2]))
class OrOp(BoolExpression):
    def __init__(self, left, right):
        self.name = "OR"
        self.op = lambda a, b: int.__or__(a, b)
        self.opStr = "||"
        self.type = SlangParser.Or_opContext
        self.gba = "or"
        super().__init__(left, right)
        #print(f"OrOp Value: {self.value}")
        self.smartEval()
        #print(f"OrOp smart Value: {self.value}")
    def smartEval(self):
        if self.left.value!=None and self.right.value!=None:
            if self.left.value == self.right.value:
                self.value = self.left.value

def getXor(exp:SlangParser.Xor_opContext):
    assert isinstance(exp, SlangParser.Xor_opContext)
    return XorOp(getValue(exp.children[0]), getValue(exp.children[2]))
class XorOp(BoolExpression):
    def __init__(self, left, right):
        self.name = "XOR"
        self.op = lambda a, b: int.__xor__(a, b)
        self.opStr = "^"
        self.type = SlangParser.Xor_opContext
        self.gba = "xor"
        super().__init__(left, right)
        #print(f"XorOp Value: {self.value}")
        self.smartEval()
        #print(f"XorOp smart Value: {self.value}")
    def smartEval(self):
        if self.left.value!=None and self.right.value!=None:
            if self.left.value==self.right.value:
                self.value = 0
        if isinstance(self.left, IDENT) and isinstance(self.right, IDENT):
            if self.left.name == self.right.name:
                self.value = 0

def getIdentList(identList:SlangParser.IdentListContext):
    children = identList.children[1:-1] #remove first and last element '(' and ')'
    return [getIDENT(c) for c in children]

def getFunctionDecl(decl:SlangParser.FunctionDeclContext):
    assert isinstance(decl, SlangParser.FunctionDeclContext)
    children = decl.children

    ident = getIDENT(children[1])
    identList = getIdentList(children[2])
    block = getClosedBlock(children[3])
    return FunctionDecl(ident, identList, block)
class FunctionDecl():
    def __init__(self, ident:IDENT, params:list, block:Block):
        self.name = ident.name
        self.params = params
        self.block = block
    def __repr__(self, indent=0):
        return f"{TAB*indent}FUNC[{self.name}]({', '.join([x.__repr__() for x in self.params])})({self.block.__repr__(indent=indent)})"

def getWhileLoop(loop:SlangParser.WhileLoopContext):
    assert isinstance(loop, SlangParser.WhileLoopContext)
    boolExp, block = None, None
    for el in loop.children:
        if isinstance(el, SlangParser.BoolExpressionContext):
            boolExp = getBoolExpression(el)
        elif isinstance(el, SlangParser.ClosedBlockContext):
            block = getClosedBlock(el)
        else:
            #print(f"ignored {type(el)} in while loop")
            pass
    if block is None:
        raise Exception(f"block in whileloop is None")
    return WhileLoop(boolExp, block)
class WhileLoop():
    def __init__(self, exp:BoolExpression, block:Block):
        self.exp = exp
        self.block = block
    def __repr__(self, indent=0):
        return f"{TAB*indent}WHILE ({self.exp}) {self.block.__repr__(indent=indent+1)}"
    
def getIfStatement(statement:SlangParser.IfStatementContext):
    assert isinstance(statement, SlangParser.IfStatementContext)
    boolExp, block = None, None
    for el in statement.children:
        if isinstance(el, SlangParser.BoolExpressionContext):
            boolExp = getBoolExpression(el)
        if isinstance(el, SlangParser.ClosedBlockContext):
            block = getClosedBlock(el)
    return IfStatement(boolExp, block)
class IfStatement():
    def __init__(self, exp:BoolExpression, block:Block):
        self.exp = exp
        self.block = block
    def __repr__(self, indent=0):
        return f"{TAB*indent}IF ({self.exp}) {self.block.__repr__(indent=indent)}"