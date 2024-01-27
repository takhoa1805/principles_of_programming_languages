# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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





