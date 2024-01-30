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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u0186\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\7\6\u0088\n\6\f\6\16\6\u008b\13\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00ec\n\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3")
        buf.write("\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0118")
        buf.write("\n\"\3#\6#\u011b\n#\r#\16#\u011c\3#\3#\7#\u0121\n#\f#")
        buf.write("\16#\u0124\13#\5#\u0126\n#\3#\5#\u0129\n#\3#\6#\u012c")
        buf.write("\n#\r#\16#\u012d\3#\3#\5#\u0132\n#\3$\3$\3%\3%\5%\u0138")
        buf.write("\n%\3%\6%\u013b\n%\r%\16%\u013c\3&\3&\7&\u0141\n&\f&\16")
        buf.write("&\u0144\13&\3\'\3\'\3\'\3\'\7\'\u014a\n\'\f\'\16\'\u014d")
        buf.write("\13\'\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+")
        buf.write("\3,\3,\3,\3,\7,\u0162\n,\f,\16,\u0165\13,\3,\5,\u0168")
        buf.write("\n,\3,\3,\3-\3-\3-\3-\7-\u0170\n-\f-\16-\u0173\13-\3-")
        buf.write("\3-\3-\3-\5-\u0179\n-\3-\3-\3.\6.\u017e\n.\r.\16.\u017f")
        buf.write("\3.\3.\3/\3/\3/\2\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G\2I\2K%M&O\2Q\2S\2U\2W\'Y([)]*\3\2\21\4\2")
        buf.write("\f\f\17\17\3\2\f\f\3\2\62;\4\2GGgg\4\2--//\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv")
        buf.write("\5\2$$))^^\4\3\f\f\17\17\5\2\f\f\17\17$$\3\2))\3\2$$\5")
        buf.write("\2\n\13\16\17\"\"\2\u01a0\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5g\3\2\2\2\7w\3\2\2\2\t\177")
        buf.write("\3\2\2\2\13\u0083\3\2\2\2\r\u008c\3\2\2\2\17\u0093\3\2")
        buf.write("\2\2\21\u0097\3\2\2\2\23\u009c\3\2\2\2\25\u00a0\3\2\2")
        buf.write("\2\27\u00a4\3\2\2\2\31\u00a7\3\2\2\2\33\u00ae\3\2\2\2")
        buf.write("\35\u00b0\3\2\2\2\37\u00b2\3\2\2\2!\u00b4\3\2\2\2#\u00b6")
        buf.write("\3\2\2\2%\u00eb\3\2\2\2\'\u00ed\3\2\2\2)\u00ef\3\2\2\2")
        buf.write("+\u00f1\3\2\2\2-\u00f4\3\2\2\2/\u00f6\3\2\2\2\61\u00f8")
        buf.write("\3\2\2\2\63\u00fb\3\2\2\2\65\u00fe\3\2\2\2\67\u0101\3")
        buf.write("\2\2\29\u0104\3\2\2\2;\u0106\3\2\2\2=\u0108\3\2\2\2?\u010a")
        buf.write("\3\2\2\2A\u010c\3\2\2\2C\u0117\3\2\2\2E\u0131\3\2\2\2")
        buf.write("G\u0133\3\2\2\2I\u0135\3\2\2\2K\u013e\3\2\2\2M\u0145\3")
        buf.write("\2\2\2O\u0151\3\2\2\2Q\u0153\3\2\2\2S\u0156\3\2\2\2U\u0159")
        buf.write("\3\2\2\2W\u015d\3\2\2\2Y\u016b\3\2\2\2[\u017d\3\2\2\2")
        buf.write("]\u0183\3\2\2\2_`\7q\2\2`a\7r\2\2ab\7g\2\2bc\7t\2\2cd")
        buf.write("\7c\2\2de\7p\2\2ef\7f\2\2f\4\3\2\2\2gh\7c\2\2hi\7t\2\2")
        buf.write("ij\7t\2\2jk\7c\2\2kl\7{\2\2lm\7g\2\2mn\7z\2\2no\7r\2\2")
        buf.write("op\7t\2\2pq\7g\2\2qr\7u\2\2rs\7u\2\2st\7k\2\2tu\7q\2\2")
        buf.write("uv\7p\2\2v\6\3\2\2\2wx\7f\2\2xy\7{\2\2yz\7p\2\2z{\7c\2")
        buf.write("\2{|\7o\2\2|}\7k\2\2}~\7e\2\2~\b\3\2\2\2\177\u0080\7x")
        buf.write("\2\2\u0080\u0081\7c\2\2\u0081\u0082\7t\2\2\u0082\n\3\2")
        buf.write("\2\2\u0083\u0084\7%\2\2\u0084\u0085\7%\2\2\u0085\u0089")
        buf.write("\3\2\2\2\u0086\u0088\n\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\u008b\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\f\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\7u\2")
        buf.write("\2\u008d\u008e\7v\2\2\u008e\u008f\7t\2\2\u008f\u0090\7")
        buf.write("k\2\2\u0090\u0091\7p\2\2\u0091\u0092\7i\2\2\u0092\16\3")
        buf.write("\2\2\2\u0093\u0094\7\60\2\2\u0094\u0095\7\60\2\2\u0095")
        buf.write("\u0096\7\60\2\2\u0096\20\3\2\2\2\u0097\u0098\7d\2\2\u0098")
        buf.write("\u0099\7q\2\2\u0099\u009a\7q\2\2\u009a\u009b\7n\2\2\u009b")
        buf.write("\22\3\2\2\2\u009c\u009d\7p\2\2\u009d\u009e\7q\2\2\u009e")
        buf.write("\u009f\7v\2\2\u009f\24\3\2\2\2\u00a0\u00a1\7c\2\2\u00a1")
        buf.write("\u00a2\7p\2\2\u00a2\u00a3\7f\2\2\u00a3\26\3\2\2\2\u00a4")
        buf.write("\u00a5\7q\2\2\u00a5\u00a6\7t\2\2\u00a6\30\3\2\2\2\u00a7")
        buf.write("\u00a8\7p\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa\7o\2\2\u00aa")
        buf.write("\u00ab\7d\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7t\2\2\u00ad")
        buf.write("\32\3\2\2\2\u00ae\u00af\7-\2\2\u00af\34\3\2\2\2\u00b0")
        buf.write("\u00b1\7/\2\2\u00b1\36\3\2\2\2\u00b2\u00b3\7,\2\2\u00b3")
        buf.write(" \3\2\2\2\u00b4\u00b5\7\61\2\2\u00b5\"\3\2\2\2\u00b6\u00b7")
        buf.write("\7\'\2\2\u00b7$\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00ec\7p\2\2\u00be\u00bf\7h\2\2\u00bf\u00c0")
        buf.write("\7w\2\2\u00c0\u00c1\7p\2\2\u00c1\u00ec\7e\2\2\u00c2\u00c3")
        buf.write("\7h\2\2\u00c3\u00c4\7q\2\2\u00c4\u00ec\7t\2\2\u00c5\u00c6")
        buf.write("\7w\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9")
        buf.write("\7k\2\2\u00c9\u00ec\7n\2\2\u00ca\u00cb\7d\2\2\u00cb\u00ec")
        buf.write("\7{\2\2\u00cc\u00cd\7d\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00ec\7m\2\2\u00d1\u00d2")
        buf.write("\7e\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5")
        buf.write("\7v\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7w\2\2\u00d8\u00ec\7g\2\2\u00d9\u00da\7k\2\2\u00da\u00ec")
        buf.write("\7h\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de")
        buf.write("\7u\2\2\u00de\u00ec\7g\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1")
        buf.write("\7n\2\2\u00e1\u00e2\7k\2\2\u00e2\u00ec\7h\2\2\u00e3\u00e4")
        buf.write("\7d\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7i\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00ec\7p\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00ec\7f\2\2\u00eb\u00b8\3\2\2\2\u00eb\u00be")
        buf.write("\3\2\2\2\u00eb\u00c2\3\2\2\2\u00eb\u00c5\3\2\2\2\u00eb")
        buf.write("\u00ca\3\2\2\2\u00eb\u00cc\3\2\2\2\u00eb\u00d1\3\2\2\2")
        buf.write("\u00eb\u00d9\3\2\2\2\u00eb\u00db\3\2\2\2\u00eb\u00df\3")
        buf.write("\2\2\2\u00eb\u00e3\3\2\2\2\u00eb\u00e8\3\2\2\2\u00ec&")
        buf.write("\3\2\2\2\u00ed\u00ee\t\3\2\2\u00ee(\3\2\2\2\u00ef\u00f0")
        buf.write("\7?\2\2\u00f0*\3\2\2\2\u00f1\u00f2\7#\2\2\u00f2\u00f3")
        buf.write("\7?\2\2\u00f3,\3\2\2\2\u00f4\u00f5\7>\2\2\u00f5.\3\2\2")
        buf.write("\2\u00f6\u00f7\7@\2\2\u00f7\60\3\2\2\2\u00f8\u00f9\7>")
        buf.write("\2\2\u00f9\u00fa\7?\2\2\u00fa\62\3\2\2\2\u00fb\u00fc\7")
        buf.write("@\2\2\u00fc\u00fd\7?\2\2\u00fd\64\3\2\2\2\u00fe\u00ff")
        buf.write("\7?\2\2\u00ff\u0100\7?\2\2\u0100\66\3\2\2\2\u0101\u0102")
        buf.write("\7>\2\2\u0102\u0103\7/\2\2\u01038\3\2\2\2\u0104\u0105")
        buf.write("\7*\2\2\u0105:\3\2\2\2\u0106\u0107\7+\2\2\u0107<\3\2\2")
        buf.write("\2\u0108\u0109\7]\2\2\u0109>\3\2\2\2\u010a\u010b\7_\2")
        buf.write("\2\u010b@\3\2\2\2\u010c\u010d\7.\2\2\u010dB\3\2\2\2\u010e")
        buf.write("\u010f\7v\2\2\u010f\u0110\7t\2\2\u0110\u0111\7w\2\2\u0111")
        buf.write("\u0118\7g\2\2\u0112\u0113\7h\2\2\u0113\u0114\7c\2\2\u0114")
        buf.write("\u0115\7n\2\2\u0115\u0116\7u\2\2\u0116\u0118\7g\2\2\u0117")
        buf.write("\u010e\3\2\2\2\u0117\u0112\3\2\2\2\u0118D\3\2\2\2\u0119")
        buf.write("\u011b\5G$\2\u011a\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u0125\3\2\2\2")
        buf.write("\u011e\u0122\7\60\2\2\u011f\u0121\5G$\2\u0120\u011f\3")
        buf.write("\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0125")
        buf.write("\u011e\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2")
        buf.write("\u0127\u0129\5I%\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2")
        buf.write("\2\2\u0129\u0132\3\2\2\2\u012a\u012c\5G$\2\u012b\u012a")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\5I%\2\u0130")
        buf.write("\u0132\3\2\2\2\u0131\u011a\3\2\2\2\u0131\u012b\3\2\2\2")
        buf.write("\u0132F\3\2\2\2\u0133\u0134\t\4\2\2\u0134H\3\2\2\2\u0135")
        buf.write("\u0137\t\5\2\2\u0136\u0138\t\6\2\2\u0137\u0136\3\2\2\2")
        buf.write("\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b\5")
        buf.write("G$\2\u013a\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013dJ\3\2\2\2\u013e\u0142")
        buf.write("\t\7\2\2\u013f\u0141\t\b\2\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143L\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u014b\5O(\2")
        buf.write("\u0146\u014a\n\t\2\2\u0147\u014a\5S*\2\u0148\u014a\5Q")
        buf.write(")\2\u0149\u0146\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u0148")
        buf.write("\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u014b\3\2\2\2")
        buf.write("\u014e\u014f\5O(\2\u014f\u0150\b\'\2\2\u0150N\3\2\2\2")
        buf.write("\u0151\u0152\7$\2\2\u0152P\3\2\2\2\u0153\u0154\7)\2\2")
        buf.write("\u0154\u0155\7$\2\2\u0155R\3\2\2\2\u0156\u0157\7^\2\2")
        buf.write("\u0157\u0158\t\n\2\2\u0158T\3\2\2\2\u0159\u015a\7^\2\2")
        buf.write("\u015a\u015b\7^\2\2\u015b\u015c\n\n\2\2\u015cV\3\2\2\2")
        buf.write("\u015d\u0163\5O(\2\u015e\u0162\n\13\2\2\u015f\u0162\5")
        buf.write("Q)\2\u0160\u0162\5S*\2\u0161\u015e\3\2\2\2\u0161\u015f")
        buf.write("\3\2\2\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0166\u0168\t\f\2\2\u0167\u0166\3")
        buf.write("\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a\b,\3\2\u016aX\3")
        buf.write("\2\2\2\u016b\u0171\5O(\2\u016c\u0170\n\r\2\2\u016d\u0170")
        buf.write("\5Q)\2\u016e\u0170\5S*\2\u016f\u016c\3\2\2\2\u016f\u016d")
        buf.write("\3\2\2\2\u016f\u016e\3\2\2\2\u0170\u0173\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0178\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0174\u0175\7^\2\2\u0175\u0179\n")
        buf.write("\n\2\2\u0176\u0177\t\16\2\2\u0177\u0179\n\17\2\2\u0178")
        buf.write("\u0174\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u017b\b-\4\2\u017bZ\3\2\2\2\u017c\u017e\t\20\2")
        buf.write("\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0182\b.\5\2\u0182\\\3\2\2\2\u0183\u0184\13\2\2\2\u0184")
        buf.write("\u0185\b/\6\2\u0185^\3\2\2\2\30\2\u0089\u00eb\u0117\u011c")
        buf.write("\u0122\u0125\u0128\u012d\u0131\u0137\u013c\u0142\u0149")
        buf.write("\u014b\u0161\u0163\u0167\u016f\u0171\u0178\u017f\7\3\'")
        buf.write("\2\3,\3\3-\4\b\2\2\3/\5")
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
    NOT_OPERATOR = 9
    AND_OPERATOR = 10
    OR_OPERATOR = 11
    NUMBER_TYPE = 12
    ADD_OPERATOR = 13
    SUB_OPERATOR = 14
    MUL_OPERATOR = 15
    DIV_OPERATOR = 16
    MOD_OPERATOR = 17
    KEYWORD = 18
    NEWLINE = 19
    EQ_OPERATOR = 20
    NEQ_OPERATOR = 21
    LT_OPERATOR = 22
    GT_OPERATOR = 23
    LEQ_OPERATOR = 24
    GEQ_OPERATOR = 25
    SEQ_OPERATOR = 26
    ASSIGN_OPERATOR = 27
    OPEN_PARENTHESIS = 28
    CLOSE_PARENTHESIS = 29
    OPEN_BRACKET = 30
    CLOSE_BRACKET = 31
    COMMA = 32
    BOOLEAN = 33
    NUMBER = 34
    IDENTIFIER = 35
    STRING = 36
    UNCLOSE_STRING = 37
    ILLEGAL_ESCAPE = 38
    WS = 39
    ERROR_CHAR = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'operand'", "'arrayexpression'", "'dynamic'", "'var'", "'string'", 
            "'...'", "'bool'", "'not'", "'and'", "'or'", "'number'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=='", "'<-'", "'('", "')'", "'['", "']'", "','" ]

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

    ruleNames = [ "T__0", "T__1", "DYNAMIC_TYPE", "VAR_TYPE", "COMMENT", 
                  "STRING_TYPE", "STRING_OPERATOR", "BOOL_TYPE", "NOT_OPERATOR", 
                  "AND_OPERATOR", "OR_OPERATOR", "NUMBER_TYPE", "ADD_OPERATOR", 
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
            actions[37] = self.STRING_action 
            actions[42] = self.UNCLOSE_STRING_action 
            actions[43] = self.ILLEGAL_ESCAPE_action 
            actions[45] = self.ERROR_CHAR_action 
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
     


