# Generated from Slang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,184,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,3,0,32,8,0,1,0,3,0,35,8,0,1,0,1,0,1,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,3,0,47,8,0,1,0,3,0,50,8,0,1,1,1,1,3,1,54,
        8,1,1,1,3,1,57,8,1,1,1,3,1,60,8,1,1,2,1,2,3,2,64,8,2,1,2,1,2,3,2,
        68,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,79,8,3,1,4,1,4,3,
        4,83,8,4,1,4,1,4,3,4,87,8,4,1,4,1,4,1,5,1,5,3,5,93,8,5,1,5,1,5,3,
        5,97,8,5,1,5,1,5,1,6,1,6,3,6,103,8,6,1,6,1,6,3,6,107,8,6,1,6,1,6,
        1,7,1,7,3,7,113,8,7,1,7,1,7,3,7,117,8,7,1,7,1,7,1,8,1,8,3,8,123,
        8,8,1,8,1,8,3,8,127,8,8,1,8,1,8,1,9,1,9,1,9,3,9,134,8,9,1,10,1,10,
        3,10,138,8,10,1,10,1,10,3,10,142,8,10,1,10,1,10,1,10,3,10,147,8,
        10,5,10,149,8,10,10,10,12,10,152,9,10,1,10,1,10,3,10,156,8,10,1,
        10,1,10,1,10,1,10,3,10,162,8,10,1,10,1,10,3,10,166,8,10,1,10,1,10,
        1,10,3,10,171,8,10,5,10,173,8,10,10,10,12,10,176,9,10,1,10,3,10,
        179,8,10,1,10,3,10,182,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,
        20,0,0,212,0,49,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,0,6,78,1,0,0,0,8,
        80,1,0,0,0,10,90,1,0,0,0,12,100,1,0,0,0,14,110,1,0,0,0,16,120,1,
        0,0,0,18,133,1,0,0,0,20,181,1,0,0,0,22,23,3,2,1,0,23,24,5,12,0,0,
        24,26,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,
        0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,31,
        32,1,0,0,0,32,34,1,0,0,0,33,35,5,12,0,0,34,33,1,0,0,0,34,35,1,0,
        0,0,35,36,1,0,0,0,36,50,5,0,0,1,37,38,3,2,1,0,38,39,5,12,0,0,39,
        41,1,0,0,0,40,37,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,
        0,43,46,1,0,0,0,44,42,1,0,0,0,45,47,5,12,0,0,46,45,1,0,0,0,46,47,
        1,0,0,0,47,48,1,0,0,0,48,50,5,0,0,1,49,27,1,0,0,0,49,42,1,0,0,0,
        50,1,1,0,0,0,51,53,3,4,2,0,52,54,5,13,0,0,53,52,1,0,0,0,53,54,1,
        0,0,0,54,56,1,0,0,0,55,57,5,11,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,
        60,1,0,0,0,58,60,5,11,0,0,59,51,1,0,0,0,59,58,1,0,0,0,60,3,1,0,0,
        0,61,63,5,10,0,0,62,64,5,13,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,65,
        1,0,0,0,65,67,5,1,0,0,66,68,5,13,0,0,67,66,1,0,0,0,67,68,1,0,0,0,
        68,69,1,0,0,0,69,70,3,6,3,0,70,5,1,0,0,0,71,79,1,0,0,0,72,79,3,10,
        5,0,73,79,3,12,6,0,74,79,3,14,7,0,75,79,3,16,8,0,76,79,3,18,9,0,
        77,79,3,20,10,0,78,71,1,0,0,0,78,72,1,0,0,0,78,73,1,0,0,0,78,74,
        1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,7,1,0,0,0,80,
        82,5,2,0,0,81,83,5,13,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,84,1,0,
        0,0,84,86,3,6,3,0,85,87,5,13,0,0,86,85,1,0,0,0,86,87,1,0,0,0,87,
        88,1,0,0,0,88,89,5,3,0,0,89,9,1,0,0,0,90,92,3,18,9,0,91,93,5,13,
        0,0,92,91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,96,5,4,0,0,95,97,
        5,13,0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,3,18,9,
        0,99,11,1,0,0,0,100,102,3,18,9,0,101,103,5,13,0,0,102,101,1,0,0,
        0,102,103,1,0,0,0,103,104,1,0,0,0,104,106,5,5,0,0,105,107,5,13,0,
        0,106,105,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,3,18,9,
        0,109,13,1,0,0,0,110,112,3,18,9,0,111,113,5,13,0,0,112,111,1,0,0,
        0,112,113,1,0,0,0,113,114,1,0,0,0,114,116,5,6,0,0,115,117,5,13,0,
        0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,3,18,9,
        0,119,15,1,0,0,0,120,122,3,18,9,0,121,123,5,13,0,0,122,121,1,0,0,
        0,122,123,1,0,0,0,123,124,1,0,0,0,124,126,5,7,0,0,125,127,5,13,0,
        0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,3,18,9,
        0,129,17,1,0,0,0,130,134,5,10,0,0,131,134,5,9,0,0,132,134,3,8,4,
        0,133,130,1,0,0,0,133,131,1,0,0,0,133,132,1,0,0,0,134,19,1,0,0,0,
        135,137,5,10,0,0,136,138,5,13,0,0,137,136,1,0,0,0,137,138,1,0,0,
        0,138,139,1,0,0,0,139,141,5,2,0,0,140,142,5,13,0,0,141,140,1,0,0,
        0,141,142,1,0,0,0,142,150,1,0,0,0,143,144,3,18,9,0,144,146,5,8,0,
        0,145,147,5,13,0,0,146,145,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,
        0,148,143,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,
        0,151,153,1,0,0,0,152,150,1,0,0,0,153,155,3,18,9,0,154,156,5,13,
        0,0,155,154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,158,5,3,
        0,0,158,182,1,0,0,0,159,161,5,10,0,0,160,162,5,13,0,0,161,160,1,
        0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,165,5,2,0,0,164,166,5,
        13,0,0,165,164,1,0,0,0,165,166,1,0,0,0,166,174,1,0,0,0,167,168,3,
        18,9,0,168,170,5,8,0,0,169,171,5,13,0,0,170,169,1,0,0,0,170,171,
        1,0,0,0,171,173,1,0,0,0,172,167,1,0,0,0,173,176,1,0,0,0,174,172,
        1,0,0,0,174,175,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,177,179,
        5,13,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,182,
        5,3,0,0,181,135,1,0,0,0,181,159,1,0,0,0,182,21,1,0,0,0,34,27,31,
        34,42,46,49,53,56,59,63,67,78,82,86,92,96,102,106,112,116,122,126,
        133,137,141,146,150,155,161,165,170,174,178,181
    ]

