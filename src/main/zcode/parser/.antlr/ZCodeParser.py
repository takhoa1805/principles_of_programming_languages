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
        4,1,40,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,40,8,1,1,2,1,
        2,3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,87,8,3,1,4,1,
        4,1,4,1,4,3,4,93,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        105,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,5,5,127,8,5,10,5,12,5,130,9,5,1,6,1,6,1,
        7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,
        14,1,14,1,15,1,15,1,15,0,1,10,16,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,0,6,3,0,6,6,8,8,12,12,1,0,33,36,1,0,15,17,1,0,13,14,
        1,0,10,11,1,0,20,26,152,0,32,1,0,0,0,2,39,1,0,0,0,4,43,1,0,0,0,6,
        86,1,0,0,0,8,92,1,0,0,0,10,104,1,0,0,0,12,131,1,0,0,0,14,133,1,0,
        0,0,16,135,1,0,0,0,18,137,1,0,0,0,20,139,1,0,0,0,22,141,1,0,0,0,
        24,143,1,0,0,0,26,145,1,0,0,0,28,147,1,0,0,0,30,149,1,0,0,0,32,33,
        3,2,1,0,33,34,5,0,0,1,34,1,1,0,0,0,35,36,3,4,2,0,36,37,3,2,1,0,37,
        40,1,0,0,0,38,40,3,4,2,0,39,35,1,0,0,0,39,38,1,0,0,0,40,3,1,0,0,
        0,41,44,3,6,3,0,42,44,3,16,8,0,43,41,1,0,0,0,43,42,1,0,0,0,44,5,
        1,0,0,0,45,46,3,18,9,0,46,47,5,35,0,0,47,48,5,19,0,0,48,87,1,0,0,
        0,49,50,5,3,0,0,50,51,5,35,0,0,51,87,5,19,0,0,52,53,5,4,0,0,53,54,
        5,35,0,0,54,55,5,27,0,0,55,56,3,10,5,0,56,57,5,19,0,0,57,87,1,0,
        0,0,58,59,3,18,9,0,59,60,5,35,0,0,60,61,5,27,0,0,61,62,3,10,5,0,
        62,63,5,19,0,0,63,87,1,0,0,0,64,65,5,3,0,0,65,66,5,35,0,0,66,67,
        5,27,0,0,67,68,3,10,5,0,68,69,5,19,0,0,69,87,1,0,0,0,70,71,3,18,
        9,0,71,72,5,35,0,0,72,73,5,30,0,0,73,74,3,8,4,0,74,75,5,31,0,0,75,
        76,5,19,0,0,76,87,1,0,0,0,77,78,3,18,9,0,78,79,5,35,0,0,79,80,5,
        30,0,0,80,81,3,8,4,0,81,82,5,31,0,0,82,83,5,27,0,0,83,84,3,14,7,
        0,84,85,5,19,0,0,85,87,1,0,0,0,86,45,1,0,0,0,86,49,1,0,0,0,86,52,
        1,0,0,0,86,58,1,0,0,0,86,64,1,0,0,0,86,70,1,0,0,0,86,77,1,0,0,0,
        87,7,1,0,0,0,88,89,5,34,0,0,89,90,5,32,0,0,90,93,3,8,4,0,91,93,5,
        34,0,0,92,88,1,0,0,0,92,91,1,0,0,0,93,9,1,0,0,0,94,95,6,5,-1,0,95,
        96,5,28,0,0,96,97,3,10,5,0,97,98,5,29,0,0,98,105,1,0,0,0,99,100,
        5,14,0,0,100,105,3,10,5,8,101,102,5,9,0,0,102,105,3,10,5,7,103,105,
        3,20,10,0,104,94,1,0,0,0,104,99,1,0,0,0,104,101,1,0,0,0,104,103,
        1,0,0,0,105,128,1,0,0,0,106,107,10,6,0,0,107,108,3,22,11,0,108,109,
        3,10,5,7,109,127,1,0,0,0,110,111,10,5,0,0,111,112,3,24,12,0,112,
        113,3,10,5,6,113,127,1,0,0,0,114,115,10,4,0,0,115,116,3,26,13,0,
        116,117,3,10,5,5,117,127,1,0,0,0,118,119,10,3,0,0,119,120,3,28,14,
        0,120,121,3,10,5,4,121,127,1,0,0,0,122,123,10,2,0,0,123,124,3,30,
        15,0,124,125,3,10,5,3,125,127,1,0,0,0,126,106,1,0,0,0,126,110,1,
        0,0,0,126,114,1,0,0,0,126,118,1,0,0,0,126,122,1,0,0,0,127,130,1,
        0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,11,1,0,0,0,130,128,1,0,
        0,0,131,132,5,1,0,0,132,13,1,0,0,0,133,134,5,2,0,0,134,15,1,0,0,
        0,135,136,5,19,0,0,136,17,1,0,0,0,137,138,7,0,0,0,138,19,1,0,0,0,
        139,140,7,1,0,0,140,21,1,0,0,0,141,142,7,2,0,0,142,23,1,0,0,0,143,
        144,7,3,0,0,144,25,1,0,0,0,145,146,7,4,0,0,146,27,1,0,0,0,147,148,
        7,5,0,0,148,29,1,0,0,0,149,150,5,7,0,0,150,31,1,0,0,0,7,39,43,86,
        92,104,126,128
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'operand'", "'arrayexpression'", "'dynamic'", 
                     "'var'", "<INVALID>", "'string'", "'...'", "'bool'", 
                     "'not'", "'and'", "'or'", "'number'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", "'='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", "'<-'", 
                     "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DYNAMIC_TYPE", 
                      "VAR_TYPE", "COMMENT", "STRING_TYPE", "STRING_OPERATOR", 
                      "BOOL_TYPE", "NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", 
                      "NUMBER_TYPE", "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", 
                      "DIV_OPERATOR", "MOD_OPERATOR", "KEYWORD", "NEWLINE", 
                      "EQ_OPERATOR", "NEQ_OPERATOR", "LT_OPERATOR", "GT_OPERATOR", 
                      "LEQ_OPERATOR", "GEQ_OPERATOR", "SEQ_OPERATOR", "ASSIGN_OPERATOR", 
                      "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", 
                      "CLOSE_BRACKET", "COMMA", "BOOLEAN", "NUMBER", "IDENTIFIER", 
                      "STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_arrlist = 4
    RULE_expression = 5
    RULE_operand = 6
    RULE_arrexpression = 7
    RULE_funcdecl = 8
    RULE_typ = 9
    RULE_literal = 10
    RULE_mul_operators = 11
    RULE_add_operators = 12
    RULE_logic_operators = 13
    RULE_rel_operators = 14
    RULE_str_operators = 15

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "arrlist", 
                   "expression", "operand", "arrexpression", "funcdecl", 
                   "typ", "literal", "mul_operators", "add_operators", "logic_operators", 
                   "rel_operators", "str_operators" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DYNAMIC_TYPE=3
    VAR_TYPE=4
    COMMENT=5
    STRING_TYPE=6
    STRING_OPERATOR=7
    BOOL_TYPE=8
    NOT_OPERATOR=9
    AND_OPERATOR=10
    OR_OPERATOR=11
    NUMBER_TYPE=12
    ADD_OPERATOR=13
    SUB_OPERATOR=14
    MUL_OPERATOR=15
    DIV_OPERATOR=16
    MOD_OPERATOR=17
    KEYWORD=18
    NEWLINE=19
    EQ_OPERATOR=20
    NEQ_OPERATOR=21
    LT_OPERATOR=22
    GT_OPERATOR=23
    LEQ_OPERATOR=24
    GEQ_OPERATOR=25
    SEQ_OPERATOR=26
    ASSIGN_OPERATOR=27
    OPEN_PARENTHESIS=28
    CLOSE_PARENTHESIS=29
    OPEN_BRACKET=30
    CLOSE_BRACKET=31
    COMMA=32
    BOOLEAN=33
    NUMBER=34
    IDENTIFIER=35
    STRING=36
    UNCLOSE_STRING=37
    ILLEGAL_ESCAPE=38
    WS=39
    ERROR_CHAR=40

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
            self.state = 32
            self.decllist()
            self.state = 33
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
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.decl()
                self.state = 36
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
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
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 6, 8, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.vardecl()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
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
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.typ()
                self.state = 46
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 47
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 50
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 51
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(ZCodeParser.VAR_TYPE)
                self.state = 53
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 54
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 55
                self.expression(0)
                self.state = 56
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.typ()
                self.state = 59
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 60
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 61
                self.expression(0)
                self.state = 62
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 65
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 66
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 67
                self.expression(0)
                self.state = 68
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.typ()
                self.state = 71
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 72
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 73
                self.arrlist()
                self.state = 74
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 75
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.typ()
                self.state = 78
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 79
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 80
                self.arrlist()
                self.state = 81
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 82
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 83
                self.arrexpression()
                self.state = 84
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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(ZCodeParser.NUMBER)
                self.state = 89
                self.match(ZCodeParser.COMMA)
                self.state = 90
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(ZCodeParser.NUMBER)
                pass


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

        def OPEN_PARENTHESIS(self):
            return self.getToken(ZCodeParser.OPEN_PARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSE_PARENTHESIS, 0)

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def NOT_OPERATOR(self):
            return self.getToken(ZCodeParser.NOT_OPERATOR, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def mul_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_operatorsContext,0)


        def add_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Add_operatorsContext,0)


        def logic_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_operatorsContext,0)


        def rel_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Rel_operatorsContext,0)


        def str_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Str_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 95
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 96
                self.expression(0)
                self.state = 97
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass
            elif token in [14]:
                self.state = 99
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 100
                self.expression(8)
                pass
            elif token in [9]:
                self.state = 101
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 102
                self.expression(7)
                pass
            elif token in [33, 34, 35, 36]:
                self.state = 103
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 126
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 106
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 107
                        self.mul_operators()
                        self.state = 108
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 110
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 111
                        self.add_operators()
                        self.state = 112
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 114
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 115
                        self.logic_operators()
                        self.state = 116
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 119
                        self.rel_operators()
                        self.state = 120
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 122
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 123
                        self.str_operators()
                        self.state = 124
                        self.expression(3)
                        pass

             
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ZCodeParser.T__0)
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
        self.enterRule(localctx, 14, self.RULE_arrexpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
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
        self.enterRule(localctx, 16, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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
        self.enterRule(localctx, 18, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4416) != 0)):
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(ZCodeParser.BOOLEAN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
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


    class Mul_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL_OPERATOR(self):
            return self.getToken(ZCodeParser.MUL_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(ZCodeParser.DIV_OPERATOR, 0)

        def MOD_OPERATOR(self):
            return self.getToken(ZCodeParser.MOD_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_mul_operators




    def mul_operators(self):

        localctx = ZCodeParser.Mul_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mul_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
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


    class Add_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_OPERATOR(self):
            return self.getToken(ZCodeParser.ADD_OPERATOR, 0)

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_add_operators




    def add_operators(self):

        localctx = ZCodeParser.Add_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_add_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
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


    class Logic_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_OPERATOR(self):
            return self.getToken(ZCodeParser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(ZCodeParser.OR_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logic_operators




    def logic_operators(self):

        localctx = ZCodeParser.Logic_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
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


    class Rel_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_OPERATOR(self):
            return self.getToken(ZCodeParser.EQ_OPERATOR, 0)

        def SEQ_OPERATOR(self):
            return self.getToken(ZCodeParser.SEQ_OPERATOR, 0)

        def NEQ_OPERATOR(self):
            return self.getToken(ZCodeParser.NEQ_OPERATOR, 0)

        def LT_OPERATOR(self):
            return self.getToken(ZCodeParser.LT_OPERATOR, 0)

        def GT_OPERATOR(self):
            return self.getToken(ZCodeParser.GT_OPERATOR, 0)

        def LEQ_OPERATOR(self):
            return self.getToken(ZCodeParser.LEQ_OPERATOR, 0)

        def GEQ_OPERATOR(self):
            return self.getToken(ZCodeParser.GEQ_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_rel_operators




    def rel_operators(self):

        localctx = ZCodeParser.Rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_rel_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133169152) != 0)):
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


    class Str_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_OPERATOR(self):
            return self.getToken(ZCodeParser.STRING_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_str_operators




    def str_operators(self):

        localctx = ZCodeParser.Str_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_str_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ZCodeParser.STRING_OPERATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




