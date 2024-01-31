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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u018a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3`\n\3\3\4\3\4\5\4d\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5\u0097\n\5\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u009d\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u00aa\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\7\7\u00c5\n\7\f\7\16\7\u00c8\13\7\3\b\3\b\5\b\u00cc")
        buf.write("\n\b\3\t\3\t\5\t\u00d0\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00d7")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00e0\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00e7\n\r\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u00ef\n\17\3\20\3\20\3\20\3\20\5\20\u00f5")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u010b\n\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3")
        buf.write("\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\5\33\u0129")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\5\34\u0130\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u013b\n\35")
        buf.write("\3\36\3\36\3\36\5\36\u0140\n\36\3\37\3\37\3\37\5\37\u0145")
        buf.write("\n\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\5!\u0151\n!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u015b\n\"\3#\3#\3#\5#\u0160")
        buf.write("\n#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\5\'\u0176\n\'\3(\3(\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\2\3\f-\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTV\2\b\4\2\13\f\21\21\3\2),\3\2\27\31\3\2\25")
        buf.write("\26\3\2\23\24\3\2\34\"\2\u0193\2X\3\2\2\2\4_\3\2\2\2\6")
        buf.write("c\3\2\2\2\b\u0096\3\2\2\2\n\u009c\3\2\2\2\f\u00a9\3\2")
        buf.write("\2\2\16\u00cb\3\2\2\2\20\u00cf\3\2\2\2\22\u00d6\3\2\2")
        buf.write("\2\24\u00d8\3\2\2\2\26\u00df\3\2\2\2\30\u00e6\3\2\2\2")
        buf.write("\32\u00e8\3\2\2\2\34\u00ee\3\2\2\2\36\u00f4\3\2\2\2 \u010a")
        buf.write("\3\2\2\2\"\u010c\3\2\2\2$\u010e\3\2\2\2&\u0110\3\2\2\2")
        buf.write("(\u0112\3\2\2\2*\u0114\3\2\2\2,\u0116\3\2\2\2.\u0118\3")
        buf.write("\2\2\2\60\u011a\3\2\2\2\62\u0122\3\2\2\2\64\u0128\3\2")
        buf.write("\2\2\66\u012f\3\2\2\28\u013a\3\2\2\2:\u013f\3\2\2\2<\u0144")
        buf.write("\3\2\2\2>\u0146\3\2\2\2@\u0150\3\2\2\2B\u015a\3\2\2\2")
        buf.write("D\u015f\3\2\2\2F\u0161\3\2\2\2H\u0165\3\2\2\2J\u0169\3")
        buf.write("\2\2\2L\u0175\3\2\2\2N\u0177\3\2\2\2P\u0179\3\2\2\2R\u017d")
        buf.write("\3\2\2\2T\u0181\3\2\2\2V\u0185\3\2\2\2XY\5\4\3\2YZ\7\2")
        buf.write("\2\3Z\3\3\2\2\2[\\\5\6\4\2\\]\5\4\3\2]`\3\2\2\2^`\5\6")
        buf.write("\4\2_[\3\2\2\2_^\3\2\2\2`\5\3\2\2\2ad\5\b\5\2bd\5\60\31")
        buf.write("\2ca\3\2\2\2cb\3\2\2\2d\7\3\2\2\2ef\5\"\22\2fg\7+\2\2")
        buf.write("gh\5:\36\2hi\7\33\2\2i\u0097\3\2\2\2jk\7\r\2\2kl\7+\2")
        buf.write("\2lm\5:\36\2mn\7\33\2\2n\u0097\3\2\2\2op\7\16\2\2pq\7")
        buf.write("+\2\2qr\7#\2\2rs\5\f\7\2st\5:\36\2tu\7\33\2\2u\u0097\3")
        buf.write("\2\2\2vw\5\"\22\2wx\7+\2\2xy\7#\2\2yz\5\f\7\2z{\5:\36")
        buf.write("\2{|\7\33\2\2|\u0097\3\2\2\2}~\7\r\2\2~\177\7+\2\2\177")
        buf.write("\u0080\7#\2\2\u0080\u0081\5\f\7\2\u0081\u0082\5:\36\2")
        buf.write("\u0082\u0083\7\33\2\2\u0083\u0097\3\2\2\2\u0084\u0085")
        buf.write("\5\"\22\2\u0085\u0086\7+\2\2\u0086\u0087\7&\2\2\u0087")
        buf.write("\u0088\5\n\6\2\u0088\u0089\7\'\2\2\u0089\u008a\5:\36\2")
        buf.write("\u008a\u008b\7\33\2\2\u008b\u0097\3\2\2\2\u008c\u008d")
        buf.write("\5\"\22\2\u008d\u008e\7+\2\2\u008e\u008f\7&\2\2\u008f")
        buf.write("\u0090\5\n\6\2\u0090\u0091\7\'\2\2\u0091\u0092\7#\2\2")
        buf.write("\u0092\u0093\5\f\7\2\u0093\u0094\5:\36\2\u0094\u0095\7")
        buf.write("\33\2\2\u0095\u0097\3\2\2\2\u0096e\3\2\2\2\u0096j\3\2")
        buf.write("\2\2\u0096o\3\2\2\2\u0096v\3\2\2\2\u0096}\3\2\2\2\u0096")
        buf.write("\u0084\3\2\2\2\u0096\u008c\3\2\2\2\u0097\t\3\2\2\2\u0098")
        buf.write("\u0099\7*\2\2\u0099\u009a\7(\2\2\u009a\u009d\5\n\6\2\u009b")
        buf.write("\u009d\7*\2\2\u009c\u0098\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\13\3\2\2\2\u009e\u009f\b\7\1\2\u009f\u00a0\7$\2")
        buf.write("\2\u00a0\u00a1\5\f\7\2\u00a1\u00a2\7%\2\2\u00a2\u00aa")
        buf.write("\3\2\2\2\u00a3\u00a4\7\26\2\2\u00a4\u00aa\5\f\7\13\u00a5")
        buf.write("\u00a6\7\22\2\2\u00a6\u00aa\5\f\7\n\u00a7\u00aa\5\24\13")
        buf.write("\2\u00a8\u00aa\5$\23\2\u00a9\u009e\3\2\2\2\u00a9\u00a3")
        buf.write("\3\2\2\2\u00a9\u00a5\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\u00c6\3\2\2\2\u00ab\u00ac\f\t\2\2")
        buf.write("\u00ac\u00ad\5&\24\2\u00ad\u00ae\5\f\7\n\u00ae\u00c5\3")
        buf.write("\2\2\2\u00af\u00b0\f\b\2\2\u00b0\u00b1\5(\25\2\u00b1\u00b2")
        buf.write("\5\f\7\t\u00b2\u00c5\3\2\2\2\u00b3\u00b4\f\7\2\2\u00b4")
        buf.write("\u00b5\5*\26\2\u00b5\u00b6\5\f\7\b\u00b6\u00c5\3\2\2\2")
        buf.write("\u00b7\u00b8\f\6\2\2\u00b8\u00b9\5,\27\2\u00b9\u00ba\5")
        buf.write("\f\7\7\u00ba\u00c5\3\2\2\2\u00bb\u00bc\f\5\2\2\u00bc\u00bd")
        buf.write("\5.\30\2\u00bd\u00be\5\f\7\6\u00be\u00c5\3\2\2\2\u00bf")
        buf.write("\u00c0\f\r\2\2\u00c0\u00c1\7&\2\2\u00c1\u00c2\5\22\n\2")
        buf.write("\u00c2\u00c3\7\'\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00ab\3")
        buf.write("\2\2\2\u00c4\u00af\3\2\2\2\u00c4\u00b3\3\2\2\2\u00c4\u00b7")
        buf.write("\3\2\2\2\u00c4\u00bb\3\2\2\2\u00c4\u00bf\3\2\2\2\u00c5")
        buf.write("\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\r\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00cc\5$\23")
        buf.write("\2\u00ca\u00cc\7\26\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\17\3\2\2\2\u00cd\u00d0\5$\23\2\u00ce\u00d0")
        buf.write("\7\22\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\21\3\2\2\2\u00d1\u00d7\5\f\7\2\u00d2\u00d3\5\f\7\2\u00d3")
        buf.write("\u00d4\7(\2\2\u00d4\u00d5\5\22\n\2\u00d5\u00d7\3\2\2\2")
        buf.write("\u00d6\u00d1\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d7\23\3\2")
        buf.write("\2\2\u00d8\u00d9\7+\2\2\u00d9\u00da\7$\2\2\u00da\u00db")
        buf.write("\5\26\f\2\u00db\u00dc\7%\2\2\u00dc\25\3\2\2\2\u00dd\u00e0")
        buf.write("\5\30\r\2\u00de\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00df")
        buf.write("\u00de\3\2\2\2\u00e0\27\3\2\2\2\u00e1\u00e2\5\32\16\2")
        buf.write("\u00e2\u00e3\7(\2\2\u00e3\u00e4\5\30\r\2\u00e4\u00e7\3")
        buf.write("\2\2\2\u00e5\u00e7\5\32\16\2\u00e6\u00e1\3\2\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\31\3\2\2\2\u00e8\u00e9\5\f\7\2\u00e9")
        buf.write("\33\3\2\2\2\u00ea\u00ef\5&\24\2\u00eb\u00ef\5(\25\2\u00ec")
        buf.write("\u00ef\5*\26\2\u00ed\u00ef\5.\30\2\u00ee\u00ea\3\2\2\2")
        buf.write("\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3")
        buf.write("\2\2\2\u00ef\35\3\2\2\2\u00f0\u00f5\5&\24\2\u00f1\u00f5")
        buf.write("\5(\25\2\u00f2\u00f5\5*\26\2\u00f3\u00f5\5,\27\2\u00f4")
        buf.write("\u00f0\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5\37\3\2\2\2\u00f6\u010b\5\24")
        buf.write("\13\2\u00f7\u010b\5$\23\2\u00f8\u00f9\5\24\13\2\u00f9")
        buf.write("\u00fa\7&\2\2\u00fa\u00fb\5\22\n\2\u00fb\u00fc\7\'\2\2")
        buf.write("\u00fc\u010b\3\2\2\2\u00fd\u00fe\5$\23\2\u00fe\u00ff\7")
        buf.write("&\2\2\u00ff\u0100\5\22\n\2\u0100\u0101\7\'\2\2\u0101\u010b")
        buf.write("\3\2\2\2\u0102\u0103\7\26\2\2\u0103\u010b\5\24\13\2\u0104")
        buf.write("\u0105\7\26\2\2\u0105\u010b\5$\23\2\u0106\u0107\7\22\2")
        buf.write("\2\u0107\u010b\5\24\13\2\u0108\u0109\7\22\2\2\u0109\u010b")
        buf.write("\5$\23\2\u010a\u00f6\3\2\2\2\u010a\u00f7\3\2\2\2\u010a")
        buf.write("\u00f8\3\2\2\2\u010a\u00fd\3\2\2\2\u010a\u0102\3\2\2\2")
        buf.write("\u010a\u0104\3\2\2\2\u010a\u0106\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010b!\3\2\2\2\u010c\u010d\t\2\2\2\u010d#\3\2\2")
        buf.write("\2\u010e\u010f\t\3\2\2\u010f%\3\2\2\2\u0110\u0111\t\4")
        buf.write("\2\2\u0111\'\3\2\2\2\u0112\u0113\t\5\2\2\u0113)\3\2\2")
        buf.write("\2\u0114\u0115\t\6\2\2\u0115+\3\2\2\2\u0116\u0117\t\7")
        buf.write("\2\2\u0117-\3\2\2\2\u0118\u0119\7\20\2\2\u0119/\3\2\2")
        buf.write("\2\u011a\u011b\7\3\2\2\u011b\u011c\7+\2\2\u011c\u011d")
        buf.write("\5\62\32\2\u011d\u011e\5:\36\2\u011e\u011f\5<\37\2\u011f")
        buf.write("\u0120\5:\36\2\u0120\u0121\7\33\2\2\u0121\61\3\2\2\2\u0122")
        buf.write("\u0123\7$\2\2\u0123\u0124\5\64\33\2\u0124\u0125\7%\2\2")
        buf.write("\u0125\63\3\2\2\2\u0126\u0129\5\66\34\2\u0127\u0129\3")
        buf.write("\2\2\2\u0128\u0126\3\2\2\2\u0128\u0127\3\2\2\2\u0129\65")
        buf.write("\3\2\2\2\u012a\u012b\58\35\2\u012b\u012c\7(\2\2\u012c")
        buf.write("\u012d\5\66\34\2\u012d\u0130\3\2\2\2\u012e\u0130\58\35")
        buf.write("\2\u012f\u012a\3\2\2\2\u012f\u012e\3\2\2\2\u0130\67\3")
        buf.write("\2\2\2\u0131\u0132\5\"\22\2\u0132\u0133\7+\2\2\u0133\u013b")
        buf.write("\3\2\2\2\u0134\u0135\5\"\22\2\u0135\u0136\7+\2\2\u0136")
        buf.write("\u0137\7&\2\2\u0137\u0138\5\n\6\2\u0138\u0139\7\'\2\2")
        buf.write("\u0139\u013b\3\2\2\2\u013a\u0131\3\2\2\2\u013a\u0134\3")
        buf.write("\2\2\2\u013b9\3\2\2\2\u013c\u013d\7\33\2\2\u013d\u0140")
        buf.write("\5:\36\2\u013e\u0140\3\2\2\2\u013f\u013c\3\2\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140;\3\2\2\2\u0141\u0145\5> \2\u0142")
        buf.write("\u0145\5D#\2\u0143\u0145\3\2\2\2\u0144\u0141\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145=\3\2\2\2\u0146")
        buf.write("\u0147\7\4\2\2\u0147\u0148\5@!\2\u0148\u0149\7\5\2\2\u0149")
        buf.write("\u014a\5:\36\2\u014a\u014b\7\33\2\2\u014b?\3\2\2\2\u014c")
        buf.write("\u014d\5B\"\2\u014d\u014e\5@!\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u0151\3\2\2\2\u0150\u014c\3\2\2\2\u0150\u014f\3\2\2\2")
        buf.write("\u0151A\3\2\2\2\u0152\u015b\5\b\5\2\u0153\u015b\5J&\2")
        buf.write("\u0154\u015b\5P)\2\u0155\u015b\5R*\2\u0156\u015b\5T+\2")
        buf.write("\u0157\u015b\5V,\2\u0158\u015b\5F$\2\u0159\u015b\5H%\2")
        buf.write("\u015a\u0152\3\2\2\2\u015a\u0153\3\2\2\2\u015a\u0154\3")
        buf.write("\2\2\2\u015a\u0155\3\2\2\2\u015a\u0156\3\2\2\2\u015a\u0157")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015b")
        buf.write("C\3\2\2\2\u015c\u015d\7\6\2\2\u015d\u0160\5\f\7\2\u015e")
        buf.write("\u0160\7\6\2\2\u015f\u015c\3\2\2\2\u015f\u015e\3\2\2\2")
        buf.write("\u0160E\3\2\2\2\u0161\u0162\5D#\2\u0162\u0163\5:\36\2")
        buf.write("\u0163\u0164\7\33\2\2\u0164G\3\2\2\2\u0165\u0166\5\24")
        buf.write("\13\2\u0166\u0167\5:\36\2\u0167\u0168\7\33\2\2\u0168I")
        buf.write("\3\2\2\2\u0169\u016a\5L\'\2\u016a\u016b\7#\2\2\u016b\u016c")
        buf.write("\5N(\2\u016c\u016d\5:\36\2\u016d\u016e\7\33\2\2\u016e")
        buf.write("K\3\2\2\2\u016f\u0176\7+\2\2\u0170\u0171\5\f\7\2\u0171")
        buf.write("\u0172\7&\2\2\u0172\u0173\5\22\n\2\u0173\u0174\7\'\2\2")
        buf.write("\u0174\u0176\3\2\2\2\u0175\u016f\3\2\2\2\u0175\u0170\3")
        buf.write("\2\2\2\u0176M\3\2\2\2\u0177\u0178\5\f\7\2\u0178O\3\2\2")
        buf.write("\2\u0179\u017a\7\7\2\2\u017a\u017b\5:\36\2\u017b\u017c")
        buf.write("\7\33\2\2\u017cQ\3\2\2\2\u017d\u017e\7\b\2\2\u017e\u017f")
        buf.write("\5:\36\2\u017f\u0180\7\33\2\2\u0180S\3\2\2\2\u0181\u0182")
        buf.write("\7\t\2\2\u0182\u0183\5:\36\2\u0183\u0184\7\33\2\2\u0184")
        buf.write("U\3\2\2\2\u0185\u0186\7\n\2\2\u0186\u0187\5:\36\2\u0187")
        buf.write("\u0188\7\33\2\2\u0188W\3\2\2\2\32_c\u0096\u009c\u00a9")
        buf.write("\u00c4\u00c6\u00cb\u00cf\u00d6\u00df\u00e6\u00ee\u00f4")
        buf.write("\u010a\u0128\u012f\u013a\u013f\u0144\u0150\u015a\u015f")
        buf.write("\u0175")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'begin'", "'end'", "'return'", 
                     "'if statement'", "'for statement'", "'break statement'", 
                     "'continue statement'", "'string'", "'number'", "'dynamic'", 
                     "'var'", "<INVALID>", "'...'", "'bool'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", 
                     "<INVALID>", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'<-'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING_TYPE", "NUMBER_TYPE", "DYNAMIC_TYPE", 
                      "VAR_TYPE", "COMMENT", "STRING_OPERATOR", "BOOL_TYPE", 
                      "NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", "ADD_OPERATOR", 
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
    RULE_typ = 16
    RULE_literal = 17
    RULE_mul_operators = 18
    RULE_add_operators = 19
    RULE_logic_operators = 20
    RULE_rel_operators = 21
    RULE_str_operators = 22
    RULE_funcdecl = 23
    RULE_param_decl = 24
    RULE_param_decl_list = 25
    RULE_param_decl_prime = 26
    RULE_param_single_decl = 27
    RULE_newline_list = 28
    RULE_body = 29
    RULE_statement_block = 30
    RULE_statement_list = 31
    RULE_statement = 32
    RULE_ret = 33
    RULE_return_statement = 34
    RULE_func_call_statement = 35
    RULE_assignment_statement = 36
    RULE_lhs = 37
    RULE_rhs = 38
    RULE_if_statement = 39
    RULE_for_statement = 40
    RULE_break_statement = 41
    RULE_continue_statement = 42

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "arrlist", 
                   "expression", "sign_operands", "not_operands", "index_operators", 
                   "func_call", "param_list", "param_prime", "param", "non_rel_operators", 
                   "non_str_operators", "non_associative_operands", "typ", 
                   "literal", "mul_operators", "add_operators", "logic_operators", 
                   "rel_operators", "str_operators", "funcdecl", "param_decl", 
                   "param_decl_list", "param_decl_prime", "param_single_decl", 
                   "newline_list", "body", "statement_block", "statement_list", 
                   "statement", "ret", "return_statement", "func_call_statement", 
                   "assignment_statement", "lhs", "rhs", "if_statement", 
                   "for_statement", "break_statement", "continue_statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    STRING_TYPE=9
    NUMBER_TYPE=10
    DYNAMIC_TYPE=11
    VAR_TYPE=12
    COMMENT=13
    STRING_OPERATOR=14
    BOOL_TYPE=15
    NOT_OPERATOR=16
    AND_OPERATOR=17
    OR_OPERATOR=18
    ADD_OPERATOR=19
    SUB_OPERATOR=20
    MUL_OPERATOR=21
    DIV_OPERATOR=22
    MOD_OPERATOR=23
    KEYWORD=24
    NEWLINE=25
    EQ_OPERATOR=26
    NEQ_OPERATOR=27
    LT_OPERATOR=28
    GT_OPERATOR=29
    LEQ_OPERATOR=30
    GEQ_OPERATOR=31
    SEQ_OPERATOR=32
    ASSIGN_OPERATOR=33
    OPEN_PARENTHESIS=34
    CLOSE_PARENTHESIS=35
    OPEN_BRACKET=36
    CLOSE_BRACKET=37
    COMMA=38
    BOOLEAN=39
    NUMBER=40
    IDENTIFIER=41
    STRING=42
    UNCLOSE_STRING=43
    ILLEGAL_ESCAPE=44
    WS=45
    ERROR_CHAR=46

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
            self.state = 86
            self.decllist()
            self.state = 87
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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.decl()
                self.state = 90
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRING_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.DYNAMIC_TYPE, ZCodeParser.VAR_TYPE, ZCodeParser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.vardecl()
                pass
            elif token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.typ()
                self.state = 100
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 101
                self.newline_list()
                self.state = 102
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 105
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 106
                self.newline_list()
                self.state = 107
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(ZCodeParser.VAR_TYPE)
                self.state = 110
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 111
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 112
                self.expression(0)
                self.state = 113
                self.newline_list()
                self.state = 114
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.typ()
                self.state = 117
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 118
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 119
                self.expression(0)
                self.state = 120
                self.newline_list()
                self.state = 121
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 124
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 125
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 126
                self.expression(0)
                self.state = 127
                self.newline_list()
                self.state = 128
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.typ()
                self.state = 131
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 132
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 133
                self.arrlist()
                self.state = 134
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 135
                self.newline_list()
                self.state = 136
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 138
                self.typ()
                self.state = 139
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 140
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 141
                self.arrlist()
                self.state = 142
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 143
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.newline_list()
                self.state = 146
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
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(ZCodeParser.NUMBER)
                self.state = 151
                self.match(ZCodeParser.COMMA)
                self.state = 152
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 157
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 158
                self.expression(0)
                self.state = 159
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 2:
                self.state = 161
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 162
                self.expression(9)
                pass

            elif la_ == 3:
                self.state = 163
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 164
                self.expression(8)
                pass

            elif la_ == 4:
                self.state = 165
                self.func_call()
                pass

            elif la_ == 5:
                self.state = 166
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 170
                        self.mul_operators()
                        self.state = 171
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 174
                        self.add_operators()
                        self.state = 175
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 177
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 178
                        self.logic_operators()
                        self.state = 179
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 182
                        self.rel_operators()
                        self.state = 183
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 186
                        self.str_operators()
                        self.state = 187
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 190
                        self.match(ZCodeParser.OPEN_BRACKET)
                        self.state = 191
                        self.index_operators()
                        self.state = 192
                        self.match(ZCodeParser.CLOSE_BRACKET)
                        pass

             
                self.state = 198
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_operands" ):
                return visitor.visitSign_operands(self)
            else:
                return visitor.visitChildren(self)




    def sign_operands(self):

        localctx = ZCodeParser.Sign_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sign_operands)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.literal()
                pass
            elif token in [ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_operands" ):
                return visitor.visitNot_operands(self)
            else:
                return visitor.visitChildren(self)




    def not_operands(self):

        localctx = ZCodeParser.Not_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_not_operands)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.literal()
                pass
            elif token in [ZCodeParser.NOT_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_index_operators)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.expression(0)
                self.state = 209
                self.match(ZCodeParser.COMMA)
                self.state = 210
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 215
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 216
            self.param_list()
            self.state = 217
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_list)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OPERATOR, ZCodeParser.SUB_OPERATOR, ZCodeParser.OPEN_PARENTHESIS, ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.param_prime()
                pass
            elif token in [ZCodeParser.CLOSE_PARENTHESIS]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_prime" ):
                return visitor.visitParam_prime(self)
            else:
                return visitor.visitChildren(self)




    def param_prime(self):

        localctx = ZCodeParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_prime)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.param()
                self.state = 224
                self.match(ZCodeParser.COMMA)
                self.state = 225
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_rel_operators" ):
                return visitor.visitNon_rel_operators(self)
            else:
                return visitor.visitChildren(self)




    def non_rel_operators(self):

        localctx = ZCodeParser.Non_rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_non_rel_operators)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MUL_OPERATOR, ZCodeParser.DIV_OPERATOR, ZCodeParser.MOD_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.mul_operators()
                pass
            elif token in [ZCodeParser.ADD_OPERATOR, ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.add_operators()
                pass
            elif token in [ZCodeParser.AND_OPERATOR, ZCodeParser.OR_OPERATOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.logic_operators()
                pass
            elif token in [ZCodeParser.STRING_OPERATOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_str_operators" ):
                return visitor.visitNon_str_operators(self)
            else:
                return visitor.visitChildren(self)




    def non_str_operators(self):

        localctx = ZCodeParser.Non_str_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_non_str_operators)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MUL_OPERATOR, ZCodeParser.DIV_OPERATOR, ZCodeParser.MOD_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.mul_operators()
                pass
            elif token in [ZCodeParser.ADD_OPERATOR, ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.add_operators()
                pass
            elif token in [ZCodeParser.AND_OPERATOR, ZCodeParser.OR_OPERATOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.logic_operators()
                pass
            elif token in [ZCodeParser.EQ_OPERATOR, ZCodeParser.NEQ_OPERATOR, ZCodeParser.LT_OPERATOR, ZCodeParser.GT_OPERATOR, ZCodeParser.LEQ_OPERATOR, ZCodeParser.GEQ_OPERATOR, ZCodeParser.SEQ_OPERATOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_associative_operands" ):
                return visitor.visitNon_associative_operands(self)
            else:
                return visitor.visitChildren(self)




    def non_associative_operands(self):

        localctx = ZCodeParser.Non_associative_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_non_associative_operands)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.func_call()
                self.state = 247
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 248
                self.index_operators()
                self.state = 249
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.literal()
                self.state = 252
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 253
                self.index_operators()
                self.state = 254
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 257
                self.func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 259
                self.literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 260
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 261
                self.func_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 262
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 263
                self.literal()
                pass


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
        self.enterRule(localctx, 32, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.STRING_TYPE) | (1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.BOOL_TYPE))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.STRING))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_operators" ):
                return visitor.visitMul_operators(self)
            else:
                return visitor.visitChildren(self)




    def mul_operators(self):

        localctx = ZCodeParser.Mul_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_mul_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OPERATOR) | (1 << ZCodeParser.DIV_OPERATOR) | (1 << ZCodeParser.MOD_OPERATOR))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_operators" ):
                return visitor.visitAdd_operators(self)
            else:
                return visitor.visitChildren(self)




    def add_operators(self):

        localctx = ZCodeParser.Add_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_add_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.ADD_OPERATOR or _la==ZCodeParser.SUB_OPERATOR):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_operators" ):
                return visitor.visitLogic_operators(self)
            else:
                return visitor.visitChildren(self)




    def logic_operators(self):

        localctx = ZCodeParser.Logic_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.AND_OPERATOR or _la==ZCodeParser.OR_OPERATOR):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_operators" ):
                return visitor.visitRel_operators(self)
            else:
                return visitor.visitChildren(self)




    def rel_operators(self):

        localctx = ZCodeParser.Rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_rel_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ_OPERATOR) | (1 << ZCodeParser.NEQ_OPERATOR) | (1 << ZCodeParser.LT_OPERATOR) | (1 << ZCodeParser.GT_OPERATOR) | (1 << ZCodeParser.LEQ_OPERATOR) | (1 << ZCodeParser.GEQ_OPERATOR) | (1 << ZCodeParser.SEQ_OPERATOR))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_operators" ):
                return visitor.visitStr_operators(self)
            else:
                return visitor.visitChildren(self)




    def str_operators(self):

        localctx = ZCodeParser.Str_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_str_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.STRING_OPERATOR)
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


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
        self.enterRule(localctx, 46, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ZCodeParser.T__0)
            self.state = 281
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 282
            self.param_decl()
            self.state = 283
            self.newline_list()
            self.state = 284
            self.body()
            self.state = 285
            self.newline_list()
            self.state = 286
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(ZCodeParser.OPEN_PARENTHESIS, 0)

        def param_decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_listContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSE_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = ZCodeParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 289
            self.param_decl_list()
            self.state = 290
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_list" ):
                return visitor.visitParam_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_list(self):

        localctx = ZCodeParser.Param_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_param_decl_list)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRING_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.param_decl_prime()
                pass
            elif token in [ZCodeParser.CLOSE_PARENTHESIS]:
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


    class Param_decl_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_single_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_single_declContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_decl_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_prime" ):
                return visitor.visitParam_decl_prime(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_prime(self):

        localctx = ZCodeParser.Param_decl_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_param_decl_prime)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.param_single_decl()
                self.state = 297
                self.match(ZCodeParser.COMMA)
                self.state = 298
                self.param_decl_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.param_single_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_single_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_single_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_single_decl" ):
                return visitor.visitParam_single_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_single_decl(self):

        localctx = ZCodeParser.Param_single_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_param_single_decl)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.typ()
                self.state = 304
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.typ()
                self.state = 307
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 308
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 309
                self.arrlist()
                self.state = 310
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_newline_list)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(ZCodeParser.NEWLINE)
                self.state = 315
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_block(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_blockContext,0)


        def ret(self):
            return self.getTypedRuleContext(ZCodeParser.RetContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_body)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.statement_block()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.ret()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)

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


    class Statement_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_block" ):
                return visitor.visitStatement_block(self)
            else:
                return visitor.visitChildren(self)




    def statement_block(self):

        localctx = ZCodeParser.Statement_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.T__1)
            self.state = 325
            self.statement_list()
            self.state = 326
            self.match(ZCodeParser.T__2)
            self.state = 327
            self.newline_list()
            self.state = 328
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statement_list)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.T__6, ZCodeParser.T__7, ZCodeParser.STRING_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.DYNAMIC_TYPE, ZCodeParser.VAR_TYPE, ZCodeParser.BOOL_TYPE, ZCodeParser.NOT_OPERATOR, ZCodeParser.SUB_OPERATOR, ZCodeParser.OPEN_PARENTHESIS, ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.statement()
                self.state = 331
                self.statement_list()
                pass
            elif token in [ZCodeParser.T__2]:
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def func_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 339
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 340
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 341
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 342
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 343
                self.func_call_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ret

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = ZCodeParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ret)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(ZCodeParser.T__3)
                self.state = 347
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(ZCodeParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ret(self):
            return self.getTypedRuleContext(ZCodeParser.RetContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.ret()
            self.state = 352
            self.newline_list()
            self.state = 353
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_statement" ):
                return visitor.visitFunc_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def func_call_statement(self):

        localctx = ZCodeParser.Func_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_func_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.func_call()
            self.state = 356
            self.newline_list()
            self.state = 357
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN_OPERATOR, 0)

        def rhs(self):
            return self.getTypedRuleContext(ZCodeParser.RhsContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.lhs()
            self.state = 360
            self.match(ZCodeParser.ASSIGN_OPERATOR)
            self.state = 361
            self.rhs()
            self.state = 362
            self.newline_list()
            self.state = 363
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_lhs)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.expression(0)
                self.state = 367
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 368
                self.index_operators()
                self.state = 369
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = ZCodeParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(ZCodeParser.T__4)
            self.state = 376
            self.newline_list()
            self.state = 377
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ZCodeParser.T__5)
            self.state = 380
            self.newline_list()
            self.state = 381
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(ZCodeParser.T__6)
            self.state = 384
            self.newline_list()
            self.state = 385
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(ZCodeParser.T__7)
            self.state = 388
            self.newline_list()
            self.state = 389
            self.match(ZCodeParser.NEWLINE)
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
         




