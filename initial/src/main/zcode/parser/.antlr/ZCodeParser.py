# Generated from c://Users//takho//Desktop//principles_of_programming_languages//initial//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
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
        4,1,20,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,5,0,0,
        1,3,1,1,0,0,0,0
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'string'", "'...'", "'bool'", 
                     "<INVALID>", "'number'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<-'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "STRING_TYPE", "STRING_OPERATOR", 
                      "BOOLEAN_TYPE", "LOGIC_OPERATOR", "NUMERIC_TYPE", 
                      "ARITHMETIC_OPERATORS", "KEYWORD", "CHARSET", "RELATIONAL_OPERATOR", 
                      "ASSIGN_OPERATOR", "SEPARATOR", "BOOLEAN", "NUMBER", 
                      "STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "IDENTIFIER", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMENT=1
    STRING_TYPE=2
    STRING_OPERATOR=3
    BOOLEAN_TYPE=4
    LOGIC_OPERATOR=5
    NUMERIC_TYPE=6
    ARITHMETIC_OPERATORS=7
    KEYWORD=8
    CHARSET=9
    RELATIONAL_OPERATOR=10
    ASSIGN_OPERATOR=11
    SEPARATOR=12
    BOOLEAN=13
    NUMBER=14
    STRING=15
    UNCLOSE_STRING=16
    ILLEGAL_ESCAPE=17
    IDENTIFIER=18
    WS=19
    ERROR_CHAR=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





