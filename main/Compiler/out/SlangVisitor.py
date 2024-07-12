# Generated from Slang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SlangParser import SlangParser
else:
    from SlangParser import SlangParser

# This class defines a complete generic visitor for a parse tree produced by SlangParser.

class SlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SlangParser#prog.
    def visitProg(self, ctx:SlangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#closedBlock.
    def visitClosedBlock(self, ctx:SlangParser.ClosedBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#block.
    def visitBlock(self, ctx:SlangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#functionDecl.
    def visitFunctionDecl(self, ctx:SlangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#identList.
    def visitIdentList(self, ctx:SlangParser.IdentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#line.
    def visitLine(self, ctx:SlangParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#whileLoop.
    def visitWhileLoop(self, ctx:SlangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#ifStatement.
    def visitIfStatement(self, ctx:SlangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#elseStatement.
    def visitElseStatement(self, ctx:SlangParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#returnStatement.
    def visitReturnStatement(self, ctx:SlangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#assignment.
    def visitAssignment(self, ctx:SlangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#expression.
    def visitExpression(self, ctx:SlangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#boolExpression.
    def visitBoolExpression(self, ctx:SlangParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:SlangParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#brackets.
    def visitBrackets(self, ctx:SlangParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#equals_op.
    def visitEquals_op(self, ctx:SlangParser.Equals_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#notEquals_op.
    def visitNotEquals_op(self, ctx:SlangParser.NotEquals_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#and_op.
    def visitAnd_op(self, ctx:SlangParser.And_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#xor_op.
    def visitXor_op(self, ctx:SlangParser.Xor_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#or_op.
    def visitOr_op(self, ctx:SlangParser.Or_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#addition.
    def visitAddition(self, ctx:SlangParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#subtraction.
    def visitSubtraction(self, ctx:SlangParser.SubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#multiplication.
    def visitMultiplication(self, ctx:SlangParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#division.
    def visitDivision(self, ctx:SlangParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#value.
    def visitValue(self, ctx:SlangParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#functionCall.
    def visitFunctionCall(self, ctx:SlangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#byteArray.
    def visitByteArray(self, ctx:SlangParser.ByteArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#byteList.
    def visitByteList(self, ctx:SlangParser.ByteListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#s_int.
    def visitS_int(self, ctx:SlangParser.S_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#s_bool.
    def visitS_bool(self, ctx:SlangParser.S_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#ident.
    def visitIdent(self, ctx:SlangParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#comment.
    def visitComment(self, ctx:SlangParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#newline.
    def visitNewline(self, ctx:SlangParser.NewlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#ws.
    def visitWs(self, ctx:SlangParser.WsContext):
        return self.visitChildren(ctx)



del SlangParser