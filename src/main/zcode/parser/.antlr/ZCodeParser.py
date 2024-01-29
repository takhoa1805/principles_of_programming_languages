# Generated from c://Users//takho//Desktop//principles_of_programming_languages//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
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
        4,1,28,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,26,8,1,1,2,1,2,
        3,2,30,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,73,8,3,1,4,1,4,
        1,4,1,4,3,4,79,8,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,
        4,6,8,10,12,14,16,0,1,3,0,6,6,8,8,10,10,88,0,18,1,0,0,0,2,25,1,0,
        0,0,4,29,1,0,0,0,6,72,1,0,0,0,8,78,1,0,0,0,10,80,1,0,0,0,12,82,1,
        0,0,0,14,84,1,0,0,0,16,86,1,0,0,0,18,19,3,2,1,0,19,20,5,0,0,1,20,
        1,1,0,0,0,21,22,3,4,2,0,22,23,3,2,1,0,23,26,1,0,0,0,24,26,3,4,2,
        0,25,21,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,30,3,6,3,0,28,30,3,
        14,7,0,29,27,1,0,0,0,29,28,1,0,0,0,30,5,1,0,0,0,31,32,3,16,8,0,32,
        33,5,23,0,0,33,34,5,13,0,0,34,73,1,0,0,0,35,36,5,3,0,0,36,37,5,23,
        0,0,37,73,5,13,0,0,38,39,5,4,0,0,39,40,5,23,0,0,40,41,5,15,0,0,41,
        42,3,12,6,0,42,43,5,13,0,0,43,73,1,0,0,0,44,45,3,16,8,0,45,46,5,
        23,0,0,46,47,5,15,0,0,47,48,3,12,6,0,48,49,5,13,0,0,49,73,1,0,0,
        0,50,51,5,3,0,0,51,52,5,23,0,0,52,53,5,15,0,0,53,54,3,12,6,0,54,
        55,5,13,0,0,55,73,1,0,0,0,56,57,3,16,8,0,57,58,5,23,0,0,58,59,5,
        18,0,0,59,60,3,8,4,0,60,61,5,19,0,0,61,62,5,13,0,0,62,73,1,0,0,0,
        63,64,3,16,8,0,64,65,5,23,0,0,65,66,5,18,0,0,66,67,3,8,4,0,67,68,
        5,19,0,0,68,69,5,15,0,0,69,70,3,10,5,0,70,71,5,13,0,0,71,73,1,0,
        0,0,72,31,1,0,0,0,72,35,1,0,0,0,72,38,1,0,0,0,72,44,1,0,0,0,72,50,
        1,0,0,0,72,56,1,0,0,0,72,63,1,0,0,0,73,7,1,0,0,0,74,75,5,22,0,0,
        75,76,5,20,0,0,76,79,3,8,4,0,77,79,5,22,0,0,78,74,1,0,0,0,78,77,
        1,0,0,0,79,9,1,0,0,0,80,81,5,1,0,0,81,11,1,0,0,0,82,83,5,2,0,0,83,
        13,1,0,0,0,84,85,5,13,0,0,85,15,1,0,0,0,86,87,7,0,0,0,87,17,1,0,
        0,0,4,25,29,72,78
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'arrayexpression'", "'expression'", "'dynamic'", 
                     "'var'", "<INVALID>", "'string'", "'...'", "'bool'", 
                     "<INVALID>", "'number'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<-'", "'('", "')'", "'['", 
                     "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DYNAMIC_TYPE", 
                      "VAR_TYPE", "COMMENT", "STRING_TYPE", "STRING_OPERATOR", 
                      "BOOL_TYPE", "LOGIC_OPERATOR", "NUMBER_TYPE", "ARITHMETIC_OPERATORS", 
                      "KEYWORD", "NEWLINE", "RELATIONAL_OPERATOR", "ASSIGN_OPERATOR", 
                      "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", 
                      "CLOSE_BRACKET", "COMMA", "BOOLEAN", "NUMBER", "IDENTIFIER", 
                      "STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_arrlist = 4
    RULE_arrexpression = 5
    RULE_expression = 6
    RULE_funcdecl = 7
    RULE_typ = 8

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "arrlist", 
                   "arrexpression", "expression", "funcdecl", "typ" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DYNAMIC_TYPE=3
    VAR_TYPE=4
    COMMENT=5
    STRING_TYPE=6
    STRING_OPERATOR=7
    BOOL_TYPE=8
    LOGIC_OPERATOR=9
    NUMBER_TYPE=10
    ARITHMETIC_OPERATORS=11
    KEYWORD=12
    NEWLINE=13
    RELATIONAL_OPERATOR=14
    ASSIGN_OPERATOR=15
    OPEN_PARENTHESIS=16
    CLOSE_PARENTHESIS=17
    OPEN_BRACKET=18
    CLOSE_BRACKET=19
    COMMA=20
    BOOLEAN=21
    NUMBER=22
    IDENTIFIER=23
    STRING=24
    UNCLOSE_STRING=25
    ILLEGAL_ESCAPE=26
    WS=27
    ERROR_CHAR=28

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

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.decllist()
            self.state = 19
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.decl()
                self.state = 22
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 6, 8, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.vardecl()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.funcdecl()
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def DYNAMIC_TYPE(self):
            return self.getToken(ZCodeParser.DYNAMIC_TYPE, 0)

        def VAR_TYPE(self):
            return self.getToken(ZCodeParser.VAR_TYPE, 0)

        def ASSIGN_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN_OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def arrexpression(self):
            return self.getTypedRuleContext(ZCodeParser.ArrexpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.typ()
                self.state = 32
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 33
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 36
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 37
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.match(ZCodeParser.VAR_TYPE)
                self.state = 39
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 40
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 41
                self.expression()
                self.state = 42
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.typ()
                self.state = 45
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 46
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 47
                self.expression()
                self.state = 48
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 51
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 52
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 53
                self.expression()
                self.state = 54
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.typ()
                self.state = 57
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 58
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 59
                self.arrlist()
                self.state = 60
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 61
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 63
                self.typ()
                self.state = 64
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 65
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 66
                self.arrlist()
                self.state = 67
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 68
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 69
                self.arrexpression()
                self.state = 70
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrlist




    def arrlist(self):

        localctx = ZCodeParser.ArrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrlist)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(ZCodeParser.NUMBER)
                self.state = 75
                self.match(ZCodeParser.COMMA)
                self.state = 76
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrexpression




    def arrexpression(self):

        localctx = ZCodeParser.ArrexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ZCodeParser.T__0)
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ZCodeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_TYPE(self):
            return self.getToken(ZCodeParser.BOOL_TYPE, 0)

        def NUMBER_TYPE(self):
            return self.getToken(ZCodeParser.NUMBER_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(ZCodeParser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





