# Generated from /home/felix/Documents/sync/Uni/SS24/COMP/gba/main/Compiler/Slang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\6\n/\n\n\r\n\16\n\60\3\13\6\13\64")
        buf.write("\n\13\r\13\16\13\65\3\13\5\139\n\13\3\f\3\f\6\f=\n\f\r")
        buf.write("\f\16\f>\3\r\6\rB\n\r\r\r\16\rC\3\16\6\16G\n\16\r\16\16")
        buf.write("\16H\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\3\2\6\3\2\62;\4\2C\\c|")
        buf.write("\13\2\"\"$%\'(*-//\61;??C\\c|\4\2\f\f\17\17\2Q\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35")
        buf.write("\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2")
        buf.write("\2\r\'\3\2\2\2\17)\3\2\2\2\21+\3\2\2\2\23.\3\2\2\2\25")
        buf.write("8\3\2\2\2\27:\3\2\2\2\31A\3\2\2\2\33F\3\2\2\2\35\36\7")
        buf.write("?\2\2\36\4\3\2\2\2\37 \7*\2\2 \6\3\2\2\2!\"\7+\2\2\"\b")
        buf.write("\3\2\2\2#$\7-\2\2$\n\3\2\2\2%&\7/\2\2&\f\3\2\2\2\'(\7")
        buf.write(",\2\2(\16\3\2\2\2)*\7\61\2\2*\20\3\2\2\2+,\7.\2\2,\22")
        buf.write("\3\2\2\2-/\t\2\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\24\3\2\2\2\62\64\t\3\2\2\63\62\3\2\2\2")
        buf.write("\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\669\3\2\2\2")
        buf.write("\679\7a\2\28\63\3\2\2\28\67\3\2\2\29\26\3\2\2\2:<\7%\2")
        buf.write("\2;=\t\4\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?")
        buf.write("\30\3\2\2\2@B\t\5\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD")
        buf.write("\3\2\2\2D\32\3\2\2\2EG\7\"\2\2FE\3\2\2\2GH\3\2\2\2HF\3")
        buf.write("\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\16\2\2K\34\3\2\2\2\t\2")
        buf.write("\60\658>CH\3\3\16\2")
        return buf.getvalue()


class SlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    INT = 9
    IDENT = 10
    COMM = 11
    NEWLINE = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INT", "IDENT", "COMM", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INT", "IDENT", "COMM", "NEWLINE", "WS" ]

    grammarFileName = "Slang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.WS_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.skip();
     


