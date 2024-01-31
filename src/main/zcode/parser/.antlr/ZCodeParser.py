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
        4,1,38,237,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,56,8,1,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        3,3,103,8,3,1,4,1,4,1,4,1,4,3,4,109,8,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,122,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,5,5,149,8,5,10,5,12,5,152,9,5,1,6,1,6,3,6,156,8,6,1,7,1,7,3,
        7,160,8,7,1,8,1,8,1,8,1,8,1,8,3,8,167,8,8,1,9,1,9,1,9,1,9,1,9,1,
        10,1,10,3,10,176,8,10,1,11,1,11,1,11,1,11,1,11,3,11,183,8,11,1,12,
        1,12,1,13,1,13,1,13,1,13,3,13,191,8,13,1,14,1,14,1,14,1,14,3,14,
        197,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,219,8,15,1,16,
        1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,
        1,23,1,23,1,23,0,1,10,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,0,6,3,0,4,4,6,6,10,10,1,0,31,34,1,0,13,
        15,1,0,11,12,1,0,8,9,1,0,18,24,249,0,48,1,0,0,0,2,55,1,0,0,0,4,59,
        1,0,0,0,6,102,1,0,0,0,8,108,1,0,0,0,10,121,1,0,0,0,12,155,1,0,0,
        0,14,159,1,0,0,0,16,166,1,0,0,0,18,168,1,0,0,0,20,175,1,0,0,0,22,
        182,1,0,0,0,24,184,1,0,0,0,26,190,1,0,0,0,28,196,1,0,0,0,30,218,
        1,0,0,0,32,220,1,0,0,0,34,222,1,0,0,0,36,224,1,0,0,0,38,226,1,0,
        0,0,40,228,1,0,0,0,42,230,1,0,0,0,44,232,1,0,0,0,46,234,1,0,0,0,
        48,49,3,2,1,0,49,50,5,0,0,1,50,1,1,0,0,0,51,52,3,4,2,0,52,53,3,2,
        1,0,53,56,1,0,0,0,54,56,3,4,2,0,55,51,1,0,0,0,55,54,1,0,0,0,56,3,
        1,0,0,0,57,60,3,6,3,0,58,60,3,32,16,0,59,57,1,0,0,0,59,58,1,0,0,
        0,60,5,1,0,0,0,61,62,3,34,17,0,62,63,5,33,0,0,63,64,5,17,0,0,64,
        103,1,0,0,0,65,66,5,1,0,0,66,67,5,33,0,0,67,103,5,17,0,0,68,69,5,
        2,0,0,69,70,5,33,0,0,70,71,5,25,0,0,71,72,3,10,5,0,72,73,5,17,0,
        0,73,103,1,0,0,0,74,75,3,34,17,0,75,76,5,33,0,0,76,77,5,25,0,0,77,
        78,3,10,5,0,78,79,5,17,0,0,79,103,1,0,0,0,80,81,5,1,0,0,81,82,5,
        33,0,0,82,83,5,25,0,0,83,84,3,10,5,0,84,85,5,17,0,0,85,103,1,0,0,
        0,86,87,3,34,17,0,87,88,5,33,0,0,88,89,5,28,0,0,89,90,3,8,4,0,90,
        91,5,29,0,0,91,92,5,17,0,0,92,103,1,0,0,0,93,94,3,34,17,0,94,95,
        5,33,0,0,95,96,5,28,0,0,96,97,3,8,4,0,97,98,5,29,0,0,98,99,5,25,
        0,0,99,100,3,10,5,0,100,101,5,17,0,0,101,103,1,0,0,0,102,61,1,0,
        0,0,102,65,1,0,0,0,102,68,1,0,0,0,102,74,1,0,0,0,102,80,1,0,0,0,
        102,86,1,0,0,0,102,93,1,0,0,0,103,7,1,0,0,0,104,105,5,32,0,0,105,
        106,5,30,0,0,106,109,3,8,4,0,107,109,5,32,0,0,108,104,1,0,0,0,108,
        107,1,0,0,0,109,9,1,0,0,0,110,111,6,5,-1,0,111,112,5,26,0,0,112,
        113,3,10,5,0,113,114,5,27,0,0,114,122,1,0,0,0,115,116,5,12,0,0,116,
        122,3,10,5,9,117,118,5,7,0,0,118,122,3,10,5,8,119,122,3,18,9,0,120,
        122,3,36,18,0,121,110,1,0,0,0,121,115,1,0,0,0,121,117,1,0,0,0,121,
        119,1,0,0,0,121,120,1,0,0,0,122,150,1,0,0,0,123,124,10,7,0,0,124,
        125,3,38,19,0,125,126,3,10,5,8,126,149,1,0,0,0,127,128,10,6,0,0,
        128,129,3,40,20,0,129,130,3,10,5,7,130,149,1,0,0,0,131,132,10,5,
        0,0,132,133,3,42,21,0,133,134,3,10,5,6,134,149,1,0,0,0,135,136,10,
        4,0,0,136,137,3,44,22,0,137,138,3,10,5,5,138,149,1,0,0,0,139,140,
        10,3,0,0,140,141,3,46,23,0,141,142,3,10,5,4,142,149,1,0,0,0,143,
        144,10,11,0,0,144,145,5,28,0,0,145,146,3,16,8,0,146,147,5,29,0,0,
        147,149,1,0,0,0,148,123,1,0,0,0,148,127,1,0,0,0,148,131,1,0,0,0,
        148,135,1,0,0,0,148,139,1,0,0,0,148,143,1,0,0,0,149,152,1,0,0,0,
        150,148,1,0,0,0,150,151,1,0,0,0,151,11,1,0,0,0,152,150,1,0,0,0,153,
        156,3,36,18,0,154,156,5,12,0,0,155,153,1,0,0,0,155,154,1,0,0,0,156,
        13,1,0,0,0,157,160,3,36,18,0,158,160,5,7,0,0,159,157,1,0,0,0,159,
        158,1,0,0,0,160,15,1,0,0,0,161,167,3,10,5,0,162,163,3,10,5,0,163,
        164,5,30,0,0,164,165,3,16,8,0,165,167,1,0,0,0,166,161,1,0,0,0,166,
        162,1,0,0,0,167,17,1,0,0,0,168,169,5,33,0,0,169,170,5,26,0,0,170,
        171,3,20,10,0,171,172,5,27,0,0,172,19,1,0,0,0,173,176,3,22,11,0,
        174,176,1,0,0,0,175,173,1,0,0,0,175,174,1,0,0,0,176,21,1,0,0,0,177,
        178,3,24,12,0,178,179,5,30,0,0,179,180,3,22,11,0,180,183,1,0,0,0,
        181,183,3,24,12,0,182,177,1,0,0,0,182,181,1,0,0,0,183,23,1,0,0,0,
        184,185,3,10,5,0,185,25,1,0,0,0,186,191,3,38,19,0,187,191,3,40,20,
        0,188,191,3,42,21,0,189,191,3,46,23,0,190,186,1,0,0,0,190,187,1,
        0,0,0,190,188,1,0,0,0,190,189,1,0,0,0,191,27,1,0,0,0,192,197,3,38,
        19,0,193,197,3,40,20,0,194,197,3,42,21,0,195,197,3,44,22,0,196,192,
        1,0,0,0,196,193,1,0,0,0,196,194,1,0,0,0,196,195,1,0,0,0,197,29,1,
        0,0,0,198,219,3,18,9,0,199,219,3,36,18,0,200,201,3,18,9,0,201,202,
        5,28,0,0,202,203,3,16,8,0,203,204,5,29,0,0,204,219,1,0,0,0,205,206,
        3,36,18,0,206,207,5,28,0,0,207,208,3,16,8,0,208,209,5,29,0,0,209,
        219,1,0,0,0,210,211,5,12,0,0,211,219,3,18,9,0,212,213,5,12,0,0,213,
        219,3,36,18,0,214,215,5,7,0,0,215,219,3,18,9,0,216,217,5,7,0,0,217,
        219,3,36,18,0,218,198,1,0,0,0,218,199,1,0,0,0,218,200,1,0,0,0,218,
        205,1,0,0,0,218,210,1,0,0,0,218,212,1,0,0,0,218,214,1,0,0,0,218,
        216,1,0,0,0,219,31,1,0,0,0,220,221,5,17,0,0,221,33,1,0,0,0,222,223,
        7,0,0,0,223,35,1,0,0,0,224,225,7,1,0,0,225,37,1,0,0,0,226,227,7,
        2,0,0,227,39,1,0,0,0,228,229,7,3,0,0,229,41,1,0,0,0,230,231,7,4,
        0,0,231,43,1,0,0,0,232,233,7,5,0,0,233,45,1,0,0,0,234,235,5,5,0,
        0,235,47,1,0,0,0,15,55,59,102,108,121,148,150,155,159,166,175,182,
        190,196,218
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'dynamic'", "'var'", "<INVALID>", "'string'", 
                     "'...'", "'bool'", "'not'", "'and'", "'or'", "'number'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'<-'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "DYNAMIC_TYPE", "VAR_TYPE", "COMMENT", 
                      "STRING_TYPE", "STRING_OPERATOR", "BOOL_TYPE", "NOT_OPERATOR", 
                      "AND_OPERATOR", "OR_OPERATOR", "NUMBER_TYPE", "ADD_OPERATOR", 
                      "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", "MOD_OPERATOR", 
                      "KEYWORD", "NEWLINE", "EQ_OPERATOR", "NEQ_OPERATOR", 
                      "LT_OPERATOR", "GT_OPERATOR", "LEQ_OPERATOR", "GEQ_OPERATOR", 
                      "SEQ_OPERATOR", "ASSIGN_OPERATOR", "OPEN_PARENTHESIS", 
                      "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "COMMA", "BOOLEAN", "NUMBER", "IDENTIFIER", "STRING", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_arrlist = 4
    RULE_expression = 5
    RULE_sign_operands = 6
    RULE_not_operands = 7
    RULE_index_operators = 8
    RULE_func_call = 9
    RULE_param_list = 10
    RULE_param_prime = 11
    RULE_param = 12
    RULE_non_rel_operators = 13
    RULE_non_str_operators = 14
    RULE_non_associative_operands = 15
    RULE_funcdecl = 16
    RULE_typ = 17
    RULE_literal = 18
    RULE_mul_operators = 19
    RULE_add_operators = 20
    RULE_logic_operators = 21
    RULE_rel_operators = 22
    RULE_str_operators = 23

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "arrlist", 
                   "expression", "sign_operands", "not_operands", "index_operators", 
                   "func_call", "param_list", "param_prime", "param", "non_rel_operators", 
                   "non_str_operators", "non_associative_operands", "funcdecl", 
                   "typ", "literal", "mul_operators", "add_operators", "logic_operators", 
                   "rel_operators", "str_operators" ]

    EOF = Token.EOF
    DYNAMIC_TYPE=1
    VAR_TYPE=2
    COMMENT=3
    STRING_TYPE=4
    STRING_OPERATOR=5
    BOOL_TYPE=6
    NOT_OPERATOR=7
    AND_OPERATOR=8
    OR_OPERATOR=9
    NUMBER_TYPE=10
    ADD_OPERATOR=11
    SUB_OPERATOR=12
    MUL_OPERATOR=13
    DIV_OPERATOR=14
    MOD_OPERATOR=15
    KEYWORD=16
    NEWLINE=17
    EQ_OPERATOR=18
    NEQ_OPERATOR=19
    LT_OPERATOR=20
    GT_OPERATOR=21
    LEQ_OPERATOR=22
    GEQ_OPERATOR=23
    SEQ_OPERATOR=24
    ASSIGN_OPERATOR=25
    OPEN_PARENTHESIS=26
    CLOSE_PARENTHESIS=27
    OPEN_BRACKET=28
    CLOSE_BRACKET=29
    COMMA=30
    BOOLEAN=31
    NUMBER=32
    IDENTIFIER=33
    STRING=34
    UNCLOSE_STRING=35
    ILLEGAL_ESCAPE=36
    WS=37
    ERROR_CHAR=38

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
            self.state = 48
            self.decllist()
            self.state = 49
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
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.decl()
                self.state = 52
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
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
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 4, 6, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.vardecl()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.typ()
                self.state = 62
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 63
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 66
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 67
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(ZCodeParser.VAR_TYPE)
                self.state = 69
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 70
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 71
                self.expression(0)
                self.state = 72
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.typ()
                self.state = 75
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 76
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 77
                self.expression(0)
                self.state = 78
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 81
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 82
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 83
                self.expression(0)
                self.state = 84
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.typ()
                self.state = 87
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 88
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 89
                self.arrlist()
                self.state = 90
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 91
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
                self.typ()
                self.state = 94
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 95
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 96
                self.arrlist()
                self.state = 97
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 98
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 99
                self.expression(0)
                self.state = 100
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
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(ZCodeParser.NUMBER)
                self.state = 105
                self.match(ZCodeParser.COMMA)
                self.state = 106
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
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

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


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


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 112
                self.expression(0)
                self.state = 113
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 2:
                self.state = 115
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 116
                self.expression(9)
                pass

            elif la_ == 3:
                self.state = 117
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 118
                self.expression(8)
                pass

            elif la_ == 4:
                self.state = 119
                self.func_call()
                pass

            elif la_ == 5:
                self.state = 120
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 148
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 123
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 124
                        self.mul_operators()
                        self.state = 125
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 127
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 128
                        self.add_operators()
                        self.state = 129
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 131
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 132
                        self.logic_operators()
                        self.state = 133
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 135
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 136
                        self.rel_operators()
                        self.state = 137
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 139
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 140
                        self.str_operators()
                        self.state = 141
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 143
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 144
                        self.match(ZCodeParser.OPEN_BRACKET)
                        self.state = 145
                        self.index_operators()
                        self.state = 146
                        self.match(ZCodeParser.CLOSE_BRACKET)
                        pass

             
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Sign_operandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_operands




    def sign_operands(self):

        localctx = ZCodeParser.Sign_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sign_operands)
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.literal()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(ZCodeParser.SUB_OPERATOR)
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


    class Not_operandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def NOT_OPERATOR(self):
            return self.getToken(ZCodeParser.NOT_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_not_operands




    def not_operands(self):

        localctx = ZCodeParser.Not_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_not_operands)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.literal()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(ZCodeParser.NOT_OPERATOR)
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


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_index_operators)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.expression(0)
                self.state = 163
                self.match(ZCodeParser.COMMA)
                self.state = 164
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(ZCodeParser.OPEN_PARENTHESIS, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSE_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 169
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 170
            self.param_list()
            self.state = 171
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_list)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 12, 26, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.param_prime()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

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


    class Param_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_prime




    def param_prime(self):

        localctx = ZCodeParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_prime)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.param()
                self.state = 178
                self.match(ZCodeParser.COMMA)
                self.state = 179
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_rel_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_operatorsContext,0)


        def add_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Add_operatorsContext,0)


        def logic_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_operatorsContext,0)


        def str_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Str_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_non_rel_operators




    def non_rel_operators(self):

        localctx = ZCodeParser.Non_rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_non_rel_operators)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.mul_operators()
                pass
            elif token in [11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.add_operators()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.logic_operators()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.str_operators()
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


    class Non_str_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Mul_operatorsContext,0)


        def add_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Add_operatorsContext,0)


        def logic_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_operatorsContext,0)


        def rel_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Rel_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_non_str_operators




    def non_str_operators(self):

        localctx = ZCodeParser.Non_str_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_non_str_operators)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.mul_operators()
                pass
            elif token in [11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.add_operators()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.logic_operators()
                pass
            elif token in [18, 19, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.rel_operators()
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


    class Non_associative_operandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def SUB_OPERATOR(self):
            return self.getToken(ZCodeParser.SUB_OPERATOR, 0)

        def NOT_OPERATOR(self):
            return self.getToken(ZCodeParser.NOT_OPERATOR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_non_associative_operands




    def non_associative_operands(self):

        localctx = ZCodeParser.Non_associative_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_non_associative_operands)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.func_call()
                self.state = 201
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 202
                self.index_operators()
                self.state = 203
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.literal()
                self.state = 206
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 207
                self.index_operators()
                self.state = 208
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 211
                self.func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 212
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 213
                self.literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 215
                self.func_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 216
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 217
                self.literal()
                pass


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
        self.enterRule(localctx, 32, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
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
        self.enterRule(localctx, 34, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1104) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_mul_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_add_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
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
        self.enterRule(localctx, 42, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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
        self.enterRule(localctx, 44, self.RULE_rel_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33292288) != 0)):
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
        self.enterRule(localctx, 46, self.RULE_str_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         




