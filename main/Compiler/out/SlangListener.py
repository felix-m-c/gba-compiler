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


    # Enter a parse tree produced by SlangParser#line.
    def enterLine(self, ctx:SlangParser.LineContext):
        pass

    # Exit a parse tree produced by SlangParser#line.
    def exitLine(self, ctx:SlangParser.LineContext):
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


    # Enter a parse tree produced by SlangParser#brackets.
    def enterBrackets(self, ctx:SlangParser.BracketsContext):
        pass

    # Exit a parse tree produced by SlangParser#brackets.
    def exitBrackets(self, ctx:SlangParser.BracketsContext):
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



del SlangParser