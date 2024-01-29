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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u0162\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\7")
        buf.write("\6s\n\6\f\6\16\6v\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u0090\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\5\r\u00ce\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00dc\n\17\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00f4\n")
        buf.write("\26\3\27\6\27\u00f7\n\27\r\27\16\27\u00f8\3\27\3\27\7")
        buf.write("\27\u00fd\n\27\f\27\16\27\u0100\13\27\5\27\u0102\n\27")
        buf.write("\3\27\5\27\u0105\n\27\3\27\6\27\u0108\n\27\r\27\16\27")
        buf.write("\u0109\3\27\3\27\5\27\u010e\n\27\3\30\3\30\3\31\3\31\5")
        buf.write("\31\u0114\n\31\3\31\6\31\u0117\n\31\r\31\16\31\u0118\3")
        buf.write("\32\3\32\7\32\u011d\n\32\f\32\16\32\u0120\13\32\3\33\3")
        buf.write("\33\3\33\3\33\7\33\u0126\n\33\f\33\16\33\u0129\13\33\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \7 \u013e\n \f \16 \u0141")
        buf.write("\13 \3 \5 \u0144\n \3 \3 \3!\3!\3!\3!\7!\u014c\n!\f!\16")
        buf.write("!\u014f\13!\3!\3!\3!\3!\5!\u0155\n!\3!\3!\3\"\6\"\u015a")
        buf.write("\n\"\r\"\16\"\u015b\3\"\3\"\3#\3#\3#\2\2$\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\2\61\2\63\31\65")
        buf.write("\32\67\29\2;\2=\2?\33A\34C\35E\36\3\2\23\4\2\f\f\17\17")
        buf.write("\6\2\'\',-//\61\61\3\2\f\f\4\2>>@@\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\5\2C\\aac|\6\2\62;C\\aac|\7\2\f\f\17\17$$))^^\t\2")
        buf.write("))^^ddhhppttvv\5\2$$))^^\4\3\f\f\17\17\5\2\f\f\17\17$")
        buf.write("$\3\2))\3\2$$\5\2\n\13\16\17\"\"\2\u0183\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\3G\3\2\2\2\5W\3\2\2\2\7b\3\2\2\2\tj\3\2\2\2\13n\3\2")
        buf.write("\2\2\rw\3\2\2\2\17~\3\2\2\2\21\u0082\3\2\2\2\23\u008f")
        buf.write("\3\2\2\2\25\u0091\3\2\2\2\27\u0098\3\2\2\2\31\u00cd\3")
        buf.write("\2\2\2\33\u00cf\3\2\2\2\35\u00db\3\2\2\2\37\u00dd\3\2")
        buf.write("\2\2!\u00e0\3\2\2\2#\u00e2\3\2\2\2%\u00e4\3\2\2\2\'\u00e6")
        buf.write("\3\2\2\2)\u00e8\3\2\2\2+\u00f3\3\2\2\2-\u010d\3\2\2\2")
        buf.write("/\u010f\3\2\2\2\61\u0111\3\2\2\2\63\u011a\3\2\2\2\65\u0121")
        buf.write("\3\2\2\2\67\u012d\3\2\2\29\u012f\3\2\2\2;\u0132\3\2\2")
        buf.write("\2=\u0135\3\2\2\2?\u0139\3\2\2\2A\u0147\3\2\2\2C\u0159")
        buf.write("\3\2\2\2E\u015f\3\2\2\2GH\7c\2\2HI\7t\2\2IJ\7t\2\2JK\7")
        buf.write("c\2\2KL\7{\2\2LM\7g\2\2MN\7z\2\2NO\7r\2\2OP\7t\2\2PQ\7")
        buf.write("g\2\2QR\7u\2\2RS\7u\2\2ST\7k\2\2TU\7q\2\2UV\7p\2\2V\4")
        buf.write("\3\2\2\2WX\7g\2\2XY\7z\2\2YZ\7r\2\2Z[\7t\2\2[\\\7g\2\2")
        buf.write("\\]\7u\2\2]^\7u\2\2^_\7k\2\2_`\7q\2\2`a\7p\2\2a\6\3\2")
        buf.write("\2\2bc\7f\2\2cd\7{\2\2de\7p\2\2ef\7c\2\2fg\7o\2\2gh\7")
        buf.write("k\2\2hi\7e\2\2i\b\3\2\2\2jk\7x\2\2kl\7c\2\2lm\7t\2\2m")
        buf.write("\n\3\2\2\2no\7%\2\2op\7%\2\2pt\3\2\2\2qs\n\2\2\2rq\3\2")
        buf.write("\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\f\3\2\2\2vt\3\2\2")
        buf.write("\2wx\7u\2\2xy\7v\2\2yz\7t\2\2z{\7k\2\2{|\7p\2\2|}\7i\2")
        buf.write("\2}\16\3\2\2\2~\177\7\60\2\2\177\u0080\7\60\2\2\u0080")
        buf.write("\u0081\7\60\2\2\u0081\20\3\2\2\2\u0082\u0083\7d\2\2\u0083")
        buf.write("\u0084\7q\2\2\u0084\u0085\7q\2\2\u0085\u0086\7n\2\2\u0086")
        buf.write("\22\3\2\2\2\u0087\u0088\7p\2\2\u0088\u0089\7q\2\2\u0089")
        buf.write("\u0090\7v\2\2\u008a\u008b\7c\2\2\u008b\u008c\7p\2\2\u008c")
        buf.write("\u0090\7f\2\2\u008d\u008e\7q\2\2\u008e\u0090\7t\2\2\u008f")
        buf.write("\u0087\3\2\2\2\u008f\u008a\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\24\3\2\2\2\u0091\u0092\7p\2\2\u0092\u0093\7w\2")
        buf.write("\2\u0093\u0094\7o\2\2\u0094\u0095\7d\2\2\u0095\u0096\7")
        buf.write("g\2\2\u0096\u0097\7t\2\2\u0097\26\3\2\2\2\u0098\u0099")
        buf.write("\t\3\2\2\u0099\30\3\2\2\2\u009a\u009b\7t\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7v\2\2\u009d\u009e\7w\2\2\u009e\u009f")
        buf.write("\7t\2\2\u009f\u00ce\7p\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2")
        buf.write("\7w\2\2\u00a2\u00a3\7p\2\2\u00a3\u00ce\7e\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\u00a6\7q\2\2\u00a6\u00ce\7t\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7k\2\2\u00ab\u00ce\7n\2\2\u00ac\u00ad\7d\2\2\u00ad\u00ce")
        buf.write("\7{\2\2\u00ae\u00af\7d\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00ce\7m\2\2\u00b3\u00b4")
        buf.write("\7e\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba")
        buf.write("\7w\2\2\u00ba\u00ce\7g\2\2\u00bb\u00bc\7k\2\2\u00bc\u00ce")
        buf.write("\7h\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\u00ce\7g\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3")
        buf.write("\7n\2\2\u00c3\u00c4\7k\2\2\u00c4\u00ce\7h\2\2\u00c5\u00c6")
        buf.write("\7d\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7i\2\2\u00c8\u00c9")
        buf.write("\7k\2\2\u00c9\u00ce\7p\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00ce\7f\2\2\u00cd\u009a\3\2\2\2\u00cd\u00a0")
        buf.write("\3\2\2\2\u00cd\u00a4\3\2\2\2\u00cd\u00a7\3\2\2\2\u00cd")
        buf.write("\u00ac\3\2\2\2\u00cd\u00ae\3\2\2\2\u00cd\u00b3\3\2\2\2")
        buf.write("\u00cd\u00bb\3\2\2\2\u00cd\u00bd\3\2\2\2\u00cd\u00c1\3")
        buf.write("\2\2\2\u00cd\u00c5\3\2\2\2\u00cd\u00ca\3\2\2\2\u00ce\32")
        buf.write("\3\2\2\2\u00cf\u00d0\t\4\2\2\u00d0\34\3\2\2\2\u00d1\u00dc")
        buf.write("\7?\2\2\u00d2\u00d3\7#\2\2\u00d3\u00dc\7?\2\2\u00d4\u00dc")
        buf.write("\t\5\2\2\u00d5\u00d6\7>\2\2\u00d6\u00dc\7?\2\2\u00d7\u00d8")
        buf.write("\7@\2\2\u00d8\u00dc\7?\2\2\u00d9\u00da\7?\2\2\u00da\u00dc")
        buf.write("\7?\2\2\u00db\u00d1\3\2\2\2\u00db\u00d2\3\2\2\2\u00db")
        buf.write("\u00d4\3\2\2\2\u00db\u00d5\3\2\2\2\u00db\u00d7\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7>\2")
        buf.write("\2\u00de\u00df\7/\2\2\u00df \3\2\2\2\u00e0\u00e1\7*\2")
        buf.write("\2\u00e1\"\3\2\2\2\u00e2\u00e3\7+\2\2\u00e3$\3\2\2\2\u00e4")
        buf.write("\u00e5\7]\2\2\u00e5&\3\2\2\2\u00e6\u00e7\7_\2\2\u00e7")
        buf.write("(\3\2\2\2\u00e8\u00e9\7.\2\2\u00e9*\3\2\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed\7w\2\2\u00ed\u00f4")
        buf.write("\7g\2\2\u00ee\u00ef\7h\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f4\7g\2\2\u00f3\u00ea")
        buf.write("\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f4,\3\2\2\2\u00f5\u00f7")
        buf.write("\5/\30\2\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u0101\3\2\2\2")
        buf.write("\u00fa\u00fe\7\60\2\2\u00fb\u00fd\5/\30\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2")
        buf.write("\u0101\u00fa\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0104\3")
        buf.write("\2\2\2\u0103\u0105\5\61\31\2\u0104\u0103\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u010e\3\2\2\2\u0106\u0108\5/\30\2")
        buf.write("\u0107\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u0107\3")
        buf.write("\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c")
        buf.write("\5\61\31\2\u010c\u010e\3\2\2\2\u010d\u00f6\3\2\2\2\u010d")
        buf.write("\u0107\3\2\2\2\u010e.\3\2\2\2\u010f\u0110\t\6\2\2\u0110")
        buf.write("\60\3\2\2\2\u0111\u0113\t\7\2\2\u0112\u0114\t\b\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2")
        buf.write("\u0115\u0117\5/\30\2\u0116\u0115\3\2\2\2\u0117\u0118\3")
        buf.write("\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\62")
        buf.write("\3\2\2\2\u011a\u011e\t\t\2\2\u011b\u011d\t\n\2\2\u011c")
        buf.write("\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f\64\3\2\2\2\u0120\u011e\3\2")
        buf.write("\2\2\u0121\u0127\5\67\34\2\u0122\u0126\n\13\2\2\u0123")
        buf.write("\u0126\5;\36\2\u0124\u0126\59\35\2\u0125\u0122\3\2\2\2")
        buf.write("\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u0126\u0129\3")
        buf.write("\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a")
        buf.write("\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\5\67\34\2\u012b")
        buf.write("\u012c\b\33\2\2\u012c\66\3\2\2\2\u012d\u012e\7$\2\2\u012e")
        buf.write("8\3\2\2\2\u012f\u0130\7)\2\2\u0130\u0131\7$\2\2\u0131")
        buf.write(":\3\2\2\2\u0132\u0133\7^\2\2\u0133\u0134\t\f\2\2\u0134")
        buf.write("<\3\2\2\2\u0135\u0136\7^\2\2\u0136\u0137\7^\2\2\u0137")
        buf.write("\u0138\n\f\2\2\u0138>\3\2\2\2\u0139\u013f\5\67\34\2\u013a")
        buf.write("\u013e\n\r\2\2\u013b\u013e\59\35\2\u013c\u013e\5;\36\2")
        buf.write("\u013d\u013a\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c\3")
        buf.write("\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0142")
        buf.write("\u0144\t\16\2\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2")
        buf.write("\2\u0145\u0146\b \3\2\u0146@\3\2\2\2\u0147\u014d\5\67")
        buf.write("\34\2\u0148\u014c\n\17\2\2\u0149\u014c\59\35\2\u014a\u014c")
        buf.write("\5;\36\2\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2")
        buf.write("\u014d\u014e\3\2\2\2\u014e\u0154\3\2\2\2\u014f\u014d\3")
        buf.write("\2\2\2\u0150\u0151\7^\2\2\u0151\u0155\n\f\2\2\u0152\u0153")
        buf.write("\t\20\2\2\u0153\u0155\n\21\2\2\u0154\u0150\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\b!\4\2")
        buf.write("\u0157B\3\2\2\2\u0158\u015a\t\22\2\2\u0159\u0158\3\2\2")
        buf.write("\2\u015a\u015b\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\b\"\5\2\u015e")
        buf.write("D\3\2\2\2\u015f\u0160\13\2\2\2\u0160\u0161\b#\6\2\u0161")
        buf.write("F\3\2\2\2\32\2t\u008f\u00cd\u00db\u00f3\u00f8\u00fe\u0101")
        buf.write("\u0104\u0109\u010d\u0113\u0118\u011e\u0125\u0127\u013d")
        buf.write("\u013f\u0143\u014b\u014d\u0154\u015b\7\3\33\2\3 \3\3!")
        buf.write("\4\b\2\2\3#\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    DYNAMIC_TYPE = 3
    VAR_TYPE = 4
    COMMENT = 5
    STRING_TYPE = 6
    STRING_OPERATOR = 7
    BOOL_TYPE = 8
    LOGIC_OPERATOR = 9
    NUMBER_TYPE = 10
    ARITHMETIC_OPERATORS = 11
    KEYWORD = 12
    NEWLINE = 13
    RELATIONAL_OPERATOR = 14
    ASSIGN_OPERATOR = 15
    OPEN_PARENTHESIS = 16
    CLOSE_PARENTHESIS = 17
    OPEN_BRACKET = 18
    CLOSE_BRACKET = 19
    COMMA = 20
    BOOLEAN = 21
    NUMBER = 22
    IDENTIFIER = 23
    STRING = 24
    UNCLOSE_STRING = 25
    ILLEGAL_ESCAPE = 26
    WS = 27
    ERROR_CHAR = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'arrayexpression'", "'expression'", "'dynamic'", "'var'", "'string'", 
            "'...'", "'bool'", "'number'", "'<-'", "'('", "')'", "'['", 
            "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DYNAMIC_TYPE", "VAR_TYPE", "COMMENT", "STRING_TYPE", "STRING_OPERATOR", 
            "BOOL_TYPE", "LOGIC_OPERATOR", "NUMBER_TYPE", "ARITHMETIC_OPERATORS", 
            "KEYWORD", "NEWLINE", "RELATIONAL_OPERATOR", "ASSIGN_OPERATOR", 
            "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
            "COMMA", "BOOLEAN", "NUMBER", "IDENTIFIER", "STRING", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "DYNAMIC_TYPE", "VAR_TYPE", "COMMENT", 
                  "STRING_TYPE", "STRING_OPERATOR", "BOOL_TYPE", "LOGIC_OPERATOR", 
                  "NUMBER_TYPE", "ARITHMETIC_OPERATORS", "KEYWORD", "NEWLINE", 
                  "RELATIONAL_OPERATOR", "ASSIGN_OPERATOR", "OPEN_PARENTHESIS", 
                  "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
                  "COMMA", "BOOLEAN", "NUMBER", "DIGIT", "EXPONENT", "IDENTIFIER", 
                  "STRING", "DOUBLE_QUOTE", "DOUBLE_QUOTE_NOTATION", "LEGAL_ESCAPE_SEQUENCE", 
                  "ILLEGAL_ESCAPE_SEQUENCE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "WS", "ERROR_CHAR" ]

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
            actions[25] = self.STRING_action 
            actions[30] = self.UNCLOSE_STRING_action 
            actions[31] = self.ILLEGAL_ESCAPE_action 
            actions[33] = self.ERROR_CHAR_action 
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
     


