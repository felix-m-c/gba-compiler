"""
# Elements that are removed when building the AST
(prog) -> (context) -> Block
(brackets) -> Exp

Assignment(target:IDENT, value:Exp)
    # move value of Exp into target

Exp
    # Has a Value (possibly known at compiletime)
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
