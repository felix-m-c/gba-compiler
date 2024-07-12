# Generated from Slang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SlangParser import SlangParser
else:
    from SlangParser import SlangParser

# This class defines a complete listener for a parse tree produced by SlangParser.
class SlangListener(ParseTreeListener):

    # Enter a parse tree produced by SlangParser#prog.
    def enterProg(self, ctx:SlangParser.ProgContext):
        pass

    # Exit a parse tree produced by SlangParser#prog.
    def exitProg(self, ctx:SlangParser.ProgContext):
        pass


    # Enter a parse tree produced by SlangParser#closedBlock.
    def enterClosedBlock(self, ctx:SlangParser.ClosedBlockContext):
        pass

    # Exit a parse tree produced by SlangParser#closedBlock.
    def exitClosedBlock(self, ctx:SlangParser.ClosedBlockContext):
        pass


    # Enter a parse tree produced by SlangParser#block.
    def enterBlock(self, ctx:SlangParser.BlockContext):
        pass

    # Exit a parse tree produced by SlangParser#block.
    def exitBlock(self, ctx:SlangParser.BlockContext):
        pass


    # Enter a parse tree produced by SlangParser#functionDecl.
    def enterFunctionDecl(self, ctx:SlangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by SlangParser#functionDecl.
    def exitFunctionDecl(self, ctx:SlangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by SlangParser#identList.
    def enterIdentList(self, ctx:SlangParser.IdentListContext):
        pass

    # Exit a parse tree produced by SlangParser#identList.
    def exitIdentList(self, ctx:SlangParser.IdentListContext):
        pass


    # Enter a parse tree produced by SlangParser#line.
    def enterLine(self, ctx:SlangParser.LineContext):
        pass

    # Exit a parse tree produced by SlangParser#line.
    def exitLine(self, ctx:SlangParser.LineContext):
        pass


    # Enter a parse tree produced by SlangParser#whileLoop.
    def enterWhileLoop(self, ctx:SlangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by SlangParser#whileLoop.
    def exitWhileLoop(self, ctx:SlangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by SlangParser#ifStatement.
    def enterIfStatement(self, ctx:SlangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SlangParser#ifStatement.
    def exitIfStatement(self, ctx:SlangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SlangParser#elseStatement.
    def enterElseStatement(self, ctx:SlangParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by SlangParser#elseStatement.
    def exitElseStatement(self, ctx:SlangParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by SlangParser#returnStatement.
    def enterReturnStatement(self, ctx:SlangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SlangParser#returnStatement.
    def exitReturnStatement(self, ctx:SlangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SlangParser#assignment.
    def enterAssignment(self, ctx:SlangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SlangParser#assignment.
    def exitAssignment(self, ctx:SlangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SlangParser#expression.
    def enterExpression(self, ctx:SlangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SlangParser#expression.
    def exitExpression(self, ctx:SlangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SlangParser#boolExpression.
    def enterBoolExpression(self, ctx:SlangParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by SlangParser#boolExpression.
    def exitBoolExpression(self, ctx:SlangParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by SlangParser#arithmeticExpression.
    def enterArithmeticExpression(self, ctx:SlangParser.ArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by SlangParser#arithmeticExpression.
    def exitArithmeticExpression(self, ctx:SlangParser.ArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by SlangParser#brackets.
    def enterBrackets(self, ctx:SlangParser.BracketsContext):
        pass

    # Exit a parse tree produced by SlangParser#brackets.
    def exitBrackets(self, ctx:SlangParser.BracketsContext):
        pass


    # Enter a parse tree produced by SlangParser#equals_op.
    def enterEquals_op(self, ctx:SlangParser.Equals_opContext):
        pass

    # Exit a parse tree produced by SlangParser#equals_op.
    def exitEquals_op(self, ctx:SlangParser.Equals_opContext):
        pass


    # Enter a parse tree produced by SlangParser#notEquals_op.
    def enterNotEquals_op(self, ctx:SlangParser.NotEquals_opContext):
        pass

    # Exit a parse tree produced by SlangParser#notEquals_op.
    def exitNotEquals_op(self, ctx:SlangParser.NotEquals_opContext):
        pass


    # Enter a parse tree produced by SlangParser#and_op.
    def enterAnd_op(self, ctx:SlangParser.And_opContext):
        pass

    # Exit a parse tree produced by SlangParser#and_op.
    def exitAnd_op(self, ctx:SlangParser.And_opContext):
        pass


    # Enter a parse tree produced by SlangParser#xor_op.
    def enterXor_op(self, ctx:SlangParser.Xor_opContext):
        pass

    # Exit a parse tree produced by SlangParser#xor_op.
    def exitXor_op(self, ctx:SlangParser.Xor_opContext):
        pass


    # Enter a parse tree produced by SlangParser#or_op.
    def enterOr_op(self, ctx:SlangParser.Or_opContext):
        pass

    # Exit a parse tree produced by SlangParser#or_op.
    def exitOr_op(self, ctx:SlangParser.Or_opContext):
        pass


    # Enter a parse tree produced by SlangParser#addition.
    def enterAddition(self, ctx:SlangParser.AdditionContext):
        pass

    # Exit a parse tree produced by SlangParser#addition.
    def exitAddition(self, ctx:SlangParser.AdditionContext):
        pass


    # Enter a parse tree produced by SlangParser#subtraction.
    def enterSubtraction(self, ctx:SlangParser.SubtractionContext):
        pass

    # Exit a parse tree produced by SlangParser#subtraction.
    def exitSubtraction(self, ctx:SlangParser.SubtractionContext):
        pass


    # Enter a parse tree produced by SlangParser#multiplication.
    def enterMultiplication(self, ctx:SlangParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by SlangParser#multiplication.
    def exitMultiplication(self, ctx:SlangParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by SlangParser#division.
    def enterDivision(self, ctx:SlangParser.DivisionContext):
        pass

    # Exit a parse tree produced by SlangParser#division.
    def exitDivision(self, ctx:SlangParser.DivisionContext):
        pass


    # Enter a parse tree produced by SlangParser#value.
    def enterValue(self, ctx:SlangParser.ValueContext):
        pass

    # Exit a parse tree produced by SlangParser#value.
    def exitValue(self, ctx:SlangParser.ValueContext):
        pass


    # Enter a parse tree produced by SlangParser#functionCall.
    def enterFunctionCall(self, ctx:SlangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SlangParser#functionCall.
    def exitFunctionCall(self, ctx:SlangParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SlangParser#byteArray.
    def enterByteArray(self, ctx:SlangParser.ByteArrayContext):
        pass

    # Exit a parse tree produced by SlangParser#byteArray.
    def exitByteArray(self, ctx:SlangParser.ByteArrayContext):
        pass


    # Enter a parse tree produced by SlangParser#byteList.
    def enterByteList(self, ctx:SlangParser.ByteListContext):
        pass

    # Exit a parse tree produced by SlangParser#byteList.
    def exitByteList(self, ctx:SlangParser.ByteListContext):
        pass


    # Enter a parse tree produced by SlangParser#s_int.
    def enterS_int(self, ctx:SlangParser.S_intContext):
        pass

    # Exit a parse tree produced by SlangParser#s_int.
    def exitS_int(self, ctx:SlangParser.S_intContext):
        pass


    # Enter a parse tree produced by SlangParser#s_bool.
    def enterS_bool(self, ctx:SlangParser.S_boolContext):
        pass

    # Exit a parse tree produced by SlangParser#s_bool.
    def exitS_bool(self, ctx:SlangParser.S_boolContext):
        pass


    # Enter a parse tree produced by SlangParser#ident.
    def enterIdent(self, ctx:SlangParser.IdentContext):
        pass

    # Exit a parse tree produced by SlangParser#ident.
    def exitIdent(self, ctx:SlangParser.IdentContext):
        pass


    # Enter a parse tree produced by SlangParser#comment.
    def enterComment(self, ctx:SlangParser.CommentContext):
        pass

    # Exit a parse tree produced by SlangParser#comment.
    def exitComment(self, ctx:SlangParser.CommentContext):
        pass


    # Enter a parse tree produced by SlangParser#newline.
    def enterNewline(self, ctx:SlangParser.NewlineContext):
        pass

    # Exit a parse tree produced by SlangParser#newline.
    def exitNewline(self, ctx:SlangParser.NewlineContext):
        pass


    # Enter a parse tree produced by SlangParser#ws.
    def enterWs(self, ctx:SlangParser.WsContext):
        pass

    # Exit a parse tree produced by SlangParser#ws.
    def exitWs(self, ctx:SlangParser.WsContext):
        pass



del SlangParser