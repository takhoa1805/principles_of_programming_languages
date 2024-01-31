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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u01d0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u00de\n\16\f\16\16\16\u00e1\13\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0136\n\31\3\32\3\32\3\33\3\33\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u0162\n(\3)\6)\u0165")
        buf.write("\n)\r)\16)\u0166\3)\3)\7)\u016b\n)\f)\16)\u016e\13)\5")
        buf.write(")\u0170\n)\3)\5)\u0173\n)\3)\6)\u0176\n)\r)\16)\u0177")
        buf.write("\3)\3)\5)\u017c\n)\3*\3*\3+\3+\5+\u0182\n+\3+\6+\u0185")
        buf.write("\n+\r+\16+\u0186\3,\3,\7,\u018b\n,\f,\16,\u018e\13,\3")
        buf.write("-\3-\3-\3-\7-\u0194\n-\f-\16-\u0197\13-\3-\3-\3-\3.\3")
        buf.write(".\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\7\62\u01ac\n\62\f\62\16\62\u01af\13\62\3\62")
        buf.write("\5\62\u01b2\n\62\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u01ba")
        buf.write("\n\63\f\63\16\63\u01bd\13\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u01c3\n\63\3\63\3\63\3\64\6\64\u01c8\n\64\r\64\16\64")
        buf.write("\u01c9\3\64\3\64\3\65\3\65\3\65\2\2\66\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S\2U\2W+Y,[\2")
        buf.write("]\2_\2a\2c-e.g/i\60\3\2\21\4\2\f\f\17\17\3\2\f\f\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\7\2\f\f\17")
        buf.write("\17$$))^^\t\2))^^ddhhppttvv\5\2$$))^^\4\3\f\f\17\17\5")
        buf.write("\2\f\f\17\17$$\3\2))\3\2$$\5\2\n\13\16\17\"\"\2\u01ea")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2")
        buf.write("\2\2\3k\3\2\2\2\5p\3\2\2\2\7v\3\2\2\2\tz\3\2\2\2\13\u0081")
        buf.write("\3\2\2\2\r\u008e\3\2\2\2\17\u009c\3\2\2\2\21\u00ac\3\2")
        buf.write("\2\2\23\u00bf\3\2\2\2\25\u00c6\3\2\2\2\27\u00cd\3\2\2")
        buf.write("\2\31\u00d5\3\2\2\2\33\u00d9\3\2\2\2\35\u00e4\3\2\2\2")
        buf.write("\37\u00e8\3\2\2\2!\u00ed\3\2\2\2#\u00f1\3\2\2\2%\u00f5")
        buf.write("\3\2\2\2\'\u00f8\3\2\2\2)\u00fa\3\2\2\2+\u00fc\3\2\2\2")
        buf.write("-\u00fe\3\2\2\2/\u0100\3\2\2\2\61\u0135\3\2\2\2\63\u0137")
        buf.write("\3\2\2\2\65\u0139\3\2\2\2\67\u013b\3\2\2\29\u013e\3\2")
        buf.write("\2\2;\u0140\3\2\2\2=\u0142\3\2\2\2?\u0145\3\2\2\2A\u0148")
        buf.write("\3\2\2\2C\u014b\3\2\2\2E\u014e\3\2\2\2G\u0150\3\2\2\2")
        buf.write("I\u0152\3\2\2\2K\u0154\3\2\2\2M\u0156\3\2\2\2O\u0161\3")
        buf.write("\2\2\2Q\u017b\3\2\2\2S\u017d\3\2\2\2U\u017f\3\2\2\2W\u0188")
        buf.write("\3\2\2\2Y\u018f\3\2\2\2[\u019b\3\2\2\2]\u019d\3\2\2\2")
        buf.write("_\u01a0\3\2\2\2a\u01a3\3\2\2\2c\u01a7\3\2\2\2e\u01b5\3")
        buf.write("\2\2\2g\u01c7\3\2\2\2i\u01cd\3\2\2\2kl\7h\2\2lm\7w\2\2")
        buf.write("mn\7p\2\2no\7e\2\2o\4\3\2\2\2pq\7d\2\2qr\7g\2\2rs\7i\2")
        buf.write("\2st\7k\2\2tu\7p\2\2u\6\3\2\2\2vw\7g\2\2wx\7p\2\2xy\7")
        buf.write("f\2\2y\b\3\2\2\2z{\7t\2\2{|\7g\2\2|}\7v\2\2}~\7w\2\2~")
        buf.write("\177\7t\2\2\177\u0080\7p\2\2\u0080\n\3\2\2\2\u0081\u0082")
        buf.write("\7k\2\2\u0082\u0083\7h\2\2\u0083\u0084\7\"\2\2\u0084\u0085")
        buf.write("\7u\2\2\u0085\u0086\7v\2\2\u0086\u0087\7c\2\2\u0087\u0088")
        buf.write("\7v\2\2\u0088\u0089\7g\2\2\u0089\u008a\7o\2\2\u008a\u008b")
        buf.write("\7g\2\2\u008b\u008c\7p\2\2\u008c\u008d\7v\2\2\u008d\f")
        buf.write("\3\2\2\2\u008e\u008f\7h\2\2\u008f\u0090\7q\2\2\u0090\u0091")
        buf.write("\7t\2\2\u0091\u0092\7\"\2\2\u0092\u0093\7u\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\u0095\7c\2\2\u0095\u0096\7v\2\2\u0096\u0097")
        buf.write("\7g\2\2\u0097\u0098\7o\2\2\u0098\u0099\7g\2\2\u0099\u009a")
        buf.write("\7p\2\2\u009a\u009b\7v\2\2\u009b\16\3\2\2\2\u009c\u009d")
        buf.write("\7d\2\2\u009d\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7m\2\2\u00a1\u00a2\7\"\2\2\u00a2\u00a3")
        buf.write("\7u\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7o\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\20")
        buf.write("\3\2\2\2\u00ac\u00ad\7e\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7\"\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7c\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7o\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\22\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\24\3\2\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7o\2\2\u00c9\u00ca")
        buf.write("\7d\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7t\2\2\u00cc\26")
        buf.write("\3\2\2\2\u00cd\u00ce\7f\2\2\u00ce\u00cf\7{\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7o\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7e\2\2\u00d4\30\3\2\2\2\u00d5\u00d6")
        buf.write("\7x\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7t\2\2\u00d8\32")
        buf.write("\3\2\2\2\u00d9\u00da\7%\2\2\u00da\u00db\7%\2\2\u00db\u00df")
        buf.write("\3\2\2\2\u00dc\u00de\n\2\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\b")
        buf.write("\16\2\2\u00e3\34\3\2\2\2\u00e4\u00e5\7\60\2\2\u00e5\u00e6")
        buf.write("\7\60\2\2\u00e6\u00e7\7\60\2\2\u00e7\36\3\2\2\2\u00e8")
        buf.write("\u00e9\7d\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7q\2\2\u00eb")
        buf.write("\u00ec\7n\2\2\u00ec \3\2\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write("\u00ef\7q\2\2\u00ef\u00f0\7v\2\2\u00f0\"\3\2\2\2\u00f1")
        buf.write("\u00f2\7c\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7f\2\2\u00f4")
        buf.write("$\3\2\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7t\2\2\u00f7")
        buf.write("&\3\2\2\2\u00f8\u00f9\7-\2\2\u00f9(\3\2\2\2\u00fa\u00fb")
        buf.write("\7/\2\2\u00fb*\3\2\2\2\u00fc\u00fd\7,\2\2\u00fd,\3\2\2")
        buf.write("\2\u00fe\u00ff\7\61\2\2\u00ff.\3\2\2\2\u0100\u0101\7\'")
        buf.write("\2\2\u0101\60\3\2\2\2\u0102\u0103\7t\2\2\u0103\u0104\7")
        buf.write("g\2\2\u0104\u0105\7v\2\2\u0105\u0106\7w\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\u0136\7p\2\2\u0108\u0109\7h\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7p\2\2\u010b\u0136\7e\2\2\u010c\u010d")
        buf.write("\7h\2\2\u010d\u010e\7q\2\2\u010e\u0136\7t\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7p\2\2\u0111\u0112\7v\2\2\u0112\u0113")
        buf.write("\7k\2\2\u0113\u0136\7n\2\2\u0114\u0115\7d\2\2\u0115\u0136")
        buf.write("\7{\2\2\u0116\u0117\7d\2\2\u0117\u0118\7t\2\2\u0118\u0119")
        buf.write("\7g\2\2\u0119\u011a\7c\2\2\u011a\u0136\7m\2\2\u011b\u011c")
        buf.write("\7e\2\2\u011c\u011d\7q\2\2\u011d\u011e\7p\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122")
        buf.write("\7w\2\2\u0122\u0136\7g\2\2\u0123\u0124\7k\2\2\u0124\u0136")
        buf.write("\7h\2\2\u0125\u0126\7g\2\2\u0126\u0127\7n\2\2\u0127\u0128")
        buf.write("\7u\2\2\u0128\u0136\7g\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7n\2\2\u012b\u012c\7k\2\2\u012c\u0136\7h\2\2\u012d\u012e")
        buf.write("\7d\2\2\u012e\u012f\7g\2\2\u012f\u0130\7i\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0136\7p\2\2\u0132\u0133\7g\2\2\u0133\u0134")
        buf.write("\7p\2\2\u0134\u0136\7f\2\2\u0135\u0102\3\2\2\2\u0135\u0108")
        buf.write("\3\2\2\2\u0135\u010c\3\2\2\2\u0135\u010f\3\2\2\2\u0135")
        buf.write("\u0114\3\2\2\2\u0135\u0116\3\2\2\2\u0135\u011b\3\2\2\2")
        buf.write("\u0135\u0123\3\2\2\2\u0135\u0125\3\2\2\2\u0135\u0129\3")
        buf.write("\2\2\2\u0135\u012d\3\2\2\2\u0135\u0132\3\2\2\2\u0136\62")
        buf.write("\3\2\2\2\u0137\u0138\t\3\2\2\u0138\64\3\2\2\2\u0139\u013a")
        buf.write("\7?\2\2\u013a\66\3\2\2\2\u013b\u013c\7#\2\2\u013c\u013d")
        buf.write("\7?\2\2\u013d8\3\2\2\2\u013e\u013f\7>\2\2\u013f:\3\2\2")
        buf.write("\2\u0140\u0141\7@\2\2\u0141<\3\2\2\2\u0142\u0143\7>\2")
        buf.write("\2\u0143\u0144\7?\2\2\u0144>\3\2\2\2\u0145\u0146\7@\2")
        buf.write("\2\u0146\u0147\7?\2\2\u0147@\3\2\2\2\u0148\u0149\7?\2")
        buf.write("\2\u0149\u014a\7?\2\2\u014aB\3\2\2\2\u014b\u014c\7>\2")
        buf.write("\2\u014c\u014d\7/\2\2\u014dD\3\2\2\2\u014e\u014f\7*\2")
        buf.write("\2\u014fF\3\2\2\2\u0150\u0151\7+\2\2\u0151H\3\2\2\2\u0152")
        buf.write("\u0153\7]\2\2\u0153J\3\2\2\2\u0154\u0155\7_\2\2\u0155")
        buf.write("L\3\2\2\2\u0156\u0157\7.\2\2\u0157N\3\2\2\2\u0158\u0159")
        buf.write("\7v\2\2\u0159\u015a\7t\2\2\u015a\u015b\7w\2\2\u015b\u0162")
        buf.write("\7g\2\2\u015c\u015d\7h\2\2\u015d\u015e\7c\2\2\u015e\u015f")
        buf.write("\7n\2\2\u015f\u0160\7u\2\2\u0160\u0162\7g\2\2\u0161\u0158")
        buf.write("\3\2\2\2\u0161\u015c\3\2\2\2\u0162P\3\2\2\2\u0163\u0165")
        buf.write("\5S*\2\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u016f\3\2\2\2\u0168")
        buf.write("\u016c\7\60\2\2\u0169\u016b\5S*\2\u016a\u0169\3\2\2\2")
        buf.write("\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0168")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0172\3\2\2\2\u0171")
        buf.write("\u0173\5U+\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u017c\3\2\2\2\u0174\u0176\5S*\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017a\5U+\2\u017a\u017c\3\2")
        buf.write("\2\2\u017b\u0164\3\2\2\2\u017b\u0175\3\2\2\2\u017cR\3")
        buf.write("\2\2\2\u017d\u017e\t\4\2\2\u017eT\3\2\2\2\u017f\u0181")
        buf.write("\t\5\2\2\u0180\u0182\t\6\2\2\u0181\u0180\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0184\3\2\2\2\u0183\u0185\5S*\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0186\u0187\3\2\2\2\u0187V\3\2\2\2\u0188\u018c\t\7\2")
        buf.write("\2\u0189\u018b\t\b\2\2\u018a\u0189\3\2\2\2\u018b\u018e")
        buf.write("\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d")
        buf.write("X\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0195\5[.\2\u0190")
        buf.write("\u0194\n\t\2\2\u0191\u0194\5_\60\2\u0192\u0194\5]/\2\u0193")
        buf.write("\u0190\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2")
        buf.write("\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199")
        buf.write("\5[.\2\u0199\u019a\b-\3\2\u019aZ\3\2\2\2\u019b\u019c\7")
        buf.write("$\2\2\u019c\\\3\2\2\2\u019d\u019e\7)\2\2\u019e\u019f\7")
        buf.write("$\2\2\u019f^\3\2\2\2\u01a0\u01a1\7^\2\2\u01a1\u01a2\t")
        buf.write("\n\2\2\u01a2`\3\2\2\2\u01a3\u01a4\7^\2\2\u01a4\u01a5\7")
        buf.write("^\2\2\u01a5\u01a6\n\n\2\2\u01a6b\3\2\2\2\u01a7\u01ad\5")
        buf.write("[.\2\u01a8\u01ac\n\13\2\2\u01a9\u01ac\5]/\2\u01aa\u01ac")
        buf.write("\5_\60\2\u01ab\u01a8\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01b2\t\f\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3")
        buf.write("\3\2\2\2\u01b3\u01b4\b\62\4\2\u01b4d\3\2\2\2\u01b5\u01bb")
        buf.write("\5[.\2\u01b6\u01ba\n\r\2\2\u01b7\u01ba\5]/\2\u01b8\u01ba")
        buf.write("\5_\60\2\u01b9\u01b6\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bb\u01bc\3\2\2\2\u01bc\u01c2\3\2\2\2\u01bd\u01bb\3")
        buf.write("\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c3\n\n\2\2\u01c0\u01c1")
        buf.write("\t\16\2\2\u01c1\u01c3\n\17\2\2\u01c2\u01be\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\b\63\5")
        buf.write("\2\u01c5f\3\2\2\2\u01c6\u01c8\t\20\2\2\u01c7\u01c6\3\2")
        buf.write("\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\b\64\2\2\u01cc")
        buf.write("h\3\2\2\2\u01cd\u01ce\13\2\2\2\u01ce\u01cf\b\65\6\2\u01cf")
        buf.write("j\3\2\2\2\30\2\u00df\u0135\u0161\u0166\u016c\u016f\u0172")
        buf.write("\u0177\u017b\u0181\u0186\u018c\u0193\u0195\u01ab\u01ad")
        buf.write("\u01b1\u01b9\u01bb\u01c2\u01c9\7\b\2\2\3-\2\3\62\3\3\63")
        buf.write("\4\3\65\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    STRING_TYPE = 9
    NUMBER_TYPE = 10
    DYNAMIC_TYPE = 11
    VAR_TYPE = 12
    COMMENT = 13
    STRING_OPERATOR = 14
    BOOL_TYPE = 15
    NOT_OPERATOR = 16
    AND_OPERATOR = 17
    OR_OPERATOR = 18
    ADD_OPERATOR = 19
    SUB_OPERATOR = 20
    MUL_OPERATOR = 21
    DIV_OPERATOR = 22
    MOD_OPERATOR = 23
    KEYWORD = 24
    NEWLINE = 25
    EQ_OPERATOR = 26
    NEQ_OPERATOR = 27
    LT_OPERATOR = 28
    GT_OPERATOR = 29
    LEQ_OPERATOR = 30
    GEQ_OPERATOR = 31
    SEQ_OPERATOR = 32
    ASSIGN_OPERATOR = 33
    OPEN_PARENTHESIS = 34
    CLOSE_PARENTHESIS = 35
    OPEN_BRACKET = 36
    CLOSE_BRACKET = 37
    COMMA = 38
    BOOLEAN = 39
    NUMBER = 40
    IDENTIFIER = 41
    STRING = 42
    UNCLOSE_STRING = 43
    ILLEGAL_ESCAPE = 44
    WS = 45
    ERROR_CHAR = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'func'", "'begin'", "'end'", "'return'", "'if statement'", 
            "'for statement'", "'break statement'", "'continue statement'", 
            "'string'", "'number'", "'dynamic'", "'var'", "'...'", "'bool'", 
            "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", "'<-'", 
            "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "STRING_TYPE", "NUMBER_TYPE", "DYNAMIC_TYPE", "VAR_TYPE", "COMMENT", 
            "STRING_OPERATOR", "BOOL_TYPE", "NOT_OPERATOR", "AND_OPERATOR", 
            "OR_OPERATOR", "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", 
            "DIV_OPERATOR", "MOD_OPERATOR", "KEYWORD", "NEWLINE", "EQ_OPERATOR", 
            "NEQ_OPERATOR", "LT_OPERATOR", "GT_OPERATOR", "LEQ_OPERATOR", 
            "GEQ_OPERATOR", "SEQ_OPERATOR", "ASSIGN_OPERATOR", "OPEN_PARENTHESIS", 
            "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", "COMMA", 
            "BOOLEAN", "NUMBER", "IDENTIFIER", "STRING", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "STRING_TYPE", "NUMBER_TYPE", "DYNAMIC_TYPE", 
                  "VAR_TYPE", "COMMENT", "STRING_OPERATOR", "BOOL_TYPE", 
                  "NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", "ADD_OPERATOR", 
                  "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", "MOD_OPERATOR", 
                  "KEYWORD", "NEWLINE", "EQ_OPERATOR", "NEQ_OPERATOR", "LT_OPERATOR", 
                  "GT_OPERATOR", "LEQ_OPERATOR", "GEQ_OPERATOR", "SEQ_OPERATOR", 
                  "ASSIGN_OPERATOR", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
                  "OPEN_BRACKET", "CLOSE_BRACKET", "COMMA", "BOOLEAN", "NUMBER", 
                  "DIGIT", "EXPONENT", "IDENTIFIER", "STRING", "DOUBLE_QUOTE", 
                  "DOUBLE_QUOTE_NOTATION", "LEGAL_ESCAPE_SEQUENCE", "ILLEGAL_ESCAPE_SEQUENCE", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

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
            actions[43] = self.STRING_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[49] = self.ILLEGAL_ESCAPE_action 
            actions[51] = self.ERROR_CHAR_action 
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
     


