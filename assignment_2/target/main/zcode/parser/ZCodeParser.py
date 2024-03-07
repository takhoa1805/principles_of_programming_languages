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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01e7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3u\n\3\3\4\3\4\5\4y\n\4\3\5\3\5\5\5}\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u0090\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00b1\n\7\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u00b7\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u00be\n")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c7\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00cf\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00d6\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e8\n\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0103\n\r\f\r\16")
        buf.write("\r\u0106\13\r\3\16\3\16\5\16\u010a\n\16\3\17\3\17\5\17")
        buf.write("\u010e\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u0115\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\5\22\u011e\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u0125\n\23\3\24\3\24\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u012d\n\25\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u0133\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0149\n\27\3\30\3\30\3\31\3\31\3\32\3\32\3")
        buf.write("\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \5 \u0164\n \3!\3")
        buf.write("!\3!\3!\3!\5!\u016b\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u0176\n\"\3#\3#\3#\5#\u017b\n#\3$\3$\3$\5$\u0180")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\5&\u018e\n&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0199\n\'\3(\3")
        buf.write("(\3(\5(\u019e\n(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\5")
        buf.write("/\u01be\n/\3\60\3\60\3\60\3\60\5\60\u01c4\n\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\5\62\u01cf\n\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\5\64\u01dd\n\64\3\65\3\65\3\65\3\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\2\3\30\67\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhj\2\b\4\2\3\4\26\26\3\2-\60\3\2\34\36\3\2\32\33\3\2")
        buf.write("\30\31\3\2 &\2\u01f1\2l\3\2\2\2\4t\3\2\2\2\6x\3\2\2\2")
        buf.write("\b|\3\2\2\2\n\u008f\3\2\2\2\f\u00b0\3\2\2\2\16\u00b6\3")
        buf.write("\2\2\2\20\u00bd\3\2\2\2\22\u00c6\3\2\2\2\24\u00ce\3\2")
        buf.write("\2\2\26\u00d5\3\2\2\2\30\u00e7\3\2\2\2\32\u0109\3\2\2")
        buf.write("\2\34\u010d\3\2\2\2\36\u0114\3\2\2\2 \u0116\3\2\2\2\"")
        buf.write("\u011d\3\2\2\2$\u0124\3\2\2\2&\u0126\3\2\2\2(\u012c\3")
        buf.write("\2\2\2*\u0132\3\2\2\2,\u0148\3\2\2\2.\u014a\3\2\2\2\60")
        buf.write("\u014c\3\2\2\2\62\u014e\3\2\2\2\64\u0150\3\2\2\2\66\u0152")
        buf.write("\3\2\2\28\u0154\3\2\2\2:\u0156\3\2\2\2<\u0158\3\2\2\2")
        buf.write(">\u0163\3\2\2\2@\u016a\3\2\2\2B\u0175\3\2\2\2D\u017a\3")
        buf.write("\2\2\2F\u017f\3\2\2\2H\u0181\3\2\2\2J\u018d\3\2\2\2L\u0198")
        buf.write("\3\2\2\2N\u019d\3\2\2\2P\u019f\3\2\2\2R\u01a3\3\2\2\2")
        buf.write("T\u01a7\3\2\2\2V\u01ad\3\2\2\2X\u01af\3\2\2\2Z\u01b1\3")
        buf.write("\2\2\2\\\u01bd\3\2\2\2^\u01c3\3\2\2\2`\u01c5\3\2\2\2b")
        buf.write("\u01ce\3\2\2\2d\u01d0\3\2\2\2f\u01dc\3\2\2\2h\u01de\3")
        buf.write("\2\2\2j\u01e2\3\2\2\2lm\5D#\2mn\5\4\3\2no\7\2\2\3o\3\3")
        buf.write("\2\2\2pq\5\6\4\2qr\5\4\3\2ru\3\2\2\2su\5\6\4\2tp\3\2\2")
        buf.write("\2ts\3\2\2\2u\5\3\2\2\2vy\5\b\5\2wy\5<\37\2xv\3\2\2\2")
        buf.write("xw\3\2\2\2y\7\3\2\2\2z}\5\n\6\2{}\5\f\7\2|z\3\2\2\2|{")
        buf.write("\3\2\2\2}\t\3\2\2\2~\177\5.\30\2\177\u0080\7/\2\2\u0080")
        buf.write("\u0081\7\37\2\2\u0081\u0082\5D#\2\u0082\u0090\3\2\2\2")
        buf.write("\u0083\u0084\7\5\2\2\u0084\u0085\7/\2\2\u0085\u0086\7")
        buf.write("\37\2\2\u0086\u0090\5D#\2\u0087\u0088\5.\30\2\u0088\u0089")
        buf.write("\7/\2\2\u0089\u008a\7*\2\2\u008a\u008b\5\16\b\2\u008b")
        buf.write("\u008c\7+\2\2\u008c\u008d\7\37\2\2\u008d\u008e\5D#\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f~\3\2\2\2\u008f\u0083\3\2\2\2\u008f")
        buf.write("\u0087\3\2\2\2\u0090\13\3\2\2\2\u0091\u0092\7\6\2\2\u0092")
        buf.write("\u0093\7/\2\2\u0093\u0094\7\'\2\2\u0094\u0095\5\30\r\2")
        buf.write("\u0095\u0096\7\37\2\2\u0096\u0097\5D#\2\u0097\u00b1\3")
        buf.write("\2\2\2\u0098\u0099\5.\30\2\u0099\u009a\7/\2\2\u009a\u009b")
        buf.write("\7\'\2\2\u009b\u009c\5\30\r\2\u009c\u009d\7\37\2\2\u009d")
        buf.write("\u009e\5D#\2\u009e\u00b1\3\2\2\2\u009f\u00a0\7\5\2\2\u00a0")
        buf.write("\u00a1\7/\2\2\u00a1\u00a2\7\'\2\2\u00a2\u00a3\5\30\r\2")
        buf.write("\u00a3\u00a4\7\37\2\2\u00a4\u00a5\5D#\2\u00a5\u00b1\3")
        buf.write("\2\2\2\u00a6\u00a7\5.\30\2\u00a7\u00a8\7/\2\2\u00a8\u00a9")
        buf.write("\7*\2\2\u00a9\u00aa\5\16\b\2\u00aa\u00ab\7+\2\2\u00ab")
        buf.write("\u00ac\7\'\2\2\u00ac\u00ad\5\30\r\2\u00ad\u00ae\7\37\2")
        buf.write("\2\u00ae\u00af\5D#\2\u00af\u00b1\3\2\2\2\u00b0\u0091\3")
        buf.write("\2\2\2\u00b0\u0098\3\2\2\2\u00b0\u009f\3\2\2\2\u00b0\u00a6")
        buf.write("\3\2\2\2\u00b1\r\3\2\2\2\u00b2\u00b3\7.\2\2\u00b3\u00b4")
        buf.write("\7,\2\2\u00b4\u00b7\5\16\b\2\u00b5\u00b7\7.\2\2\u00b6")
        buf.write("\u00b2\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\17\3\2\2\2\u00b8")
        buf.write("\u00b9\7*\2\2\u00b9\u00ba\5\16\b\2\u00ba\u00bb\7+\2\2")
        buf.write("\u00bb\u00be\3\2\2\2\u00bc\u00be\5\16\b\2\u00bd\u00b8")
        buf.write("\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\21\3\2\2\2\u00bf\u00c0")
        buf.write("\7*\2\2\u00c0\u00c1\5\20\t\2\u00c1\u00c2\7,\2\2\u00c2")
        buf.write("\u00c3\5\22\n\2\u00c3\u00c4\7+\2\2\u00c4\u00c7\3\2\2\2")
        buf.write("\u00c5\u00c7\5\20\t\2\u00c6\u00bf\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\23\3\2\2\2\u00c8\u00c9\7*\2\2\u00c9\u00ca")
        buf.write("\5\26\f\2\u00ca\u00cb\7+\2\2\u00cb\u00cf\3\2\2\2\u00cc")
        buf.write("\u00cd\7*\2\2\u00cd\u00cf\7+\2\2\u00ce\u00c8\3\2\2\2\u00ce")
        buf.write("\u00cc\3\2\2\2\u00cf\25\3\2\2\2\u00d0\u00d1\5\30\r\2\u00d1")
        buf.write("\u00d2\7,\2\2\u00d2\u00d3\5\26\f\2\u00d3\u00d6\3\2\2\2")
        buf.write("\u00d4\u00d6\5\30\r\2\u00d5\u00d0\3\2\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\27\3\2\2\2\u00d7\u00d8\b\r\1\2\u00d8\u00d9")
        buf.write("\7(\2\2\u00d9\u00da\5\30\r\2\u00da\u00db\7)\2\2\u00db")
        buf.write("\u00e8\3\2\2\2\u00dc\u00dd\7\33\2\2\u00dd\u00e8\5\30\r")
        buf.write("\f\u00de\u00df\7\27\2\2\u00df\u00e8\5\30\r\13\u00e0\u00e1")
        buf.write("\7/\2\2\u00e1\u00e2\7(\2\2\u00e2\u00e3\5\"\22\2\u00e3")
        buf.write("\u00e4\7)\2\2\u00e4\u00e8\3\2\2\2\u00e5\u00e8\5\60\31")
        buf.write("\2\u00e6\u00e8\5\24\13\2\u00e7\u00d7\3\2\2\2\u00e7\u00dc")
        buf.write("\3\2\2\2\u00e7\u00de\3\2\2\2\u00e7\u00e0\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\u0104\3\2\2\2")
        buf.write("\u00e9\u00ea\f\n\2\2\u00ea\u00eb\5\62\32\2\u00eb\u00ec")
        buf.write("\5\30\r\13\u00ec\u0103\3\2\2\2\u00ed\u00ee\f\t\2\2\u00ee")
        buf.write("\u00ef\5\64\33\2\u00ef\u00f0\5\30\r\n\u00f0\u0103\3\2")
        buf.write("\2\2\u00f1\u00f2\f\b\2\2\u00f2\u00f3\5\66\34\2\u00f3\u00f4")
        buf.write("\5\30\r\t\u00f4\u0103\3\2\2\2\u00f5\u00f6\f\7\2\2\u00f6")
        buf.write("\u00f7\58\35\2\u00f7\u00f8\5\30\r\b\u00f8\u0103\3\2\2")
        buf.write("\2\u00f9\u00fa\f\6\2\2\u00fa\u00fb\5:\36\2\u00fb\u00fc")
        buf.write("\5\30\r\7\u00fc\u0103\3\2\2\2\u00fd\u00fe\f\16\2\2\u00fe")
        buf.write("\u00ff\7*\2\2\u00ff\u0100\5\36\20\2\u0100\u0101\7+\2\2")
        buf.write("\u0101\u0103\3\2\2\2\u0102\u00e9\3\2\2\2\u0102\u00ed\3")
        buf.write("\2\2\2\u0102\u00f1\3\2\2\2\u0102\u00f5\3\2\2\2\u0102\u00f9")
        buf.write("\3\2\2\2\u0102\u00fd\3\2\2\2\u0103\u0106\3\2\2\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\31\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0107\u010a\5\60\31\2\u0108\u010a\7\33")
        buf.write("\2\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a\33")
        buf.write("\3\2\2\2\u010b\u010e\5\60\31\2\u010c\u010e\7\27\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010d\u010c\3\2\2\2\u010e\35\3\2\2\2\u010f")
        buf.write("\u0115\5\30\r\2\u0110\u0111\5\30\r\2\u0111\u0112\7,\2")
        buf.write("\2\u0112\u0113\5\36\20\2\u0113\u0115\3\2\2\2\u0114\u010f")
        buf.write("\3\2\2\2\u0114\u0110\3\2\2\2\u0115\37\3\2\2\2\u0116\u0117")
        buf.write("\7/\2\2\u0117\u0118\7(\2\2\u0118\u0119\5\"\22\2\u0119")
        buf.write("\u011a\7)\2\2\u011a!\3\2\2\2\u011b\u011e\5$\23\2\u011c")
        buf.write("\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2")
        buf.write("\u011e#\3\2\2\2\u011f\u0120\5&\24\2\u0120\u0121\7,\2\2")
        buf.write("\u0121\u0122\5$\23\2\u0122\u0125\3\2\2\2\u0123\u0125\5")
        buf.write("&\24\2\u0124\u011f\3\2\2\2\u0124\u0123\3\2\2\2\u0125%")
        buf.write("\3\2\2\2\u0126\u0127\5\30\r\2\u0127\'\3\2\2\2\u0128\u012d")
        buf.write("\5\62\32\2\u0129\u012d\5\64\33\2\u012a\u012d\5\66\34\2")
        buf.write("\u012b\u012d\5:\36\2\u012c\u0128\3\2\2\2\u012c\u0129\3")
        buf.write("\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d)")
        buf.write("\3\2\2\2\u012e\u0133\5\62\32\2\u012f\u0133\5\64\33\2\u0130")
        buf.write("\u0133\5\66\34\2\u0131\u0133\58\35\2\u0132\u012e\3\2\2")
        buf.write("\2\u0132\u012f\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0131")
        buf.write("\3\2\2\2\u0133+\3\2\2\2\u0134\u0149\5 \21\2\u0135\u0149")
        buf.write("\5\60\31\2\u0136\u0137\5 \21\2\u0137\u0138\7*\2\2\u0138")
        buf.write("\u0139\5\36\20\2\u0139\u013a\7+\2\2\u013a\u0149\3\2\2")
        buf.write("\2\u013b\u013c\5\60\31\2\u013c\u013d\7*\2\2\u013d\u013e")
        buf.write("\5\36\20\2\u013e\u013f\7+\2\2\u013f\u0149\3\2\2\2\u0140")
        buf.write("\u0141\7\33\2\2\u0141\u0149\5 \21\2\u0142\u0143\7\33\2")
        buf.write("\2\u0143\u0149\5\60\31\2\u0144\u0145\7\27\2\2\u0145\u0149")
        buf.write("\5 \21\2\u0146\u0147\7\27\2\2\u0147\u0149\5\60\31\2\u0148")
        buf.write("\u0134\3\2\2\2\u0148\u0135\3\2\2\2\u0148\u0136\3\2\2\2")
        buf.write("\u0148\u013b\3\2\2\2\u0148\u0140\3\2\2\2\u0148\u0142\3")
        buf.write("\2\2\2\u0148\u0144\3\2\2\2\u0148\u0146\3\2\2\2\u0149-")
        buf.write("\3\2\2\2\u014a\u014b\t\2\2\2\u014b/\3\2\2\2\u014c\u014d")
        buf.write("\t\3\2\2\u014d\61\3\2\2\2\u014e\u014f\t\4\2\2\u014f\63")
        buf.write("\3\2\2\2\u0150\u0151\t\5\2\2\u0151\65\3\2\2\2\u0152\u0153")
        buf.write("\t\6\2\2\u0153\67\3\2\2\2\u0154\u0155\t\7\2\2\u01559\3")
        buf.write("\2\2\2\u0156\u0157\7\25\2\2\u0157;\3\2\2\2\u0158\u0159")
        buf.write("\7\n\2\2\u0159\u015a\7/\2\2\u015a\u015b\7(\2\2\u015b\u015c")
        buf.write("\5> \2\u015c\u015d\7)\2\2\u015d\u015e\5D#\2\u015e\u015f")
        buf.write("\5F$\2\u015f\u0160\5D#\2\u0160=\3\2\2\2\u0161\u0164\5")
        buf.write("@!\2\u0162\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164?\3\2\2\2\u0165\u0166\5B\"\2\u0166\u0167")
        buf.write("\7,\2\2\u0167\u0168\5@!\2\u0168\u016b\3\2\2\2\u0169\u016b")
        buf.write("\5B\"\2\u016a\u0165\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("A\3\2\2\2\u016c\u016d\5.\30\2\u016d\u016e\7/\2\2\u016e")
        buf.write("\u0176\3\2\2\2\u016f\u0170\5.\30\2\u0170\u0171\7/\2\2")
        buf.write("\u0171\u0172\7*\2\2\u0172\u0173\5\16\b\2\u0173\u0174\7")
        buf.write("+\2\2\u0174\u0176\3\2\2\2\u0175\u016c\3\2\2\2\u0175\u016f")
        buf.write("\3\2\2\2\u0176C\3\2\2\2\u0177\u0178\7\37\2\2\u0178\u017b")
        buf.write("\5D#\2\u0179\u017b\3\2\2\2\u017a\u0177\3\2\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017bE\3\2\2\2\u017c\u0180\5H%\2\u017d\u0180")
        buf.write("\5N(\2\u017e\u0180\3\2\2\2\u017f\u017c\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u017e\3\2\2\2\u0180G\3\2\2\2\u0181\u0182")
        buf.write("\7\13\2\2\u0182\u0183\5J&\2\u0183\u0184\7\f\2\2\u0184")
        buf.write("\u0185\7\37\2\2\u0185\u0186\5D#\2\u0186I\3\2\2\2\u0187")
        buf.write("\u0188\5D#\2\u0188\u0189\5L\'\2\u0189\u018a\5D#\2\u018a")
        buf.write("\u018b\5J&\2\u018b\u018e\3\2\2\2\u018c\u018e\5D#\2\u018d")
        buf.write("\u0187\3\2\2\2\u018d\u018c\3\2\2\2\u018eK\3\2\2\2\u018f")
        buf.write("\u0199\5\b\5\2\u0190\u0199\5T+\2\u0191\u0199\5Z.\2\u0192")
        buf.write("\u0199\5d\63\2\u0193\u0199\5h\65\2\u0194\u0199\5j\66\2")
        buf.write("\u0195\u0199\5P)\2\u0196\u0199\5R*\2\u0197\u0199\5H%\2")
        buf.write("\u0198\u018f\3\2\2\2\u0198\u0190\3\2\2\2\u0198\u0191\3")
        buf.write("\2\2\2\u0198\u0192\3\2\2\2\u0198\u0193\3\2\2\2\u0198\u0194")
        buf.write("\3\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199M\3\2\2\2\u019a\u019b\7\r\2\2\u019b")
        buf.write("\u019e\5\30\r\2\u019c\u019e\7\r\2\2\u019d\u019a\3\2\2")
        buf.write("\2\u019d\u019c\3\2\2\2\u019eO\3\2\2\2\u019f\u01a0\5N(")
        buf.write("\2\u01a0\u01a1\7\37\2\2\u01a1\u01a2\5D#\2\u01a2Q\3\2\2")
        buf.write("\2\u01a3\u01a4\5 \21\2\u01a4\u01a5\7\37\2\2\u01a5\u01a6")
        buf.write("\5D#\2\u01a6S\3\2\2\2\u01a7\u01a8\5V,\2\u01a8\u01a9\7")
        buf.write("\'\2\2\u01a9\u01aa\5X-\2\u01aa\u01ab\7\37\2\2\u01ab\u01ac")
        buf.write("\5D#\2\u01acU\3\2\2\2\u01ad\u01ae\5\30\r\2\u01aeW\3\2")
        buf.write("\2\2\u01af\u01b0\5\30\r\2\u01b0Y\3\2\2\2\u01b1\u01b2\7")
        buf.write("\16\2\2\u01b2\u01b3\7(\2\2\u01b3\u01b4\5\30\r\2\u01b4")
        buf.write("\u01b5\7)\2\2\u01b5\u01b6\5\\/\2\u01b6\u01b7\5^\60\2\u01b7")
        buf.write("\u01b8\5b\62\2\u01b8\u01b9\5D#\2\u01b9[\3\2\2\2\u01ba")
        buf.write("\u01be\5L\'\2\u01bb\u01be\5H%\2\u01bc\u01be\7\37\2\2\u01bd")
        buf.write("\u01ba\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be]\3\2\2\2\u01bf\u01c0\5`\61\2\u01c0\u01c1\5^\60")
        buf.write("\2\u01c1\u01c4\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01bf")
        buf.write("\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4_\3\2\2\2\u01c5\u01c6")
        buf.write("\7\17\2\2\u01c6\u01c7\7(\2\2\u01c7\u01c8\5\30\r\2\u01c8")
        buf.write("\u01c9\7)\2\2\u01c9\u01ca\5\\/\2\u01caa\3\2\2\2\u01cb")
        buf.write("\u01cc\7\20\2\2\u01cc\u01cf\5\\/\2\u01cd\u01cf\3\2\2\2")
        buf.write("\u01ce\u01cb\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cfc\3\2\2")
        buf.write("\2\u01d0\u01d1\7\21\2\2\u01d1\u01d2\7/\2\2\u01d2\u01d3")
        buf.write("\7\22\2\2\u01d3\u01d4\5\30\r\2\u01d4\u01d5\7\23\2\2\u01d5")
        buf.write("\u01d6\5\30\r\2\u01d6\u01d7\5D#\2\u01d7\u01d8\5f\64\2")
        buf.write("\u01d8e\3\2\2\2\u01d9\u01dd\5L\'\2\u01da\u01dd\5H%\2\u01db")
        buf.write("\u01dd\7\37\2\2\u01dc\u01d9\3\2\2\2\u01dc\u01da\3\2\2")
        buf.write("\2\u01dc\u01db\3\2\2\2\u01ddg\3\2\2\2\u01de\u01df\7\b")
        buf.write("\2\2\u01df\u01e0\7\37\2\2\u01e0\u01e1\5D#\2\u01e1i\3\2")
        buf.write("\2\2\u01e2\u01e3\7\t\2\2\u01e3\u01e4\7\37\2\2\u01e4\u01e5")
        buf.write("\5D#\2\u01e5k\3\2\2\2#tx|\u008f\u00b0\u00b6\u00bd\u00c6")
        buf.write("\u00ce\u00d5\u00e7\u0102\u0104\u0109\u010d\u0114\u011d")
        buf.write("\u0124\u012c\u0132\u0148\u0163\u016a\u0175\u017a\u017f")
        buf.write("\u018d\u0198\u019d\u01bd\u01c3\u01ce\u01dc")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'string'", "'number'", "'dynamic'", "'var'", 
                     "'for statement'", "'break'", "'continue'", "'func'", 
                     "'begin'", "'end'", "'return'", "'if'", "'elif'", "'else'", 
                     "'for'", "'until'", "'by'", "<INVALID>", "'...'", "'bool'", 
                     "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "<INVALID>", "'='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'<-'", "'('", "')'", "'['", "']'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "STRING_TYPE", "NUMBER_TYPE", "DYNAMIC_TYPE", 
                      "VAR_TYPE", "FOR_STATEMENT", "BREAK_STATEMENT", "CONTINUE_STATEMENT", 
                      "FUNC", "BEGIN", "END", "RETURN", "IF", "ELIF", "ELSE", 
                      "FOR", "UNTIL", "BY", "COMMENT", "STRING_OPERATOR", 
                      "BOOL_TYPE", "NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", 
                      "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", 
                      "MOD_OPERATOR", "NEWLINE", "EQ_OPERATOR", "NEQ_OPERATOR", 
                      "LT_OPERATOR", "GT_OPERATOR", "LEQ_OPERATOR", "GEQ_OPERATOR", 
                      "SEQ_OPERATOR", "ASSIGN_OPERATOR", "OPEN_PARENTHESIS", 
                      "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", 
                      "COMMA", "BOOLEAN", "NUMBER", "IDENTIFIER", "STRING", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_vardecl_only = 4
    RULE_vardecl_init = 5
    RULE_arrlist = 6
    RULE_array_expression = 7
    RULE_arrlist_expression = 8
    RULE_array_literal = 9
    RULE_array_literal_prime = 10
    RULE_expression = 11
    RULE_sign_operands = 12
    RULE_not_operands = 13
    RULE_index_operators = 14
    RULE_func_call = 15
    RULE_param_list = 16
    RULE_param_prime = 17
    RULE_param = 18
    RULE_non_rel_operators = 19
    RULE_non_str_operators = 20
    RULE_non_associative_operands = 21
    RULE_typ = 22
    RULE_literal = 23
    RULE_mul_operators = 24
    RULE_add_operators = 25
    RULE_logic_operators = 26
    RULE_rel_operators = 27
    RULE_str_operators = 28
    RULE_funcdecl = 29
    RULE_param_decl_list = 30
    RULE_param_decl_prime = 31
    RULE_param_single_decl = 32
    RULE_newline_list = 33
    RULE_body = 34
    RULE_statement_block = 35
    RULE_statement_list = 36
    RULE_statement = 37
    RULE_ret = 38
    RULE_return_statement = 39
    RULE_func_call_statement = 40
    RULE_assignment_statement = 41
    RULE_lhs = 42
    RULE_rhs = 43
    RULE_if_statement = 44
    RULE_if_body = 45
    RULE_elif_statement_list = 46
    RULE_elif_statement = 47
    RULE_else_statement = 48
    RULE_for_statement = 49
    RULE_for_body = 50
    RULE_break_statement = 51
    RULE_continue_statement = 52

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "vardecl_only", 
                   "vardecl_init", "arrlist", "array_expression", "arrlist_expression", 
                   "array_literal", "array_literal_prime", "expression", 
                   "sign_operands", "not_operands", "index_operators", "func_call", 
                   "param_list", "param_prime", "param", "non_rel_operators", 
                   "non_str_operators", "non_associative_operands", "typ", 
                   "literal", "mul_operators", "add_operators", "logic_operators", 
                   "rel_operators", "str_operators", "funcdecl", "param_decl_list", 
                   "param_decl_prime", "param_single_decl", "newline_list", 
                   "body", "statement_block", "statement_list", "statement", 
                   "ret", "return_statement", "func_call_statement", "assignment_statement", 
                   "lhs", "rhs", "if_statement", "if_body", "elif_statement_list", 
                   "elif_statement", "else_statement", "for_statement", 
                   "for_body", "break_statement", "continue_statement" ]

    EOF = Token.EOF
    STRING_TYPE=1
    NUMBER_TYPE=2
    DYNAMIC_TYPE=3
    VAR_TYPE=4
    FOR_STATEMENT=5
    BREAK_STATEMENT=6
    CONTINUE_STATEMENT=7
    FUNC=8
    BEGIN=9
    END=10
    RETURN=11
    IF=12
    ELIF=13
    ELSE=14
    FOR=15
    UNTIL=16
    BY=17
    COMMENT=18
    STRING_OPERATOR=19
    BOOL_TYPE=20
    NOT_OPERATOR=21
    AND_OPERATOR=22
    OR_OPERATOR=23
    ADD_OPERATOR=24
    SUB_OPERATOR=25
    MUL_OPERATOR=26
    DIV_OPERATOR=27
    MOD_OPERATOR=28
    NEWLINE=29
    EQ_OPERATOR=30
    NEQ_OPERATOR=31
    LT_OPERATOR=32
    GT_OPERATOR=33
    LEQ_OPERATOR=34
    GEQ_OPERATOR=35
    SEQ_OPERATOR=36
    ASSIGN_OPERATOR=37
    OPEN_PARENTHESIS=38
    CLOSE_PARENTHESIS=39
    OPEN_BRACKET=40
    CLOSE_BRACKET=41
    COMMA=42
    BOOLEAN=43
    NUMBER=44
    IDENTIFIER=45
    STRING=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
    WS=49
    ERROR_CHAR=50

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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


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
            self.state = 106
            self.newline_list()
            self.state = 107
            self.decllist()
            self.state = 108
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
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.decl()
                self.state = 111
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
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
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRING_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.DYNAMIC_TYPE, ZCodeParser.VAR_TYPE, ZCodeParser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.vardecl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
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

        def vardecl_only(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_onlyContext,0)


        def vardecl_init(self):
            return self.getTypedRuleContext(ZCodeParser.Vardecl_initContext,0)


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
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.vardecl_only()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.vardecl_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_onlyContext(ParserRuleContext):
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def DYNAMIC_TYPE(self):
            return self.getToken(ZCodeParser.DYNAMIC_TYPE, 0)

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_only

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_only" ):
                return visitor.visitVardecl_only(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_only(self):

        localctx = ZCodeParser.Vardecl_onlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl_only)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.typ()
                self.state = 125
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 126
                self.match(ZCodeParser.NEWLINE)
                self.state = 127
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 130
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 131
                self.match(ZCodeParser.NEWLINE)
                self.state = 132
                self.newline_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.typ()
                self.state = 134
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 135
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 136
                self.arrlist()
                self.state = 137
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 138
                self.match(ZCodeParser.NEWLINE)
                self.state = 139
                self.newline_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_TYPE(self):
            return self.getToken(ZCodeParser.VAR_TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN_OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def DYNAMIC_TYPE(self):
            return self.getToken(ZCodeParser.DYNAMIC_TYPE, 0)

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_init" ):
                return visitor.visitVardecl_init(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_init(self):

        localctx = ZCodeParser.Vardecl_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl_init)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(ZCodeParser.VAR_TYPE)
                self.state = 144
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 145
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 146
                self.expression(0)
                self.state = 147
                self.match(ZCodeParser.NEWLINE)
                self.state = 148
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.typ()
                self.state = 151
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 152
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 153
                self.expression(0)
                self.state = 154
                self.match(ZCodeParser.NEWLINE)
                self.state = 155
                self.newline_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 158
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 159
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 160
                self.expression(0)
                self.state = 161
                self.match(ZCodeParser.NEWLINE)
                self.state = 162
                self.newline_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.typ()
                self.state = 165
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 166
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 167
                self.arrlist()
                self.state = 168
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 169
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 170
                self.expression(0)
                self.state = 171
                self.match(ZCodeParser.NEWLINE)
                self.state = 172
                self.newline_list()
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
        self.enterRule(localctx, 12, self.RULE_arrlist)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(ZCodeParser.NUMBER)
                self.state = 177
                self.match(ZCodeParser.COMMA)
                self.state = 178
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expression" ):
                return visitor.visitArray_expression(self)
            else:
                return visitor.visitChildren(self)




    def array_expression(self):

        localctx = ZCodeParser.Array_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_expression)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OPEN_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 183
                self.arrlist()
                self.state = 184
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass
            elif token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.arrlist()
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


    class Arrlist_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def array_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Array_expressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrlist_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Arrlist_expressionContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrlist_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrlist_expression" ):
                return visitor.visitArrlist_expression(self)
            else:
                return visitor.visitChildren(self)




    def arrlist_expression(self):

        localctx = ZCodeParser.Arrlist_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrlist_expression)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 190
                self.array_expression()
                self.state = 191
                self.match(ZCodeParser.COMMA)
                self.state = 192
                self.arrlist_expression()
                self.state = 193
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.array_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def array_literal_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literal_primeContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_literal)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 199
                self.array_literal_prime()
                self.state = 200
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 203
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_literal_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literal_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_prime" ):
                return visitor.visitArray_literal_prime(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_prime(self):

        localctx = ZCodeParser.Array_literal_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_literal_prime)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.expression(0)
                self.state = 207
                self.match(ZCodeParser.COMMA)
                self.state = 208
                self.array_literal_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expression(0)
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 214
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 215
                self.expression(0)
                self.state = 216
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 2:
                self.state = 218
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 219
                self.expression(10)
                pass

            elif la_ == 3:
                self.state = 220
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 221
                self.expression(9)
                pass

            elif la_ == 4:
                self.state = 222
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 223
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 224
                self.param_list()
                self.state = 225
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 5:
                self.state = 227
                self.literal()
                pass

            elif la_ == 6:
                self.state = 228
                self.array_literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 256
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 231
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 232
                        self.mul_operators()
                        self.state = 233
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 235
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 236
                        self.add_operators()
                        self.state = 237
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 239
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 240
                        self.logic_operators()
                        self.state = 241
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 243
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 244
                        self.rel_operators()
                        self.state = 245
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 247
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 248
                        self.str_operators()
                        self.state = 249
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 251
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 252
                        self.match(ZCodeParser.OPEN_BRACKET)
                        self.state = 253
                        self.index_operators()
                        self.state = 254
                        self.match(ZCodeParser.CLOSE_BRACKET)
                        pass

             
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_sign_operands)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.literal()
                pass
            elif token in [ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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
        self.enterRule(localctx, 26, self.RULE_not_operands)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.literal()
                pass
            elif token in [ZCodeParser.NOT_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
        self.enterRule(localctx, 28, self.RULE_index_operators)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.expression(0)
                self.state = 271
                self.match(ZCodeParser.COMMA)
                self.state = 272
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
        self.enterRule(localctx, 30, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 277
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 278
            self.param_list()
            self.state = 279
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
        self.enterRule(localctx, 32, self.RULE_param_list)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OPERATOR, ZCodeParser.SUB_OPERATOR, ZCodeParser.OPEN_PARENTHESIS, ZCodeParser.OPEN_BRACKET, ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.IDENTIFIER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
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
        self.enterRule(localctx, 34, self.RULE_param_prime)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.param()
                self.state = 286
                self.match(ZCodeParser.COMMA)
                self.state = 287
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
        self.enterRule(localctx, 36, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
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
        self.enterRule(localctx, 38, self.RULE_non_rel_operators)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MUL_OPERATOR, ZCodeParser.DIV_OPERATOR, ZCodeParser.MOD_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.mul_operators()
                pass
            elif token in [ZCodeParser.ADD_OPERATOR, ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.add_operators()
                pass
            elif token in [ZCodeParser.AND_OPERATOR, ZCodeParser.OR_OPERATOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.logic_operators()
                pass
            elif token in [ZCodeParser.STRING_OPERATOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
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
        self.enterRule(localctx, 40, self.RULE_non_str_operators)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MUL_OPERATOR, ZCodeParser.DIV_OPERATOR, ZCodeParser.MOD_OPERATOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.mul_operators()
                pass
            elif token in [ZCodeParser.ADD_OPERATOR, ZCodeParser.SUB_OPERATOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.add_operators()
                pass
            elif token in [ZCodeParser.AND_OPERATOR, ZCodeParser.OR_OPERATOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.logic_operators()
                pass
            elif token in [ZCodeParser.EQ_OPERATOR, ZCodeParser.NEQ_OPERATOR, ZCodeParser.LT_OPERATOR, ZCodeParser.GT_OPERATOR, ZCodeParser.LEQ_OPERATOR, ZCodeParser.GEQ_OPERATOR, ZCodeParser.SEQ_OPERATOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 303
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
        self.enterRule(localctx, 42, self.RULE_non_associative_operands)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.func_call()
                self.state = 309
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 310
                self.index_operators()
                self.state = 311
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.literal()
                self.state = 314
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 315
                self.index_operators()
                self.state = 316
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 318
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 319
                self.func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 320
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 321
                self.literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 322
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 323
                self.func_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 324
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 325
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
        self.enterRule(localctx, 44, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
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
        self.enterRule(localctx, 46, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
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
        self.enterRule(localctx, 48, self.RULE_mul_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
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
        self.enterRule(localctx, 50, self.RULE_add_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
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
        self.enterRule(localctx, 52, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
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
        self.enterRule(localctx, 54, self.RULE_rel_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
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
        self.enterRule(localctx, 56, self.RULE_str_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
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

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(ZCodeParser.OPEN_PARENTHESIS, 0)

        def param_decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_listContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSE_PARENTHESIS, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.FUNC)
            self.state = 343
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 344
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 345
            self.param_decl_list()
            self.state = 346
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
            self.state = 347
            self.newline_list()
            self.state = 348
            self.body()
            self.state = 349
            self.newline_list()
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
        self.enterRule(localctx, 60, self.RULE_param_decl_list)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.STRING_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOL_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
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
        self.enterRule(localctx, 62, self.RULE_param_decl_prime)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.param_single_decl()
                self.state = 356
                self.match(ZCodeParser.COMMA)
                self.state = 357
                self.param_decl_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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
        self.enterRule(localctx, 64, self.RULE_param_single_decl)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.typ()
                self.state = 363
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.typ()
                self.state = 366
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 367
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 368
                self.arrlist()
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
        self.enterRule(localctx, 66, self.RULE_newline_list)
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(ZCodeParser.NEWLINE)
                self.state = 374
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
        self.enterRule(localctx, 68, self.RULE_body)
        try:
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.statement_block()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.ret()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.STRING_TYPE, ZCodeParser.NUMBER_TYPE, ZCodeParser.DYNAMIC_TYPE, ZCodeParser.VAR_TYPE, ZCodeParser.FUNC, ZCodeParser.BOOL_TYPE, ZCodeParser.NEWLINE]:
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

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_block" ):
                return visitor.visitStatement_block(self)
            else:
                return visitor.visitChildren(self)




    def statement_block(self):

        localctx = ZCodeParser.Statement_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_statement_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(ZCodeParser.BEGIN)
            self.state = 384
            self.statement_list()
            self.state = 385
            self.match(ZCodeParser.END)
            self.state = 386
            self.match(ZCodeParser.NEWLINE)
            self.state = 387
            self.newline_list()
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

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


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
        self.enterRule(localctx, 72, self.RULE_statement_list)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.newline_list()
                self.state = 390
                self.statement()
                self.state = 391
                self.newline_list()
                self.state = 392
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.newline_list()
                pass


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


        def statement_block(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_statement)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 401
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 402
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 403
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 404
                self.func_call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 405
                self.statement_block()
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

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

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
        self.enterRule(localctx, 76, self.RULE_ret)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(ZCodeParser.RETURN)
                self.state = 409
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.match(ZCodeParser.RETURN)
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


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.ret()
            self.state = 414
            self.match(ZCodeParser.NEWLINE)
            self.state = 415
            self.newline_list()
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


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_statement" ):
                return visitor.visitFunc_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def func_call_statement(self):

        localctx = ZCodeParser.Func_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_func_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.func_call()
            self.state = 418
            self.match(ZCodeParser.NEWLINE)
            self.state = 419
            self.newline_list()
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


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.lhs()
            self.state = 422
            self.match(ZCodeParser.ASSIGN_OPERATOR)
            self.state = 423
            self.rhs()
            self.state = 424
            self.match(ZCodeParser.NEWLINE)
            self.state = 425
            self.newline_list()
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.expression(0)
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
        self.enterRule(localctx, 86, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
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

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(ZCodeParser.OPEN_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSE_PARENTHESIS, 0)

        def if_body(self):
            return self.getTypedRuleContext(ZCodeParser.If_bodyContext,0)


        def elif_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statement_listContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(ZCodeParser.IF)
            self.state = 432
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 433
            self.expression(0)
            self.state = 434
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
            self.state = 435
            self.if_body()
            self.state = 436
            self.elif_statement_list()
            self.state = 437
            self.else_statement()
            self.state = 438
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_block(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_blockContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_body" ):
                return visitor.visitIf_body(self)
            else:
                return visitor.visitChildren(self)




    def if_body(self):

        localctx = ZCodeParser.If_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_if_body)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.statement_block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elif_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement_list" ):
                return visitor.visitElif_statement_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement_list(self):

        localctx = ZCodeParser.Elif_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elif_statement_list)
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.elif_statement()
                self.state = 446
                self.elif_statement_list()
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


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPEN_PARENTHESIS(self):
            return self.getToken(ZCodeParser.OPEN_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSE_PARENTHESIS, 0)

        def if_body(self):
            return self.getTypedRuleContext(ZCodeParser.If_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(ZCodeParser.ELIF)
            self.state = 452
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 453
            self.expression(0)
            self.state = 454
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
            self.state = 455
            self.if_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def if_body(self):
            return self.getTypedRuleContext(ZCodeParser.If_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_else_statement)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(ZCodeParser.ELSE)
                self.state = 458
                self.if_body()
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


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def for_body(self):
            return self.getTypedRuleContext(ZCodeParser.For_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(ZCodeParser.FOR)
            self.state = 463
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 464
            self.match(ZCodeParser.UNTIL)
            self.state = 465
            self.expression(0)
            self.state = 466
            self.match(ZCodeParser.BY)
            self.state = 467
            self.expression(0)
            self.state = 468
            self.newline_list()
            self.state = 469
            self.for_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_block(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_blockContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_body" ):
                return visitor.visitFor_body(self)
            else:
                return visitor.visitChildren(self)




    def for_body(self):

        localctx = ZCodeParser.For_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_for_body)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.statement_block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 473
                self.match(ZCodeParser.NEWLINE)
                pass


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

        def BREAK_STATEMENT(self):
            return self.getToken(ZCodeParser.BREAK_STATEMENT, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(ZCodeParser.BREAK_STATEMENT)
            self.state = 477
            self.match(ZCodeParser.NEWLINE)
            self.state = 478
            self.newline_list()
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

        def CONTINUE_STATEMENT(self):
            return self.getToken(ZCodeParser.CONTINUE_STATEMENT, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(ZCodeParser.CONTINUE_STATEMENT)
            self.state = 481
            self.match(ZCodeParser.NEWLINE)
            self.state = 482
            self.newline_list()
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
        self._predicates[11] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         




