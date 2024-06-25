# Generated from Slang.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,74,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,
        4,8,45,8,8,11,8,12,8,46,1,9,4,9,50,8,9,11,9,12,9,51,1,9,3,9,55,8,
        9,1,10,1,10,4,10,59,8,10,11,10,12,10,60,1,11,4,11,64,8,11,11,11,
        12,11,65,1,12,4,12,69,8,12,11,12,12,12,70,1,12,1,12,0,0,13,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,0,4,
        1,0,48,57,2,0,65,90,97,122,9,0,32,32,34,35,37,38,40,43,45,45,47,
        57,61,61,65,90,97,122,2,0,10,10,13,13,79,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,
        25,1,0,0,0,1,27,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,33,1,0,0,0,9,
        35,1,0,0,0,11,37,1,0,0,0,13,39,1,0,0,0,15,41,1,0,0,0,17,44,1,0,0,
        0,19,54,1,0,0,0,21,56,1,0,0,0,23,63,1,0,0,0,25,68,1,0,0,0,27,28,
        5,61,0,0,28,2,1,0,0,0,29,30,5,40,0,0,30,4,1,0,0,0,31,32,5,41,0,0,
        32,6,1,0,0,0,33,34,5,43,0,0,34,8,1,0,0,0,35,36,5,45,0,0,36,10,1,
        0,0,0,37,38,5,42,0,0,38,12,1,0,0,0,39,40,5,47,0,0,40,14,1,0,0,0,
        41,42,5,44,0,0,42,16,1,0,0,0,43,45,7,0,0,0,44,43,1,0,0,0,45,46,1,
        0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,18,1,0,0,0,48,50,7,1,0,0,49,
        48,1,0,0,0,50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,55,1,0,0,
        0,53,55,5,95,0,0,54,49,1,0,0,0,54,53,1,0,0,0,55,20,1,0,0,0,56,58,
        5,35,0,0,57,59,7,2,0,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,
        60,61,1,0,0,0,61,22,1,0,0,0,62,64,7,3,0,0,63,62,1,0,0,0,64,65,1,
        0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,24,1,0,0,0,67,69,5,32,0,0,68,
        67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,
        0,72,73,6,12,0,0,73,26,1,0,0,0,7,0,46,51,54,60,65,70,1,1,12,0
    ]

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
        self.checkVersion("4.13.1")
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
     