class SlangParser ( Parser ):

    grammarFileName = "Slang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'+'", "'-'", "'*'", 
                     "'/'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "IDENT", "COMM", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_brackets = 4
    RULE_addition = 5
    RULE_subtraction = 6
    RULE_multiplication = 7
    RULE_division = 8
    RULE_value = 9
    RULE_functionCall = 10

    ruleNames =  [ "prog", "line", "assignment", "expression", "brackets", 
                   "addition", "subtraction", "multiplication", "division", 
                   "value", "functionCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INT=9
    IDENT=10
    COMM=11
    NEWLINE=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SlangParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlangParser.LineContext)
            else:
                return self.getTypedRuleContext(SlangParser.LineContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.NEWLINE)
            else:
                return self.getToken(SlangParser.NEWLINE, i)

        def getRuleIndex(self):
            return SlangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SlangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 22
                        self.line()
                        self.state = 23
                        self.match(SlangParser.NEWLINE) 
                    self.state = 29
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10 or _la==11:
                    self.state = 30
                    self.line()


                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 33
                    self.match(SlangParser.NEWLINE)


                self.state = 36
                self.match(SlangParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10 or _la==11:
                    self.state = 37
                    self.line()
                    self.state = 38
                    self.match(SlangParser.NEWLINE)
                    self.state = 44
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 45
                    self.match(SlangParser.NEWLINE)


                self.state = 48
                self.match(SlangParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(SlangParser.AssignmentContext,0)


        def WS(self):
            return self.getToken(SlangParser.WS, 0)

        def COMM(self):
            return self.getToken(SlangParser.COMM, 0)

        def getRuleIndex(self):
            return SlangParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = SlangParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.assignment()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 52
                    self.match(SlangParser.WS)


                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 55
                    self.match(SlangParser.COMM)


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(SlangParser.COMM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SlangParser.IDENT, 0)

        def expression(self):
            return self.getTypedRuleContext(SlangParser.ExpressionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.WS)
            else:
                return self.getToken(SlangParser.WS, i)

        def getRuleIndex(self):
            return SlangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SlangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(SlangParser.IDENT)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 62
                self.match(SlangParser.WS)


            self.state = 65
            self.match(SlangParser.T__0)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 66
                self.match(SlangParser.WS)


            self.state = 69
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addition(self):
            return self.getTypedRuleContext(SlangParser.AdditionContext,0)


        def subtraction(self):
            return self.getTypedRuleContext(SlangParser.SubtractionContext,0)


        def multiplication(self):
            return self.getTypedRuleContext(SlangParser.MultiplicationContext,0)


        def division(self):
            return self.getTypedRuleContext(SlangParser.DivisionContext,0)


        def value(self):
            return self.getTypedRuleContext(SlangParser.ValueContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SlangParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return SlangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SlangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.addition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.subtraction()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.multiplication()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.division()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.value()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BracketsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SlangParser.ExpressionContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.WS)
            else:
                return self.getToken(SlangParser.WS, i)

        def getRuleIndex(self):
            return SlangParser.RULE_brackets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrackets" ):
                return visitor.visitBrackets(self)
            else:
                return visitor.visitChildren(self)




    def brackets(self):

        localctx = SlangParser.BracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_brackets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SlangParser.T__1)
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 81
                self.match(SlangParser.WS)


            self.state = 84
            self.expression()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 85
                self.match(SlangParser.WS)


            self.state = 88
            self.match(SlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlangParser.ValueContext)
            else:
                return self.getTypedRuleContext(SlangParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.WS)
            else:
                return self.getToken(SlangParser.WS, i)

        def getRuleIndex(self):
            return SlangParser.RULE_addition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)




    def addition(self):

        localctx = SlangParser.AdditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_addition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.value()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 91
                self.match(SlangParser.WS)


            self.state = 94
            self.match(SlangParser.T__3)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 95
                self.match(SlangParser.WS)


            self.state = 98
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubtractionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlangParser.ValueContext)
            else:
                return self.getTypedRuleContext(SlangParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.WS)
            else:
                return self.getToken(SlangParser.WS, i)

        def getRuleIndex(self):
            return SlangParser.RULE_subtraction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtraction" ):
                listener.enterSubtraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtraction" ):
                listener.exitSubtraction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtraction" ):
                return visitor.visitSubtraction(self)
            else:
                return visitor.visitChildren(self)




    def subtraction(self):

        localctx = SlangParser.SubtractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subtraction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.value()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 101
                self.match(SlangParser.WS)


            self.state = 104
            self.match(SlangParser.T__4)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 105
                self.match(SlangParser.WS)


            self.state = 108
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlangParser.ValueContext)
            else:
                return self.getTypedRuleContext(SlangParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.WS)
            else:
                return self.getToken(SlangParser.WS, i)

        def getRuleIndex(self):
            return SlangParser.RULE_multiplication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplication" ):
                listener.enterMultiplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplication" ):
                listener.exitMultiplication(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)




    def multiplication(self):

        localctx = SlangParser.MultiplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_multiplication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.value()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 111
                self.match(SlangParser.WS)


            self.state = 114
            self.match(SlangParser.T__5)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 115
                self.match(SlangParser.WS)


            self.state = 118
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlangParser.ValueContext)
            else:
                return self.getTypedRuleContext(SlangParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.WS)
            else:
                return self.getToken(SlangParser.WS, i)

        def getRuleIndex(self):
            return SlangParser.RULE_division

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)




    def division(self):

        localctx = SlangParser.DivisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_division)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.value()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 121
                self.match(SlangParser.WS)


            self.state = 124
            self.match(SlangParser.T__6)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 125
                self.match(SlangParser.WS)


            self.state = 128
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SlangParser.IDENT, 0)

        def INT(self):
            return self.getToken(SlangParser.INT, 0)

        def brackets(self):
            return self.getTypedRuleContext(SlangParser.BracketsContext,0)


        def getRuleIndex(self):
            return SlangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = SlangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(SlangParser.IDENT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(SlangParser.INT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.brackets()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SlangParser.IDENT, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SlangParser.ValueContext)
            else:
                return self.getTypedRuleContext(SlangParser.ValueContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SlangParser.WS)
            else:
                return self.getToken(SlangParser.WS, i)

        def getRuleIndex(self):
            return SlangParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = SlangParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(SlangParser.IDENT)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 136
                    self.match(SlangParser.WS)


                self.state = 139
                self.match(SlangParser.T__1)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 140
                    self.match(SlangParser.WS)


                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 143
                        self.value()
                        self.state = 144
                        self.match(SlangParser.T__7)
                        self.state = 146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==13:
                            self.state = 145
                            self.match(SlangParser.WS)

                 
                    self.state = 152
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 153
                self.value()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 154
                    self.match(SlangParser.WS)


                self.state = 157
                self.match(SlangParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(SlangParser.IDENT)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 160
                    self.match(SlangParser.WS)


                self.state = 163
                self.match(SlangParser.T__1)
                self.state = 165
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 164
                    self.match(SlangParser.WS)


                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1540) != 0):
                    self.state = 167
                    self.value()
                    self.state = 168
                    self.match(SlangParser.T__7)
                    self.state = 170
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        self.state = 169
                        self.match(SlangParser.WS)


                    self.state = 176
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 177
                    self.match(SlangParser.WS)


                self.state = 180
                self.match(SlangParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





