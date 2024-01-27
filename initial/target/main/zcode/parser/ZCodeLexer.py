# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u0146\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \3\2\3\2\3\2\3\2\7\2F\n\2\f\2\16")
        buf.write("\2I\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("c\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00ab\n\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b9\n\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c3\n\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00d8\n\23\3\24\6")
        buf.write("\24\u00db\n\24\r\24\16\24\u00dc\3\24\3\24\7\24\u00e1\n")
        buf.write("\24\f\24\16\24\u00e4\13\24\5\24\u00e6\n\24\3\24\5\24\u00e9")
        buf.write("\n\24\3\24\6\24\u00ec\n\24\r\24\16\24\u00ed\3\24\3\24")
        buf.write("\5\24\u00f2\n\24\3\25\3\25\3\26\3\26\5\26\u00f8\n\26\3")
        buf.write("\26\6\26\u00fb\n\26\r\26\16\26\u00fc\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u0103\n\27\f\27\16\27\u0106\13\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u011b\n\34\f\34\16")
        buf.write("\34\u011e\13\34\3\34\5\34\u0121\n\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\3\35\7\35\u0129\n\35\f\35\16\35\u012c\13\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0132\n\35\3\35\3\35\3\36\3\36")
        buf.write("\7\36\u0138\n\36\f\36\16\36\u013b\13\36\3\37\6\37\u013e")
        buf.write("\n\37\r\37\16\37\u013f\3\37\3\37\3 \3 \3 \2\2!\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\2")
        buf.write("\35\2\37\2!\2#\2%\17\'\20)\2+\2-\21/\2\61\2\63\2\65\2")
        buf.write("\67\229\23;\24=\25?\26\3\2\23\4\2\f\f\17\17\6\2\'\',-")
        buf.write("//\61\61\3\2\f\f\4\2>>@@\3\2\62;\4\2GGgg\4\2--//\7\2\f")
        buf.write("\f\17\17$$))^^\t\2))^^ddhhppttvv\5\2$$))^^\4\3\f\f\17")
        buf.write("\17\5\2\f\f\17\17$$\3\2))\3\2$$\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\5\2\n\13\16\17\"\"\2\u0168\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2-\3\2\2")
        buf.write("\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3")
        buf.write("\2\2\2\3A\3\2\2\2\5J\3\2\2\2\7Q\3\2\2\2\tU\3\2\2\2\13")
        buf.write("b\3\2\2\2\rd\3\2\2\2\17k\3\2\2\2\21\u00aa\3\2\2\2\23\u00ac")
        buf.write("\3\2\2\2\25\u00b8\3\2\2\2\27\u00ba\3\2\2\2\31\u00c2\3")
        buf.write("\2\2\2\33\u00c4\3\2\2\2\35\u00c6\3\2\2\2\37\u00c8\3\2")
        buf.write("\2\2!\u00ca\3\2\2\2#\u00cc\3\2\2\2%\u00d7\3\2\2\2\'\u00f1")
        buf.write("\3\2\2\2)\u00f3\3\2\2\2+\u00f5\3\2\2\2-\u00fe\3\2\2\2")
        buf.write("/\u010a\3\2\2\2\61\u010c\3\2\2\2\63\u010f\3\2\2\2\65\u0112")
        buf.write("\3\2\2\2\67\u0116\3\2\2\29\u0124\3\2\2\2;\u0135\3\2\2")
        buf.write("\2=\u013d\3\2\2\2?\u0143\3\2\2\2AB\7%\2\2BC\7%\2\2CG\3")
        buf.write("\2\2\2DF\n\2\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2")
        buf.write("\2H\4\3\2\2\2IG\3\2\2\2JK\7u\2\2KL\7v\2\2LM\7t\2\2MN\7")
        buf.write("k\2\2NO\7p\2\2OP\7i\2\2P\6\3\2\2\2QR\7\60\2\2RS\7\60\2")
        buf.write("\2ST\7\60\2\2T\b\3\2\2\2UV\7d\2\2VW\7q\2\2WX\7q\2\2XY")
        buf.write("\7n\2\2Y\n\3\2\2\2Z[\7p\2\2[\\\7q\2\2\\c\7v\2\2]^\7c\2")
        buf.write("\2^_\7p\2\2_c\7f\2\2`a\7q\2\2ac\7t\2\2bZ\3\2\2\2b]\3\2")
        buf.write("\2\2b`\3\2\2\2c\f\3\2\2\2de\7p\2\2ef\7w\2\2fg\7o\2\2g")
        buf.write("h\7d\2\2hi\7g\2\2ij\7t\2\2j\16\3\2\2\2kl\t\3\2\2l\20\3")
        buf.write("\2\2\2mn\7t\2\2no\7g\2\2op\7v\2\2pq\7w\2\2qr\7t\2\2r\u00ab")
        buf.write("\7p\2\2st\7x\2\2tu\7c\2\2u\u00ab\7t\2\2vw\7f\2\2wx\7{")
        buf.write("\2\2xy\7p\2\2yz\7c\2\2z{\7o\2\2{|\7k\2\2|\u00ab\7e\2\2")
        buf.write("}~\7h\2\2~\177\7w\2\2\177\u0080\7p\2\2\u0080\u00ab\7e")
        buf.write("\2\2\u0081\u0082\7h\2\2\u0082\u0083\7q\2\2\u0083\u00ab")
        buf.write("\7t\2\2\u0084\u0085\7w\2\2\u0085\u0086\7p\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\u0088\7k\2\2\u0088\u00ab\7n\2\2\u0089\u008a")
        buf.write("\7d\2\2\u008a\u00ab\7{\2\2\u008b\u008c\7d\2\2\u008c\u008d")
        buf.write("\7t\2\2\u008d\u008e\7g\2\2\u008e\u008f\7c\2\2\u008f\u00ab")
        buf.write("\7m\2\2\u0090\u0091\7e\2\2\u0091\u0092\7q\2\2\u0092\u0093")
        buf.write("\7p\2\2\u0093\u0094\7v\2\2\u0094\u0095\7k\2\2\u0095\u0096")
        buf.write("\7p\2\2\u0096\u0097\7w\2\2\u0097\u00ab\7g\2\2\u0098\u0099")
        buf.write("\7k\2\2\u0099\u00ab\7h\2\2\u009a\u009b\7g\2\2\u009b\u009c")
        buf.write("\7n\2\2\u009c\u009d\7u\2\2\u009d\u00ab\7g\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7k\2\2\u00a1\u00ab")
        buf.write("\7h\2\2\u00a2\u00a3\7d\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5")
        buf.write("\7i\2\2\u00a5\u00a6\7k\2\2\u00a6\u00ab\7p\2\2\u00a7\u00a8")
        buf.write("\7g\2\2\u00a8\u00a9\7p\2\2\u00a9\u00ab\7f\2\2\u00aam\3")
        buf.write("\2\2\2\u00aas\3\2\2\2\u00aav\3\2\2\2\u00aa}\3\2\2\2\u00aa")
        buf.write("\u0081\3\2\2\2\u00aa\u0084\3\2\2\2\u00aa\u0089\3\2\2\2")
        buf.write("\u00aa\u008b\3\2\2\2\u00aa\u0090\3\2\2\2\u00aa\u0098\3")
        buf.write("\2\2\2\u00aa\u009a\3\2\2\2\u00aa\u009e\3\2\2\2\u00aa\u00a2")
        buf.write("\3\2\2\2\u00aa\u00a7\3\2\2\2\u00ab\22\3\2\2\2\u00ac\u00ad")
        buf.write("\t\4\2\2\u00ad\24\3\2\2\2\u00ae\u00b9\7?\2\2\u00af\u00b0")
        buf.write("\7#\2\2\u00b0\u00b9\7?\2\2\u00b1\u00b9\t\5\2\2\u00b2\u00b3")
        buf.write("\7>\2\2\u00b3\u00b9\7?\2\2\u00b4\u00b5\7@\2\2\u00b5\u00b9")
        buf.write("\7?\2\2\u00b6\u00b7\7?\2\2\u00b7\u00b9\7?\2\2\u00b8\u00ae")
        buf.write("\3\2\2\2\u00b8\u00af\3\2\2\2\u00b8\u00b1\3\2\2\2\u00b8")
        buf.write("\u00b2\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b9\26\3\2\2\2\u00ba\u00bb\7>\2\2\u00bb\u00bc\7/\2")
        buf.write("\2\u00bc\30\3\2\2\2\u00bd\u00c3\5\37\20\2\u00be\u00c3")
        buf.write("\5!\21\2\u00bf\u00c3\5\33\16\2\u00c0\u00c3\5\35\17\2\u00c1")
        buf.write("\u00c3\5#\22\2\u00c2\u00bd\3\2\2\2\u00c2\u00be\3\2\2\2")
        buf.write("\u00c2\u00bf\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3")
        buf.write("\2\2\2\u00c3\32\3\2\2\2\u00c4\u00c5\7*\2\2\u00c5\34\3")
        buf.write("\2\2\2\u00c6\u00c7\7+\2\2\u00c7\36\3\2\2\2\u00c8\u00c9")
        buf.write("\7]\2\2\u00c9 \3\2\2\2\u00ca\u00cb\7_\2\2\u00cb\"\3\2")
        buf.write("\2\2\u00cc\u00cd\7.\2\2\u00cd$\3\2\2\2\u00ce\u00cf\7v")
        buf.write("\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d8")
        buf.write("\7g\2\2\u00d2\u00d3\7h\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7n\2\2\u00d5\u00d6\7u\2\2\u00d6\u00d8\7g\2\2\u00d7\u00ce")
        buf.write("\3\2\2\2\u00d7\u00d2\3\2\2\2\u00d8&\3\2\2\2\u00d9\u00db")
        buf.write("\5)\25\2\u00da\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e5\3\2\2\2")
        buf.write("\u00de\u00e2\7\60\2\2\u00df\u00e1\5)\25\2\u00e0\u00df")
        buf.write("\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e5\u00de\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3")
        buf.write("\2\2\2\u00e7\u00e9\5+\26\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00f2\3\2\2\2\u00ea\u00ec\5)\25\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\5")
        buf.write("+\26\2\u00f0\u00f2\3\2\2\2\u00f1\u00da\3\2\2\2\u00f1\u00eb")
        buf.write("\3\2\2\2\u00f2(\3\2\2\2\u00f3\u00f4\t\6\2\2\u00f4*\3\2")
        buf.write("\2\2\u00f5\u00f7\t\7\2\2\u00f6\u00f8\t\b\2\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9")
        buf.write("\u00fb\5)\25\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd,\3\2\2")
        buf.write("\2\u00fe\u0104\5/\30\2\u00ff\u0103\n\t\2\2\u0100\u0103")
        buf.write("\5\63\32\2\u0101\u0103\5\61\31\2\u0102\u00ff\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0102\u0101\3\2\2\2\u0103\u0106\3\2\2\2")
        buf.write("\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0107\3")
        buf.write("\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\5/\30\2\u0108\u0109")
        buf.write("\b\27\2\2\u0109.\3\2\2\2\u010a\u010b\7$\2\2\u010b\60\3")
        buf.write("\2\2\2\u010c\u010d\7)\2\2\u010d\u010e\7$\2\2\u010e\62")
        buf.write("\3\2\2\2\u010f\u0110\7^\2\2\u0110\u0111\t\n\2\2\u0111")
        buf.write("\64\3\2\2\2\u0112\u0113\7^\2\2\u0113\u0114\7^\2\2\u0114")
        buf.write("\u0115\n\n\2\2\u0115\66\3\2\2\2\u0116\u011c\5/\30\2\u0117")
        buf.write("\u011b\n\13\2\2\u0118\u011b\5\61\31\2\u0119\u011b\5\63")
        buf.write("\32\2\u011a\u0117\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u0119")
        buf.write("\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011f\u0121\t\f\2\2\u0120\u011f\3\2\2\2\u0121\u0122\3")
        buf.write("\2\2\2\u0122\u0123\b\34\3\2\u01238\3\2\2\2\u0124\u012a")
        buf.write("\5/\30\2\u0125\u0129\n\r\2\2\u0126\u0129\5\61\31\2\u0127")
        buf.write("\u0129\5\63\32\2\u0128\u0125\3\2\2\2\u0128\u0126\3\2\2")
        buf.write("\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u0131\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012d\u012e\7^\2\2\u012e\u0132\n\n\2\2")
        buf.write("\u012f\u0130\t\16\2\2\u0130\u0132\n\17\2\2\u0131\u012d")
        buf.write("\3\2\2\2\u0131\u012f\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u0134\b\35\4\2\u0134:\3\2\2\2\u0135\u0139\t\20\2\2\u0136")
        buf.write("\u0138\t\21\2\2\u0137\u0136\3\2\2\2\u0138\u013b\3\2\2")
        buf.write("\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a<\3\2")
        buf.write("\2\2\u013b\u0139\3\2\2\2\u013c\u013e\t\22\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u013d\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\b\37\5")
        buf.write("\2\u0142>\3\2\2\2\u0143\u0144\13\2\2\2\u0144\u0145\b ")
        buf.write("\6\2\u0145@\3\2\2\2\33\2Gb\u00aa\u00b8\u00c2\u00d7\u00dc")
        buf.write("\u00e2\u00e5\u00e8\u00ed\u00f1\u00f7\u00fc\u0102\u0104")
        buf.write("\u011a\u011c\u0120\u0128\u012a\u0131\u0139\u013f\7\3\27")
        buf.write("\2\3\34\3\3\35\4\b\2\2\3 \5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    STRING_TYPE = 2
    STRING_OPERATOR = 3
    BOOLEAN_TYPE = 4
    LOGIC_OPERATOR = 5
    NUMERIC_TYPE = 6
    ARITHMETIC_OPERATORS = 7
    KEYWORD = 8
    CHARSET = 9
    RELATIONAL_OPERATOR = 10
    ASSIGN_OPERATOR = 11
    SEPARATOR = 12
    BOOLEAN = 13
    NUMBER = 14
    STRING = 15
    UNCLOSE_STRING = 16
    ILLEGAL_ESCAPE = 17
    IDENTIFIER = 18
    WS = 19
    ERROR_CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'string'", "'...'", "'bool'", "'number'", "'<-'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "STRING_TYPE", "STRING_OPERATOR", "BOOLEAN_TYPE", 
            "LOGIC_OPERATOR", "NUMERIC_TYPE", "ARITHMETIC_OPERATORS", "KEYWORD", 
            "CHARSET", "RELATIONAL_OPERATOR", "ASSIGN_OPERATOR", "SEPARATOR", 
            "BOOLEAN", "NUMBER", "STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "IDENTIFIER", "WS", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "STRING_TYPE", "STRING_OPERATOR", "BOOLEAN_TYPE", 
                  "LOGIC_OPERATOR", "NUMERIC_TYPE", "ARITHMETIC_OPERATORS", 
                  "KEYWORD", "CHARSET", "RELATIONAL_OPERATOR", "ASSIGN_OPERATOR", 
                  "SEPARATOR", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                  "OPEN_BRACKET", "CLOSE_BRACKET", "COMMA", "BOOLEAN", "NUMBER", 
                  "DIGIT", "EXPONENT", "STRING", "DOUBLE_QUOTE", "DOUBLE_QUOTE_NOTATION", 
                  "LEGAL_ESCAPE_SEQUENCE", "ILLEGAL_ESCAPE_SEQUENCE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "IDENTIFIER", "WS", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[21] = self.STRING_action 
            actions[26] = self.UNCLOSE_STRING_action 
            actions[27] = self.ILLEGAL_ESCAPE_action 
            actions[30] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]
            	#print("this is a string: "+self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text[1:]
            	print("this is an unclosed string: "+repr(self.text))
            	
            	#Windows case
            	tmp = self.text[::-1].find("\n")

            	if (tmp != -1):
            		if (self.text[::-1].find("\n\r")!=-1):
            			self.text = self.text[0:len(self.text)-tmp-2]
            			print("windows case: "+repr(self.text))
            			raise UncloseString(self.text)
            			return
            		else:
            			#Linux case
            			tmp = self.text[::-1].find("\n")

            			if(tmp!=-1):
            				self.text = self.text[0:len(self.text)-tmp-1]
            				print("Linux case: "+self.text)
            				raise UncloseString(self.text)
            				return

            	raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:]
            	print("this is illegal escape: "+self.text)
            	raise IllegalEscape(self.text)
            	

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


