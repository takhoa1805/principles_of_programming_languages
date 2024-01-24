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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("\u011b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\7\2\66\n\2\f\2\16\29\13\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0080")
        buf.write("\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\u009c\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00a3\n\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\f\u00b0\n\f")
        buf.write("\r\f\16\f\u00b1\3\f\3\f\7\f\u00b6\n\f\f\f\16\f\u00b9\13")
        buf.write("\f\5\f\u00bb\n\f\3\f\5\f\u00be\n\f\3\f\6\f\u00c1\n\f\r")
        buf.write("\f\16\f\u00c2\3\f\3\f\5\f\u00c7\n\f\3\r\3\r\3\16\3\16")
        buf.write("\5\16\u00cd\n\16\3\16\6\16\u00d0\n\16\r\16\16\16\u00d1")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u00d8\n\17\f\17\16\17\u00db")
        buf.write("\13\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\7\24")
        buf.write("\u00f0\n\24\f\24\16\24\u00f3\13\24\3\24\5\24\u00f6\n\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u00fe\n\25\f\25\16")
        buf.write("\25\u0101\13\25\3\25\3\25\3\25\3\25\5\25\u0107\n\25\3")
        buf.write("\25\3\25\3\26\3\26\7\26\u010d\n\26\f\26\16\26\u0110\13")
        buf.write("\26\3\27\6\27\u0113\n\27\r\27\16\27\u0114\3\27\3\27\3")
        buf.write("\30\3\30\3\30\2\2\31\3\3\5\4\7\5\t\6\13\7\r\2\17\2\21")
        buf.write("\2\23\2\25\2\27\b\31\2\33\2\35\t\37\2!\2#\2%\2\'\n)\13")
        buf.write("+\f-\r/\16\3\2\23\4\2\f\f\17\17\3\2\f\f\6\2\'\',-//\61")
        buf.write("\61\4\2>>@@\3\2\62;\4\2GGgg\4\2--//\7\2\f\f\17\17$$))")
        buf.write("^^\t\2))^^ddhhppttvv\5\2$$))^^\4\3\f\f\17\17\5\2\f\f\17")
        buf.write("\17$$\3\2))\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16")
        buf.write("\17\"\"\2\u0142\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3")
        buf.write("\61\3\2\2\2\5\177\3\2\2\2\7\u0081\3\2\2\2\t\u009b\3\2")
        buf.write("\2\2\13\u00a2\3\2\2\2\r\u00a4\3\2\2\2\17\u00a6\3\2\2\2")
        buf.write("\21\u00a8\3\2\2\2\23\u00aa\3\2\2\2\25\u00ac\3\2\2\2\27")
        buf.write("\u00c6\3\2\2\2\31\u00c8\3\2\2\2\33\u00ca\3\2\2\2\35\u00d3")
        buf.write("\3\2\2\2\37\u00df\3\2\2\2!\u00e1\3\2\2\2#\u00e4\3\2\2")
        buf.write("\2%\u00e7\3\2\2\2\'\u00eb\3\2\2\2)\u00f9\3\2\2\2+\u010a")
        buf.write("\3\2\2\2-\u0112\3\2\2\2/\u0118\3\2\2\2\61\62\7%\2\2\62")
        buf.write("\63\7%\2\2\63\67\3\2\2\2\64\66\n\2\2\2\65\64\3\2\2\2\66")
        buf.write("9\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\4\3\2\2\29\67\3\2")
        buf.write("\2\2:;\7p\2\2;<\7w\2\2<=\7o\2\2=>\7d\2\2>?\7g\2\2?\u0080")
        buf.write("\7t\2\2@A\7d\2\2AB\7q\2\2BC\7q\2\2C\u0080\7n\2\2DE\7t")
        buf.write("\2\2EF\7g\2\2FG\7v\2\2GH\7w\2\2HI\7t\2\2I\u0080\7p\2\2")
        buf.write("JK\7x\2\2KL\7c\2\2L\u0080\7t\2\2MN\7f\2\2NO\7{\2\2OP\7")
        buf.write("p\2\2PQ\7c\2\2QR\7o\2\2RS\7k\2\2S\u0080\7e\2\2TU\7h\2")
        buf.write("\2UV\7w\2\2VW\7p\2\2W\u0080\7e\2\2XY\7h\2\2YZ\7q\2\2Z")
        buf.write("\u0080\7t\2\2[\\\7w\2\2\\]\7p\2\2]^\7v\2\2^_\7k\2\2_\u0080")
        buf.write("\7n\2\2`a\7d\2\2a\u0080\7{\2\2bc\7d\2\2cd\7t\2\2de\7g")
        buf.write("\2\2ef\7c\2\2f\u0080\7m\2\2gh\7k\2\2h\u0080\7h\2\2ij\7")
        buf.write("g\2\2jk\7n\2\2kl\7u\2\2l\u0080\7g\2\2mn\7g\2\2no\7n\2")
        buf.write("\2op\7k\2\2p\u0080\7h\2\2qr\7d\2\2rs\7g\2\2st\7i\2\2t")
        buf.write("u\7k\2\2u\u0080\7p\2\2vw\7v\2\2wx\7t\2\2xy\7w\2\2y\u0080")
        buf.write("\7g\2\2z{\7h\2\2{|\7c\2\2|}\7n\2\2}~\7u\2\2~\u0080\7g")
        buf.write("\2\2\177:\3\2\2\2\177@\3\2\2\2\177D\3\2\2\2\177J\3\2\2")
        buf.write("\2\177M\3\2\2\2\177T\3\2\2\2\177X\3\2\2\2\177[\3\2\2\2")
        buf.write("\177`\3\2\2\2\177b\3\2\2\2\177g\3\2\2\2\177i\3\2\2\2\177")
        buf.write("m\3\2\2\2\177q\3\2\2\2\177v\3\2\2\2\177z\3\2\2\2\u0080")
        buf.write("\6\3\2\2\2\u0081\u0082\t\3\2\2\u0082\b\3\2\2\2\u0083\u009c")
        buf.write("\t\4\2\2\u0084\u0085\7>\2\2\u0085\u009c\7/\2\2\u0086\u0087")
        buf.write("\7p\2\2\u0087\u0088\7q\2\2\u0088\u009c\7v\2\2\u0089\u008a")
        buf.write("\7c\2\2\u008a\u008b\7p\2\2\u008b\u009c\7f\2\2\u008c\u008d")
        buf.write("\7q\2\2\u008d\u009c\7t\2\2\u008e\u009c\7?\2\2\u008f\u0090")
        buf.write("\7#\2\2\u0090\u009c\7?\2\2\u0091\u009c\t\5\2\2\u0092\u0093")
        buf.write("\7>\2\2\u0093\u009c\7?\2\2\u0094\u0095\7@\2\2\u0095\u009c")
        buf.write("\7?\2\2\u0096\u0097\7\60\2\2\u0097\u0098\7\60\2\2\u0098")
        buf.write("\u009c\7\60\2\2\u0099\u009a\7?\2\2\u009a\u009c\7?\2\2")
        buf.write("\u009b\u0083\3\2\2\2\u009b\u0084\3\2\2\2\u009b\u0086\3")
        buf.write("\2\2\2\u009b\u0089\3\2\2\2\u009b\u008c\3\2\2\2\u009b\u008e")
        buf.write("\3\2\2\2\u009b\u008f\3\2\2\2\u009b\u0091\3\2\2\2\u009b")
        buf.write("\u0092\3\2\2\2\u009b\u0094\3\2\2\2\u009b\u0096\3\2\2\2")
        buf.write("\u009b\u0099\3\2\2\2\u009c\n\3\2\2\2\u009d\u00a3\5\21")
        buf.write("\t\2\u009e\u00a3\5\23\n\2\u009f\u00a3\5\r\7\2\u00a0\u00a3")
        buf.write("\5\17\b\2\u00a1\u00a3\5\25\13\2\u00a2\u009d\3\2\2\2\u00a2")
        buf.write("\u009e\3\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a1\3\2\2\2\u00a3\f\3\2\2\2\u00a4\u00a5\7*\2")
        buf.write("\2\u00a5\16\3\2\2\2\u00a6\u00a7\7+\2\2\u00a7\20\3\2\2")
        buf.write("\2\u00a8\u00a9\7]\2\2\u00a9\22\3\2\2\2\u00aa\u00ab\7_")
        buf.write("\2\2\u00ab\24\3\2\2\2\u00ac\u00ad\7.\2\2\u00ad\26\3\2")
        buf.write("\2\2\u00ae\u00b0\5\31\r\2\u00af\u00ae\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00ba\3\2\2\2\u00b3\u00b7\7\60\2\2\u00b4\u00b6\5\31\r")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00b3\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bd\3\2\2\2\u00bc\u00be\5\33\16\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c7\3\2\2\2\u00bf")
        buf.write("\u00c1\5\31\r\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2")
        buf.write("\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\5\33\16\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00af\3\2\2\2\u00c6\u00c0\3\2\2\2\u00c7\30\3\2\2\2\u00c8")
        buf.write("\u00c9\t\6\2\2\u00c9\32\3\2\2\2\u00ca\u00cc\t\7\2\2\u00cb")
        buf.write("\u00cd\t\b\2\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\u00cf\3\2\2\2\u00ce\u00d0\5\31\r\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\34\3\2\2\2\u00d3\u00d9\5\37\20\2")
        buf.write("\u00d4\u00d8\n\t\2\2\u00d5\u00d8\5#\22\2\u00d6\u00d8\5")
        buf.write("!\21\2\u00d7\u00d4\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00dc\u00dd\5\37\20\2\u00dd\u00de\b\17\2\2\u00de\36\3")
        buf.write("\2\2\2\u00df\u00e0\7$\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7")
        buf.write(")\2\2\u00e2\u00e3\7$\2\2\u00e3\"\3\2\2\2\u00e4\u00e5\7")
        buf.write("^\2\2\u00e5\u00e6\t\n\2\2\u00e6$\3\2\2\2\u00e7\u00e8\7")
        buf.write("^\2\2\u00e8\u00e9\7^\2\2\u00e9\u00ea\n\n\2\2\u00ea&\3")
        buf.write("\2\2\2\u00eb\u00f1\5\37\20\2\u00ec\u00f0\n\13\2\2\u00ed")
        buf.write("\u00f0\5!\21\2\u00ee\u00f0\5#\22\2\u00ef\u00ec\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3")
        buf.write("\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f5")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f6\t\f\2\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\b\24\3")
        buf.write("\2\u00f8(\3\2\2\2\u00f9\u00ff\5\37\20\2\u00fa\u00fe\n")
        buf.write("\r\2\2\u00fb\u00fe\5!\21\2\u00fc\u00fe\5#\22\2\u00fd\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe")
        buf.write("\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0106\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103\7")
        buf.write("^\2\2\u0103\u0107\n\n\2\2\u0104\u0105\t\16\2\2\u0105\u0107")
        buf.write("\n\17\2\2\u0106\u0102\3\2\2\2\u0106\u0104\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u0109\b\25\4\2\u0109*\3\2\2\2\u010a")
        buf.write("\u010e\t\20\2\2\u010b\u010d\t\21\2\2\u010c\u010b\3\2\2")
        buf.write("\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f,\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0113")
        buf.write("\t\22\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0117\b\27\5\2\u0117.\3\2\2\2\u0118\u0119\13\2")
        buf.write("\2\2\u0119\u011a\b\30\6\2\u011a\60\3\2\2\2\31\2\67\177")
        buf.write("\u009b\u00a2\u00b1\u00b7\u00ba\u00bd\u00c2\u00c6\u00cc")
        buf.write("\u00d1\u00d7\u00d9\u00ef\u00f1\u00f5\u00fd\u00ff\u0106")
        buf.write("\u010e\u0114\7\3\17\2\3\24\3\3\25\4\b\2\2\3\30\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    KEYWORD = 2
    CHARSET = 3
    OPERATOR = 4
    SEPARATOR = 5
    NUMBER = 6
    STRING = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9
    IDENTIFIER = 10
    WS = 11
    ERROR_CHAR = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "KEYWORD", "CHARSET", "OPERATOR", "SEPARATOR", "NUMBER", 
            "STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "IDENTIFIER", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "KEYWORD", "CHARSET", "OPERATOR", "SEPARATOR", 
                  "OPEN_PARENTHESIS", "CLOSE_PARENTHESIS", "OPEN_BRACKET", 
                  "CLOSE_BRACKET", "COMMA", "NUMBER", "DIGIT", "EXPONENT", 
                  "STRING", "DOUBLE_QUOTE", "DOUBLE_QUOTE_NOTATION", "LEGAL_ESCAPE_SEQUENCE", 
                  "ILLEGAL_ESCAPE_SEQUENCE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "IDENTIFIER", "WS", "ERROR_CHAR" ]

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
            actions[13] = self.STRING_action 
            actions[18] = self.UNCLOSE_STRING_action 
            actions[19] = self.ILLEGAL_ESCAPE_action 
            actions[22] = self.ERROR_CHAR_action 
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
     


