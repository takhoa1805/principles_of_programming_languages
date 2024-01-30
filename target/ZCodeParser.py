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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\34")
        buf.write("\n\3\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5K\n\5\3\6\3\6\3\6\3\6\5\6")
        buf.write("Q\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\2\2\13\2\4\6")
        buf.write("\b\n\f\16\20\22\2\3\5\2\b\b\n\n\f\f\2Z\2\24\3\2\2\2\4")
        buf.write("\33\3\2\2\2\6\37\3\2\2\2\bJ\3\2\2\2\nP\3\2\2\2\fR\3\2")
        buf.write("\2\2\16T\3\2\2\2\20V\3\2\2\2\22X\3\2\2\2\24\25\5\4\3\2")
        buf.write("\25\26\7\2\2\3\26\3\3\2\2\2\27\30\5\6\4\2\30\31\5\4\3")
        buf.write("\2\31\34\3\2\2\2\32\34\5\6\4\2\33\27\3\2\2\2\33\32\3\2")
        buf.write("\2\2\34\5\3\2\2\2\35 \5\b\5\2\36 \5\20\t\2\37\35\3\2\2")
        buf.write("\2\37\36\3\2\2\2 \7\3\2\2\2!\"\5\22\n\2\"#\7\31\2\2#$")
        buf.write("\7\17\2\2$K\3\2\2\2%&\7\5\2\2&\'\7\31\2\2\'K\7\17\2\2")
        buf.write("()\7\6\2\2)*\7\31\2\2*+\7\21\2\2+,\5\16\b\2,-\7\17\2\2")
        buf.write("-K\3\2\2\2./\5\22\n\2/\60\7\31\2\2\60\61\7\21\2\2\61\62")
        buf.write("\5\16\b\2\62\63\7\17\2\2\63K\3\2\2\2\64\65\7\5\2\2\65")
        buf.write("\66\7\31\2\2\66\67\7\21\2\2\678\5\16\b\289\7\17\2\29K")
        buf.write("\3\2\2\2:;\5\22\n\2;<\7\31\2\2<=\7\24\2\2=>\5\n\6\2>?")
        buf.write("\7\25\2\2?@\7\17\2\2@K\3\2\2\2AB\5\22\n\2BC\7\31\2\2C")
        buf.write("D\7\24\2\2DE\5\n\6\2EF\7\25\2\2FG\7\21\2\2GH\5\f\7\2H")
        buf.write("I\7\17\2\2IK\3\2\2\2J!\3\2\2\2J%\3\2\2\2J(\3\2\2\2J.\3")
        buf.write("\2\2\2J\64\3\2\2\2J:\3\2\2\2JA\3\2\2\2K\t\3\2\2\2LM\7")
        buf.write("\30\2\2MN\7\26\2\2NQ\5\n\6\2OQ\7\30\2\2PL\3\2\2\2PO\3")
        buf.write("\2\2\2Q\13\3\2\2\2RS\7\3\2\2S\r\3\2\2\2TU\7\4\2\2U\17")
        buf.write("\3\2\2\2VW\7\17\2\2W\21\3\2\2\2XY\t\2\2\2Y\23\3\2\2\2")
        buf.write("\6\33\37JP")
        return buf.getvalue()


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
    RULE_arrexp = 5
    RULE_exp = 6
    RULE_funcdecl = 7
    RULE_typ = 8

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "arrlist", 
                   "arrexp", "exp", "funcdecl", "typ" ]

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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.DYNAMIC_TYPE, ZCodeParser.VAR_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.NUMBER_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.vardecl()
                pass
            elif token in [ZCodeParser.NEWLINE]:
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

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def arrexp(self):
            return self.getTypedRuleContext(ZCodeParser.ArrexpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




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
                self.exp()
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
                self.exp()
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
                self.exp()
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
                self.arrexp()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlist" ):
                return visitor.visitArrlist(self)
            else:
                return visitor.visitChildren(self)




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


    class ArrexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrexp" ):
                return visitor.visitArrexp(self)
            else:
                return visitor.visitChildren(self)




    def arrexp(self):

        localctx = ZCodeParser.ArrexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrexp)
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exp)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.STRING_TYPE) | (1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.NUMBER_TYPE))) != 0)):
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





