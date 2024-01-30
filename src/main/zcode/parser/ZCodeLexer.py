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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(")
        buf.write("\u016c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4l\n\4\f\4\16\4o\13\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00d2\n\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3")
        buf.write("\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u00fe\n")
        buf.write(" \3!\6!\u0101\n!\r!\16!\u0102\3!\3!\7!\u0107\n!\f!\16")
        buf.write("!\u010a\13!\5!\u010c\n!\3!\5!\u010f\n!\3!\6!\u0112\n!")
        buf.write("\r!\16!\u0113\3!\3!\5!\u0118\n!\3\"\3\"\3#\3#\5#\u011e")
        buf.write("\n#\3#\6#\u0121\n#\r#\16#\u0122\3$\3$\7$\u0127\n$\f$\16")
        buf.write("$\u012a\13$\3%\3%\3%\3%\7%\u0130\n%\f%\16%\u0133\13%\3")
        buf.write("%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\7*\u0148\n*\f*\16*\u014b\13*\3*\5*\u014e\n*\3*\3")
        buf.write("*\3+\3+\3+\3+\7+\u0156\n+\f+\16+\u0159\13+\3+\3+\3+\3")
        buf.write("+\5+\u015f\n+\3+\3+\3,\6,\u0164\n,\r,\16,\u0165\3,\3,")
        buf.write("\3-\3-\3-\2\2.\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C\2")
        buf.write("E\2G#I$K\2M\2O\2Q\2S%U&W\'Y(\3\2\21\4\2\f\f\17\17\3\2")
        buf.write("\f\f\3\2\62;\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\5\2$$))^^\4\3")
        buf.write("\f\f\17\17\5\2\f\f\17\17$$\3\2))\3\2$$\5\2\n\13\16\17")
        buf.write("\"\"\2\u0186\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\3[\3\2\2\2\5c\3\2")
        buf.write("\2\2\7g\3\2\2\2\tr\3\2\2\2\13y\3\2\2\2\r}\3\2\2\2\17\u0082")
        buf.write("\3\2\2\2\21\u0086\3\2\2\2\23\u008a\3\2\2\2\25\u008d\3")
        buf.write("\2\2\2\27\u0094\3\2\2\2\31\u0096\3\2\2\2\33\u0098\3\2")
        buf.write("\2\2\35\u009a\3\2\2\2\37\u009c\3\2\2\2!\u00d1\3\2\2\2")
        buf.write("#\u00d3\3\2\2\2%\u00d5\3\2\2\2\'\u00d7\3\2\2\2)\u00da")
        buf.write("\3\2\2\2+\u00dc\3\2\2\2-\u00de\3\2\2\2/\u00e1\3\2\2\2")
        buf.write("\61\u00e4\3\2\2\2\63\u00e7\3\2\2\2\65\u00ea\3\2\2\2\67")
        buf.write("\u00ec\3\2\2\29\u00ee\3\2\2\2;\u00f0\3\2\2\2=\u00f2\3")
        buf.write("\2\2\2?\u00fd\3\2\2\2A\u0117\3\2\2\2C\u0119\3\2\2\2E\u011b")
        buf.write("\3\2\2\2G\u0124\3\2\2\2I\u012b\3\2\2\2K\u0137\3\2\2\2")
        buf.write("M\u0139\3\2\2\2O\u013c\3\2\2\2Q\u013f\3\2\2\2S\u0143\3")
        buf.write("\2\2\2U\u0151\3\2\2\2W\u0163\3\2\2\2Y\u0169\3\2\2\2[\\")
        buf.write("\7f\2\2\\]\7{\2\2]^\7p\2\2^_\7c\2\2_`\7o\2\2`a\7k\2\2")
        buf.write("ab\7e\2\2b\4\3\2\2\2cd\7x\2\2de\7c\2\2ef\7t\2\2f\6\3\2")
        buf.write("\2\2gh\7%\2\2hi\7%\2\2im\3\2\2\2jl\n\2\2\2kj\3\2\2\2l")
        buf.write("o\3\2\2\2mk\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2pq\b")
        buf.write("\4\2\2q\b\3\2\2\2rs\7u\2\2st\7v\2\2tu\7t\2\2uv\7k\2\2")
        buf.write("vw\7p\2\2wx\7i\2\2x\n\3\2\2\2yz\7\60\2\2z{\7\60\2\2{|")
        buf.write("\7\60\2\2|\f\3\2\2\2}~\7d\2\2~\177\7q\2\2\177\u0080\7")
        buf.write("q\2\2\u0080\u0081\7n\2\2\u0081\16\3\2\2\2\u0082\u0083")
        buf.write("\7p\2\2\u0083\u0084\7q\2\2\u0084\u0085\7v\2\2\u0085\20")
        buf.write("\3\2\2\2\u0086\u0087\7c\2\2\u0087\u0088\7p\2\2\u0088\u0089")
        buf.write("\7f\2\2\u0089\22\3\2\2\2\u008a\u008b\7q\2\2\u008b\u008c")
        buf.write("\7t\2\2\u008c\24\3\2\2\2\u008d\u008e\7p\2\2\u008e\u008f")
        buf.write("\7w\2\2\u008f\u0090\7o\2\2\u0090\u0091\7d\2\2\u0091\u0092")
        buf.write("\7g\2\2\u0092\u0093\7t\2\2\u0093\26\3\2\2\2\u0094\u0095")
        buf.write("\7-\2\2\u0095\30\3\2\2\2\u0096\u0097\7/\2\2\u0097\32\3")
        buf.write("\2\2\2\u0098\u0099\7,\2\2\u0099\34\3\2\2\2\u009a\u009b")
        buf.write("\7\61\2\2\u009b\36\3\2\2\2\u009c\u009d\7\'\2\2\u009d ")
        buf.write("\3\2\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7w\2\2\u00a2\u00a3\7t\2\2\u00a3\u00d2")
        buf.write("\7p\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00d2\7e\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\u00d2\7t\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7k\2\2\u00af\u00d2")
        buf.write("\7n\2\2\u00b0\u00b1\7d\2\2\u00b1\u00d2\7{\2\2\u00b2\u00b3")
        buf.write("\7d\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7c\2\2\u00b6\u00d2\7m\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7w\2\2\u00be\u00d2")
        buf.write("\7g\2\2\u00bf\u00c0\7k\2\2\u00c0\u00d2\7h\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7u\2\2\u00c4\u00d2")
        buf.write("\7g\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8")
        buf.write("\7k\2\2\u00c8\u00d2\7h\2\2\u00c9\u00ca\7d\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7i\2\2\u00cc\u00cd\7k\2\2\u00cd\u00d2")
        buf.write("\7p\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d2")
        buf.write("\7f\2\2\u00d1\u009e\3\2\2\2\u00d1\u00a4\3\2\2\2\u00d1")
        buf.write("\u00a8\3\2\2\2\u00d1\u00ab\3\2\2\2\u00d1\u00b0\3\2\2\2")
        buf.write("\u00d1\u00b2\3\2\2\2\u00d1\u00b7\3\2\2\2\u00d1\u00bf\3")
        buf.write("\2\2\2\u00d1\u00c1\3\2\2\2\u00d1\u00c5\3\2\2\2\u00d1\u00c9")
        buf.write("\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d2\"\3\2\2\2\u00d3\u00d4")
        buf.write("\t\3\2\2\u00d4$\3\2\2\2\u00d5\u00d6\7?\2\2\u00d6&\3\2")
        buf.write("\2\2\u00d7\u00d8\7#\2\2\u00d8\u00d9\7?\2\2\u00d9(\3\2")
        buf.write("\2\2\u00da\u00db\7>\2\2\u00db*\3\2\2\2\u00dc\u00dd\7@")
        buf.write("\2\2\u00dd,\3\2\2\2\u00de\u00df\7>\2\2\u00df\u00e0\7?")
        buf.write("\2\2\u00e0.\3\2\2\2\u00e1\u00e2\7@\2\2\u00e2\u00e3\7?")
        buf.write("\2\2\u00e3\60\3\2\2\2\u00e4\u00e5\7?\2\2\u00e5\u00e6\7")
        buf.write("?\2\2\u00e6\62\3\2\2\2\u00e7\u00e8\7>\2\2\u00e8\u00e9")
        buf.write("\7/\2\2\u00e9\64\3\2\2\2\u00ea\u00eb\7*\2\2\u00eb\66\3")
        buf.write("\2\2\2\u00ec\u00ed\7+\2\2\u00ed8\3\2\2\2\u00ee\u00ef\7")
        buf.write("]\2\2\u00ef:\3\2\2\2\u00f0\u00f1\7_\2\2\u00f1<\3\2\2\2")
        buf.write("\u00f2\u00f3\7.\2\2\u00f3>\3\2\2\2\u00f4\u00f5\7v\2\2")
        buf.write("\u00f5\u00f6\7t\2\2\u00f6\u00f7\7w\2\2\u00f7\u00fe\7g")
        buf.write("\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb")
        buf.write("\7n\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fe\7g\2\2\u00fd\u00f4")
        buf.write("\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fe@\3\2\2\2\u00ff\u0101")
        buf.write("\5C\"\2\u0100\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u010b\3\2\2\2")
        buf.write("\u0104\u0108\7\60\2\2\u0105\u0107\5C\"\2\u0106\u0105\3")
        buf.write("\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u0104\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010e\3\2\2\2")
        buf.write("\u010d\u010f\5E#\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2")
        buf.write("\2\2\u010f\u0118\3\2\2\2\u0110\u0112\5C\"\2\u0111\u0110")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0111\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\5E#\2\u0116")
        buf.write("\u0118\3\2\2\2\u0117\u0100\3\2\2\2\u0117\u0111\3\2\2\2")
        buf.write("\u0118B\3\2\2\2\u0119\u011a\t\4\2\2\u011aD\3\2\2\2\u011b")
        buf.write("\u011d\t\5\2\2\u011c\u011e\t\6\2\2\u011d\u011c\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u0121\5")
        buf.write("C\"\2\u0120\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123F\3\2\2\2\u0124\u0128")
        buf.write("\t\7\2\2\u0125\u0127\t\b\2\2\u0126\u0125\3\2\2\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129H\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u0131\5K&\2")
        buf.write("\u012c\u0130\n\t\2\2\u012d\u0130\5O(\2\u012e\u0130\5M")
        buf.write("\'\2\u012f\u012c\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u0131\3\2\2\2")
        buf.write("\u0134\u0135\5K&\2\u0135\u0136\b%\3\2\u0136J\3\2\2\2\u0137")
        buf.write("\u0138\7$\2\2\u0138L\3\2\2\2\u0139\u013a\7)\2\2\u013a")
        buf.write("\u013b\7$\2\2\u013bN\3\2\2\2\u013c\u013d\7^\2\2\u013d")
        buf.write("\u013e\t\n\2\2\u013eP\3\2\2\2\u013f\u0140\7^\2\2\u0140")
        buf.write("\u0141\7^\2\2\u0141\u0142\n\n\2\2\u0142R\3\2\2\2\u0143")
        buf.write("\u0149\5K&\2\u0144\u0148\n\13\2\2\u0145\u0148\5M\'\2\u0146")
        buf.write("\u0148\5O(\2\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3")
        buf.write("\2\2\2\u014c\u014e\t\f\2\2\u014d\u014c\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u0150\b*\4\2\u0150T\3\2\2\2\u0151\u0157")
        buf.write("\5K&\2\u0152\u0156\n\r\2\2\u0153\u0156\5M\'\2\u0154\u0156")
        buf.write("\5O(\2\u0155\u0152\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u015e\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u015a\u015b\7^\2\2\u015b\u015f\n\n\2\2\u015c\u015d\t")
        buf.write("\16\2\2\u015d\u015f\n\17\2\2\u015e\u015a\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\b+\5\2")
        buf.write("\u0161V\3\2\2\2\u0162\u0164\t\20\2\2\u0163\u0162\3\2\2")
        buf.write("\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\b,\2\2\u0168")
        buf.write("X\3\2\2\2\u0169\u016a\13\2\2\2\u016a\u016b\b-\6\2\u016b")
        buf.write("Z\3\2\2\2\30\2m\u00d1\u00fd\u0102\u0108\u010b\u010e\u0113")
        buf.write("\u0117\u011d\u0122\u0128\u012f\u0131\u0147\u0149\u014d")
        buf.write("\u0155\u0157\u015e\u0165\7\b\2\2\3%\2\3*\3\3+\4\3-\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DYNAMIC_TYPE = 1
    VAR_TYPE = 2
    COMMENT = 3
    STRING_TYPE = 4
    STRING_OPERATOR = 5
    BOOL_TYPE = 6
    NOT_OPERATOR = 7
    AND_OPERATOR = 8
    OR_OPERATOR = 9
    NUMBER_TYPE = 10
    ADD_OPERATOR = 11
    SUB_OPERATOR = 12
    MUL_OPERATOR = 13
    DIV_OPERATOR = 14
    MOD_OPERATOR = 15
    KEYWORD = 16
    NEWLINE = 17
    EQ_OPERATOR = 18
    NEQ_OPERATOR = 19
    LT_OPERATOR = 20
    GT_OPERATOR = 21
    LEQ_OPERATOR = 22
    GEQ_OPERATOR = 23
    SEQ_OPERATOR = 24
    ASSIGN_OPERATOR = 25
    OPEN_PARENTHESIS = 26
    CLOSE_PARENTHESIS = 27
    OPEN_BRACKET = 28
    CLOSE_BRACKET = 29
    COMMA = 30
    BOOLEAN = 31
    NUMBER = 32
    IDENTIFIER = 33
    STRING = 34
    UNCLOSE_STRING = 35
    ILLEGAL_ESCAPE = 36
    WS = 37
    ERROR_CHAR = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'dynamic'", "'var'", "'string'", "'...'", "'bool'", "'not'", 
            "'and'", "'or'", "'number'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", "'<-'", 
            "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "DYNAMIC_TYPE", "VAR_TYPE", "COMMENT", "STRING_TYPE", "STRING_OPERATOR", 
            "BOOL_TYPE", "NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", 
            "NUMBER_TYPE", "ADD_OPERATOR", "SUB_OPERATOR", "MUL_OPERATOR", 
            "DIV_OPERATOR", "MOD_OPERATOR", "KEYWORD", "NEWLINE", "EQ_OPERATOR", 
            "NEQ_OPERATOR", "LT_OPERATOR", "GT_OPERATOR", "LEQ_OPERATOR", 
            "GEQ_OPERATOR", "SEQ_OPERATOR", "ASSIGN_OPERATOR", "OPEN_PARENTHESIS", 
            "CLOSE_PARENTHESIS", "OPEN_BRACKET", "CLOSE_BRACKET", "COMMA", 
            "BOOLEAN", "NUMBER", "IDENTIFIER", "STRING", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    ruleNames = [ "DYNAMIC_TYPE", "VAR_TYPE", "COMMENT", "STRING_TYPE", 
                  "STRING_OPERATOR", "BOOL_TYPE", "NOT_OPERATOR", "AND_OPERATOR", 
                  "OR_OPERATOR", "NUMBER_TYPE", "ADD_OPERATOR", "SUB_OPERATOR", 
                  "MUL_OPERATOR", "DIV_OPERATOR", "MOD_OPERATOR", "KEYWORD", 
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
            actions[35] = self.STRING_action 
            actions[40] = self.UNCLOSE_STRING_action 
            actions[41] = self.ILLEGAL_ESCAPE_action 
            actions[43] = self.ERROR_CHAR_action 
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
     


