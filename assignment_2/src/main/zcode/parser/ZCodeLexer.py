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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u019f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\7\23\u00df\n\23\f\23\16\23\u00e2")
        buf.write("\13\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\5\36\u0107\n\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u0131\n,\3-\6-\u0134\n-\r-\16-\u0135\3-\3-\7-")
        buf.write("\u013a\n-\f-\16-\u013d\13-\5-\u013f\n-\3-\5-\u0142\n-")
        buf.write("\3-\6-\u0145\n-\r-\16-\u0146\3-\3-\5-\u014b\n-\3.\3.\3")
        buf.write("/\3/\5/\u0151\n/\3/\6/\u0154\n/\r/\16/\u0155\3\60\3\60")
        buf.write("\7\60\u015a\n\60\f\60\16\60\u015d\13\60\3\61\3\61\3\61")
        buf.write("\3\61\7\61\u0163\n\61\f\61\16\61\u0166\13\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\7\66\u017b\n\66\f\66\16")
        buf.write("\66\u017e\13\66\3\66\5\66\u0181\n\66\3\66\3\66\3\67\3")
        buf.write("\67\3\67\3\67\7\67\u0189\n\67\f\67\16\67\u018c\13\67\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u0192\n\67\3\67\3\67\38\68\u0197")
        buf.write("\n8\r8\168\u0198\38\38\39\39\39\2\2:\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_")
        buf.write("/a\60c\2e\2g\2i\2k\61m\62o\63q\64\3\2\20\4\2\f\f\17\17")
        buf.write("\3\2\62;\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\7\2")
        buf.write("\f\f\17\17$$))^^\t\2))^^ddhhppttvv\5\2$$))^^\4\3\f\f\17")
        buf.write("\17\5\2\f\f\17\17$$\3\2))\3\2$$\5\2\n\13\16\17\"\"\2\u01af")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write("\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3")
        buf.write("\2\2\2\5z\3\2\2\2\7\u0081\3\2\2\2\t\u0089\3\2\2\2\13\u008d")
        buf.write("\3\2\2\2\r\u009b\3\2\2\2\17\u00a1\3\2\2\2\21\u00aa\3\2")
        buf.write("\2\2\23\u00af\3\2\2\2\25\u00b5\3\2\2\2\27\u00b9\3\2\2")
        buf.write("\2\31\u00c0\3\2\2\2\33\u00c3\3\2\2\2\35\u00c8\3\2\2\2")
        buf.write("\37\u00cd\3\2\2\2!\u00d1\3\2\2\2#\u00d7\3\2\2\2%\u00da")
        buf.write("\3\2\2\2\'\u00e5\3\2\2\2)\u00e9\3\2\2\2+\u00ee\3\2\2\2")
        buf.write("-\u00f2\3\2\2\2/\u00f6\3\2\2\2\61\u00f9\3\2\2\2\63\u00fb")
        buf.write("\3\2\2\2\65\u00fd\3\2\2\2\67\u00ff\3\2\2\29\u0101\3\2")
        buf.write("\2\2;\u0106\3\2\2\2=\u0108\3\2\2\2?\u010a\3\2\2\2A\u010d")
        buf.write("\3\2\2\2C\u010f\3\2\2\2E\u0111\3\2\2\2G\u0114\3\2\2\2")
        buf.write("I\u0117\3\2\2\2K\u011a\3\2\2\2M\u011d\3\2\2\2O\u011f\3")
        buf.write("\2\2\2Q\u0121\3\2\2\2S\u0123\3\2\2\2U\u0125\3\2\2\2W\u0130")
        buf.write("\3\2\2\2Y\u014a\3\2\2\2[\u014c\3\2\2\2]\u014e\3\2\2\2")
        buf.write("_\u0157\3\2\2\2a\u015e\3\2\2\2c\u016a\3\2\2\2e\u016c\3")
        buf.write("\2\2\2g\u016f\3\2\2\2i\u0172\3\2\2\2k\u0176\3\2\2\2m\u0184")
        buf.write("\3\2\2\2o\u0196\3\2\2\2q\u019c\3\2\2\2st\7u\2\2tu\7v\2")
        buf.write("\2uv\7t\2\2vw\7k\2\2wx\7p\2\2xy\7i\2\2y\4\3\2\2\2z{\7")
        buf.write("p\2\2{|\7w\2\2|}\7o\2\2}~\7d\2\2~\177\7g\2\2\177\u0080")
        buf.write("\7t\2\2\u0080\6\3\2\2\2\u0081\u0082\7f\2\2\u0082\u0083")
        buf.write("\7{\2\2\u0083\u0084\7p\2\2\u0084\u0085\7c\2\2\u0085\u0086")
        buf.write("\7o\2\2\u0086\u0087\7k\2\2\u0087\u0088\7e\2\2\u0088\b")
        buf.write("\3\2\2\2\u0089\u008a\7x\2\2\u008a\u008b\7c\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\n\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7t\2\2\u0090\u0091\7\"\2\2\u0091\u0092")
        buf.write("\7u\2\2\u0092\u0093\7v\2\2\u0093\u0094\7c\2\2\u0094\u0095")
        buf.write("\7v\2\2\u0095\u0096\7g\2\2\u0096\u0097\7o\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\u0099\7p\2\2\u0099\u009a\7v\2\2\u009a\f")
        buf.write("\3\2\2\2\u009b\u009c\7d\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7m\2\2\u00a0\16")
        buf.write("\3\2\2\2\u00a1\u00a2\7e\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4")
        buf.write("\7p\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9\7g\2\2\u00a9\20")
        buf.write("\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\22\3\2\2\2\u00af\u00b0")
        buf.write("\7d\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7i\2\2\u00b2\u00b3")
        buf.write("\7k\2\2\u00b3\u00b4\7p\2\2\u00b4\24\3\2\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7f\2\2\u00b8\26")
        buf.write("\3\2\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\30\3\2\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7h\2\2\u00c2\32\3\2\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5")
        buf.write("\7n\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7\34")
        buf.write("\3\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\36\3\2\2\2\u00cd\u00ce")
        buf.write("\7h\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7t\2\2\u00d0 \3")
        buf.write("\2\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7n\2\2\u00d6\"")
        buf.write("\3\2\2\2\u00d7\u00d8\7d\2\2\u00d8\u00d9\7{\2\2\u00d9$")
        buf.write("\3\2\2\2\u00da\u00db\7%\2\2\u00db\u00dc\7%\2\2\u00dc\u00e0")
        buf.write("\3\2\2\2\u00dd\u00df\n\2\2\2\u00de\u00dd\3\2\2\2\u00df")
        buf.write("\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\b")
        buf.write("\23\2\2\u00e4&\3\2\2\2\u00e5\u00e6\7\60\2\2\u00e6\u00e7")
        buf.write("\7\60\2\2\u00e7\u00e8\7\60\2\2\u00e8(\3\2\2\2\u00e9\u00ea")
        buf.write("\7d\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed*\3\2\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7v\2\2\u00f1,\3\2\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7f\2\2\u00f5.\3")
        buf.write("\2\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7t\2\2\u00f8\60")
        buf.write("\3\2\2\2\u00f9\u00fa\7-\2\2\u00fa\62\3\2\2\2\u00fb\u00fc")
        buf.write("\7/\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\7,\2\2\u00fe\66\3")
        buf.write("\2\2\2\u00ff\u0100\7\61\2\2\u01008\3\2\2\2\u0101\u0102")
        buf.write("\7\'\2\2\u0102:\3\2\2\2\u0103\u0107\7\f\2\2\u0104\u0105")
        buf.write("\7\17\2\2\u0105\u0107\7\f\2\2\u0106\u0103\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0107<\3\2\2\2\u0108\u0109\7?\2\2\u0109")
        buf.write(">\3\2\2\2\u010a\u010b\7#\2\2\u010b\u010c\7?\2\2\u010c")
        buf.write("@\3\2\2\2\u010d\u010e\7>\2\2\u010eB\3\2\2\2\u010f\u0110")
        buf.write("\7@\2\2\u0110D\3\2\2\2\u0111\u0112\7>\2\2\u0112\u0113")
        buf.write("\7?\2\2\u0113F\3\2\2\2\u0114\u0115\7@\2\2\u0115\u0116")
        buf.write("\7?\2\2\u0116H\3\2\2\2\u0117\u0118\7?\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119J\3\2\2\2\u011a\u011b\7>\2\2\u011b\u011c")
        buf.write("\7/\2\2\u011cL\3\2\2\2\u011d\u011e\7*\2\2\u011eN\3\2\2")
        buf.write("\2\u011f\u0120\7+\2\2\u0120P\3\2\2\2\u0121\u0122\7]\2")
        buf.write("\2\u0122R\3\2\2\2\u0123\u0124\7_\2\2\u0124T\3\2\2\2\u0125")
        buf.write("\u0126\7.\2\2\u0126V\3\2\2\2\u0127\u0128\7v\2\2\u0128")
        buf.write("\u0129\7t\2\2\u0129\u012a\7w\2\2\u012a\u0131\7g\2\2\u012b")
        buf.write("\u012c\7h\2\2\u012c\u012d\7c\2\2\u012d\u012e\7n\2\2\u012e")
        buf.write("\u012f\7u\2\2\u012f\u0131\7g\2\2\u0130\u0127\3\2\2\2\u0130")
        buf.write("\u012b\3\2\2\2\u0131X\3\2\2\2\u0132\u0134\5[.\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\u013e\3\2\2\2\u0137\u013b\7")
        buf.write("\60\2\2\u0138\u013a\5[.\2\u0139\u0138\3\2\2\2\u013a\u013d")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u0137\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u0142\5")
        buf.write("]/\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u014b")
        buf.write("\3\2\2\2\u0143\u0145\5[.\2\u0144\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0148\3\2\2\2\u0148\u0149\5]/\2\u0149\u014b\3\2\2\2\u014a")
        buf.write("\u0133\3\2\2\2\u014a\u0144\3\2\2\2\u014bZ\3\2\2\2\u014c")
        buf.write("\u014d\t\3\2\2\u014d\\\3\2\2\2\u014e\u0150\t\4\2\2\u014f")
        buf.write("\u0151\t\5\2\2\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151\u0153\3\2\2\2\u0152\u0154\5[.\2\u0153\u0152\3\2")
        buf.write("\2\2\u0154\u0155\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156^\3\2\2\2\u0157\u015b\t\6\2\2\u0158\u015a")
        buf.write("\t\7\2\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c`\3\2\2\2\u015d")
        buf.write("\u015b\3\2\2\2\u015e\u0164\5c\62\2\u015f\u0163\n\b\2\2")
        buf.write("\u0160\u0163\5g\64\2\u0161\u0163\5e\63\2\u0162\u015f\3")
        buf.write("\2\2\2\u0162\u0160\3\2\2\2\u0162\u0161\3\2\2\2\u0163\u0166")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\5c\62\2")
        buf.write("\u0168\u0169\b\61\3\2\u0169b\3\2\2\2\u016a\u016b\7$\2")
        buf.write("\2\u016bd\3\2\2\2\u016c\u016d\7)\2\2\u016d\u016e\7$\2")
        buf.write("\2\u016ef\3\2\2\2\u016f\u0170\7^\2\2\u0170\u0171\t\t\2")
        buf.write("\2\u0171h\3\2\2\2\u0172\u0173\7^\2\2\u0173\u0174\7^\2")
        buf.write("\2\u0174\u0175\n\t\2\2\u0175j\3\2\2\2\u0176\u017c\5c\62")
        buf.write("\2\u0177\u017b\n\n\2\2\u0178\u017b\5e\63\2\u0179\u017b")
        buf.write("\5g\64\2\u017a\u0177\3\2\2\2\u017a\u0178\3\2\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3")
        buf.write("\2\2\2\u017f\u0181\t\13\2\2\u0180\u017f\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0183\b\66\4\2\u0183l\3\2\2\2\u0184")
        buf.write("\u018a\5c\62\2\u0185\u0189\n\f\2\2\u0186\u0189\5e\63\2")
        buf.write("\u0187\u0189\5g\64\2\u0188\u0185\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u0191\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018d\u018e\7^\2\2\u018e\u0192\n\t\2\2")
        buf.write("\u018f\u0190\t\r\2\2\u0190\u0192\n\16\2\2\u0191\u018d")
        buf.write("\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0194\b\67\5\2\u0194n\3\2\2\2\u0195\u0197\t\17\2\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\b")
        buf.write("8\2\2\u019bp\3\2\2\2\u019c\u019d\13\2\2\2\u019d\u019e")
        buf.write("\b9\6\2\u019er\3\2\2\2\30\2\u00e0\u0106\u0130\u0135\u013b")
        buf.write("\u013e\u0141\u0146\u014a\u0150\u0155\u015b\u0162\u0164")
        buf.write("\u017a\u017c\u0180\u0188\u018a\u0191\u0198\7\b\2\2\3\61")
        buf.write("\2\3\66\3\3\67\4\39\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING_TYPE = 1
    NUMBER_TYPE = 2
    DYNAMIC_TYPE = 3
    VAR_TYPE = 4
    FOR_STATEMENT = 5
    BREAK_STATEMENT = 6
    CONTINUE_STATEMENT = 7
    FUNC = 8
    BEGIN = 9
    END = 10
    RETURN = 11
    IF = 12
    ELIF = 13
    ELSE = 14
    FOR = 15
    UNTIL = 16
    BY = 17
    COMMENT = 18
    STRING_OPERATOR = 19
    BOOL_TYPE = 20
    NOT_OPERATOR = 21
    AND_OPERATOR = 22
    OR_OPERATOR = 23
    ADD_OPERATOR = 24
    SUB_OPERATOR = 25
    MUL_OPERATOR = 26
    DIV_OPERATOR = 27
    MOD_OPERATOR = 28
    NEWLINE = 29
    EQ_OPERATOR = 30
    NEQ_OPERATOR = 31
    LT_OPERATOR = 32
    GT_OPERATOR = 33
    LEQ_OPERATOR = 34
    GEQ_OPERATOR = 35
    SEQ_OPERATOR = 36
    ASSIGN_OPERATOR = 37
    OPEN_PARENTHESIS = 38
    CLOSE_PARENTHESIS = 39
    OPEN_BRACKET = 40
    CLOSE_BRACKET = 41
    COMMA = 42
    BOOLEAN = 43
    NUMBER = 44
    IDENTIFIER = 45
    STRING = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
    WS = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'string'", "'number'", "'dynamic'", "'var'", "'for statement'", 
            "'break'", "'continue'", "'func'", "'begin'", "'end'", "'return'", 
            "'if'", "'elif'", "'else'", "'for'", "'until'", "'by'", "'...'", 
            "'bool'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", 
            "'<-'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "STRING_TYPE", "NUMBER_TYPE", "DYNAMIC_TYPE", "VAR_TYPE", "FOR_STATEMENT", 
            "BREAK_STATEMENT", "CONTINUE_STATEMENT", "FUNC", "BEGIN", "END", 
            "RETURN", "IF", "ELIF", "ELSE", "FOR", "UNTIL", "BY", "COMMENT", 
            "STRING_OPERATOR", "BOOL_TYPE", "NOT_OPERATOR", "AND_OPERATOR", 
            "OR_OPERATOR", "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", 
            "DIV_OPERATOR", "MOD_OPERATOR", "NEWLINE", "EQ_OPERATOR", "NEQ_OPERATOR", 
            "LT_OPERATOR", "GT_OPERATOR", "LEQ_OPERATOR", "GEQ_OPERATOR", 
            "SEQ_OPERATOR", "ASSIGN_OPERATOR", "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", 
            "OPEN_BRACKET", "CLOSE_BRACKET", "COMMA", "BOOLEAN", "NUMBER", 
            "IDENTIFIER", "STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "STRING_TYPE", "NUMBER_TYPE", "DYNAMIC_TYPE", "VAR_TYPE", 
                  "FOR_STATEMENT", "BREAK_STATEMENT", "CONTINUE_STATEMENT", 
                  "FUNC", "BEGIN", "END", "RETURN", "IF", "ELIF", "ELSE", 
                  "FOR", "UNTIL", "BY", "COMMENT", "STRING_OPERATOR", "BOOL_TYPE", 
                  "NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", "ADD_OPERATOR", 
                  "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", "MOD_OPERATOR", 
                  "NEWLINE", "EQ_OPERATOR", "NEQ_OPERATOR", "LT_OPERATOR", 
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
            actions[47] = self.STRING_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[55] = self.ERROR_CHAR_action 
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
            	#print("this is an unclosed string: "+repr(self.text))
            	
            	#Windows case
            	tmp = self.text[::-1].find("\n")

            	if (tmp != -1):
            		if (self.text[::-1].find("\n\r")!=-1):
            			self.text = self.text[0:len(self.text)-tmp-2]
            			#print("windows case: "+repr(self.text))
            			raise UncloseString(self.text)
            			return
            		else:
            			#Linux case
            			tmp = self.text[::-1].find("\n")

            			if(tmp!=-1):
            				self.text = self.text[0:len(self.text)-tmp-1]
            				#print("Linux case: "+self.text)
            				raise UncloseString(self.text)
            				return

            	raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:]
            	#print("this is illegal escape: "+self.text)
            	raise IllegalEscape(self.text)
            	

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


