# Generated from c://Users//takho//Desktop//initial//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,12,290,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,126,8,1,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,154,8,3,1,4,1,4,1,4,1,4,1,4,3,4,161,8,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,174,8,10,11,10,
        12,10,175,1,10,1,10,5,10,180,8,10,10,10,12,10,183,9,10,3,10,185,
        8,10,1,10,3,10,188,8,10,1,10,4,10,191,8,10,11,10,12,10,192,1,10,
        1,10,3,10,197,8,10,1,11,1,11,1,12,1,12,3,12,203,8,12,1,12,4,12,206,
        8,12,11,12,12,12,207,1,13,1,13,1,13,1,13,5,13,214,8,13,10,13,12,
        13,217,9,13,1,13,5,13,220,8,13,10,13,12,13,223,9,13,1,13,1,13,1,
        13,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,5,18,246,8,18,10,18,12,18,249,9,18,1,
        18,3,18,252,8,18,1,18,1,18,1,19,1,19,1,19,5,19,259,8,19,10,19,12,
        19,262,9,19,1,19,5,19,265,8,19,10,19,12,19,268,9,19,1,19,1,19,1,
        19,1,19,1,20,1,20,5,20,276,8,20,10,20,12,20,279,9,20,1,21,4,21,282,
        8,21,11,21,12,21,283,1,21,1,21,1,22,1,22,1,22,0,0,23,1,1,3,2,5,3,
        7,4,9,5,11,0,13,0,15,0,17,0,19,0,21,6,23,0,25,0,27,7,29,0,31,0,33,
        0,35,0,37,8,39,9,41,10,43,11,45,12,1,0,13,2,0,10,10,13,13,1,0,10,
        10,4,0,37,37,42,43,45,45,47,47,2,0,60,60,62,62,1,0,48,57,2,0,69,
        69,101,101,2,0,43,43,45,45,7,0,39,39,92,92,98,98,102,102,110,110,
        114,114,116,116,1,0,34,34,1,1,10,10,3,0,65,90,95,95,97,122,4,0,48,
        57,65,90,95,95,97,122,3,0,8,9,12,13,32,32,329,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,21,1,0,0,0,0,27,1,0,
        0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,
        0,0,1,47,1,0,0,0,3,125,1,0,0,0,5,127,1,0,0,0,7,153,1,0,0,0,9,160,
        1,0,0,0,11,162,1,0,0,0,13,164,1,0,0,0,15,166,1,0,0,0,17,168,1,0,
        0,0,19,170,1,0,0,0,21,196,1,0,0,0,23,198,1,0,0,0,25,200,1,0,0,0,
        27,209,1,0,0,0,29,227,1,0,0,0,31,229,1,0,0,0,33,232,1,0,0,0,35,237,
        1,0,0,0,37,241,1,0,0,0,39,255,1,0,0,0,41,273,1,0,0,0,43,281,1,0,
        0,0,45,287,1,0,0,0,47,48,5,35,0,0,48,49,5,35,0,0,49,53,1,0,0,0,50,
        52,8,0,0,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,
        0,54,2,1,0,0,0,55,53,1,0,0,0,56,57,5,110,0,0,57,58,5,117,0,0,58,
        59,5,109,0,0,59,60,5,98,0,0,60,61,5,101,0,0,61,126,5,114,0,0,62,
        63,5,98,0,0,63,64,5,111,0,0,64,65,5,111,0,0,65,126,5,108,0,0,66,
        67,5,114,0,0,67,68,5,101,0,0,68,69,5,116,0,0,69,70,5,117,0,0,70,
        71,5,114,0,0,71,126,5,110,0,0,72,73,5,118,0,0,73,74,5,97,0,0,74,
        126,5,114,0,0,75,76,5,100,0,0,76,77,5,121,0,0,77,78,5,110,0,0,78,
        79,5,97,0,0,79,80,5,109,0,0,80,81,5,105,0,0,81,126,5,99,0,0,82,83,
        5,102,0,0,83,84,5,117,0,0,84,85,5,110,0,0,85,126,5,99,0,0,86,87,
        5,102,0,0,87,88,5,111,0,0,88,126,5,114,0,0,89,90,5,117,0,0,90,91,
        5,110,0,0,91,92,5,116,0,0,92,93,5,105,0,0,93,126,5,108,0,0,94,95,
        5,98,0,0,95,126,5,121,0,0,96,97,5,98,0,0,97,98,5,114,0,0,98,99,5,
        101,0,0,99,100,5,97,0,0,100,126,5,107,0,0,101,102,5,105,0,0,102,
        126,5,102,0,0,103,104,5,101,0,0,104,105,5,108,0,0,105,106,5,115,
        0,0,106,126,5,101,0,0,107,108,5,101,0,0,108,109,5,108,0,0,109,110,
        5,105,0,0,110,126,5,102,0,0,111,112,5,98,0,0,112,113,5,101,0,0,113,
        114,5,103,0,0,114,115,5,105,0,0,115,126,5,110,0,0,116,117,5,116,
        0,0,117,118,5,114,0,0,118,119,5,117,0,0,119,126,5,101,0,0,120,121,
        5,102,0,0,121,122,5,97,0,0,122,123,5,108,0,0,123,124,5,115,0,0,124,
        126,5,101,0,0,125,56,1,0,0,0,125,62,1,0,0,0,125,66,1,0,0,0,125,72,
        1,0,0,0,125,75,1,0,0,0,125,82,1,0,0,0,125,86,1,0,0,0,125,89,1,0,
        0,0,125,94,1,0,0,0,125,96,1,0,0,0,125,101,1,0,0,0,125,103,1,0,0,
        0,125,107,1,0,0,0,125,111,1,0,0,0,125,116,1,0,0,0,125,120,1,0,0,
        0,126,4,1,0,0,0,127,128,7,1,0,0,128,6,1,0,0,0,129,154,7,2,0,0,130,
        131,5,60,0,0,131,154,5,45,0,0,132,133,5,110,0,0,133,134,5,111,0,
        0,134,154,5,116,0,0,135,136,5,97,0,0,136,137,5,110,0,0,137,154,5,
        100,0,0,138,139,5,111,0,0,139,154,5,114,0,0,140,154,5,61,0,0,141,
        142,5,33,0,0,142,154,5,61,0,0,143,154,7,3,0,0,144,145,5,60,0,0,145,
        154,5,61,0,0,146,147,5,62,0,0,147,154,5,61,0,0,148,149,5,46,0,0,
        149,150,5,46,0,0,150,154,5,46,0,0,151,152,5,61,0,0,152,154,5,61,
        0,0,153,129,1,0,0,0,153,130,1,0,0,0,153,132,1,0,0,0,153,135,1,0,
        0,0,153,138,1,0,0,0,153,140,1,0,0,0,153,141,1,0,0,0,153,143,1,0,
        0,0,153,144,1,0,0,0,153,146,1,0,0,0,153,148,1,0,0,0,153,151,1,0,
        0,0,154,8,1,0,0,0,155,161,3,15,7,0,156,161,3,17,8,0,157,161,3,11,
        5,0,158,161,3,13,6,0,159,161,3,19,9,0,160,155,1,0,0,0,160,156,1,
        0,0,0,160,157,1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,10,1,0,
        0,0,162,163,5,40,0,0,163,12,1,0,0,0,164,165,5,41,0,0,165,14,1,0,
        0,0,166,167,5,91,0,0,167,16,1,0,0,0,168,169,5,93,0,0,169,18,1,0,
        0,0,170,171,5,44,0,0,171,20,1,0,0,0,172,174,3,23,11,0,173,172,1,
        0,0,0,174,175,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,184,1,
        0,0,0,177,181,5,46,0,0,178,180,3,23,11,0,179,178,1,0,0,0,180,183,
        1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,185,1,0,0,0,183,181,
        1,0,0,0,184,177,1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,188,
        3,25,12,0,187,186,1,0,0,0,187,188,1,0,0,0,188,197,1,0,0,0,189,191,
        3,23,11,0,190,189,1,0,0,0,191,192,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,194,1,0,0,0,194,195,3,25,12,0,195,197,1,0,0,0,196,173,
        1,0,0,0,196,190,1,0,0,0,197,22,1,0,0,0,198,199,7,4,0,0,199,24,1,
        0,0,0,200,202,7,5,0,0,201,203,7,6,0,0,202,201,1,0,0,0,202,203,1,
        0,0,0,203,205,1,0,0,0,204,206,3,23,11,0,205,204,1,0,0,0,206,207,
        1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,26,1,0,0,0,209,215,3,
        29,14,0,210,214,8,1,0,0,211,214,3,31,15,0,212,214,3,33,16,0,213,
        210,1,0,0,0,213,211,1,0,0,0,213,212,1,0,0,0,214,217,1,0,0,0,215,
        213,1,0,0,0,215,216,1,0,0,0,216,221,1,0,0,0,217,215,1,0,0,0,218,
        220,3,33,16,0,219,218,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,
        222,1,0,0,0,222,224,1,0,0,0,223,221,1,0,0,0,224,225,3,29,14,0,225,
        226,6,13,0,0,226,28,1,0,0,0,227,228,5,34,0,0,228,30,1,0,0,0,229,
        230,5,39,0,0,230,231,5,34,0,0,231,32,1,0,0,0,232,233,5,92,0,0,233,
        234,5,92,0,0,234,235,1,0,0,0,235,236,7,7,0,0,236,34,1,0,0,0,237,
        238,5,92,0,0,238,239,5,92,0,0,239,240,8,7,0,0,240,36,1,0,0,0,241,
        247,3,29,14,0,242,246,8,8,0,0,243,246,3,31,15,0,244,246,3,33,16,
        0,245,242,1,0,0,0,245,243,1,0,0,0,245,244,1,0,0,0,246,249,1,0,0,
        0,247,245,1,0,0,0,247,248,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,
        0,250,252,7,9,0,0,251,250,1,0,0,0,252,253,1,0,0,0,253,254,6,18,1,
        0,254,38,1,0,0,0,255,260,3,29,14,0,256,259,8,1,0,0,257,259,3,31,
        15,0,258,256,1,0,0,0,258,257,1,0,0,0,259,262,1,0,0,0,260,258,1,0,
        0,0,260,261,1,0,0,0,261,266,1,0,0,0,262,260,1,0,0,0,263,265,3,33,
        16,0,264,263,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,1,0,
        0,0,267,269,1,0,0,0,268,266,1,0,0,0,269,270,3,35,17,0,270,271,1,
        0,0,0,271,272,6,19,2,0,272,40,1,0,0,0,273,277,7,10,0,0,274,276,7,
        11,0,0,275,274,1,0,0,0,276,279,1,0,0,0,277,275,1,0,0,0,277,278,1,
        0,0,0,278,42,1,0,0,0,279,277,1,0,0,0,280,282,7,12,0,0,281,280,1,
        0,0,0,282,283,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,285,1,
        0,0,0,285,286,6,21,3,0,286,44,1,0,0,0,287,288,9,0,0,0,288,289,6,
        22,4,0,289,46,1,0,0,0,24,0,53,125,153,160,175,181,184,187,192,196,
        202,207,213,215,221,245,247,251,258,260,266,277,283,5,1,13,0,1,18,
        1,1,19,2,6,0,0,1,22,3
    ]

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
        self.checkVersion("4.13.1")
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
            	print("this is a string: "+self.text)

     

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
     


