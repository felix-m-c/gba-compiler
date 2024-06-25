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


    # Visit a parse tree produced by SlangParser#line.
    def visitLine(self, ctx:SlangParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#assignment.
    def visitAssignment(self, ctx:SlangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#expression.
    def visitExpression(self, ctx:SlangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SlangParser#brackets.
    def visitBrackets(self, ctx:SlangParser.BracketsContext):
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



del SlangParser