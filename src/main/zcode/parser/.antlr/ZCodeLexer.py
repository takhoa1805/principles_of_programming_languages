# Generated from c://Users//takho//Desktop//principles_of_programming_languages//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
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
        4,0,38,362,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,106,8,2,10,2,
        12,2,109,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,
        13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,3,15,208,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,19,1,
        19,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,
        24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,252,8,30,1,31,4,31,255,
        8,31,11,31,12,31,256,1,31,1,31,5,31,261,8,31,10,31,12,31,264,9,31,
        3,31,266,8,31,1,31,3,31,269,8,31,1,31,4,31,272,8,31,11,31,12,31,
        273,1,31,1,31,3,31,278,8,31,1,32,1,32,1,33,1,33,3,33,284,8,33,1,
        33,4,33,287,8,33,11,33,12,33,288,1,34,1,34,5,34,293,8,34,10,34,12,
        34,296,9,34,1,35,1,35,1,35,1,35,5,35,302,8,35,10,35,12,35,305,9,
        35,1,35,1,35,1,35,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,
        39,1,39,1,39,1,40,1,40,1,40,1,40,5,40,326,8,40,10,40,12,40,329,9,
        40,1,40,3,40,332,8,40,1,40,1,40,1,41,1,41,1,41,1,41,5,41,340,8,41,
        10,41,12,41,343,9,41,1,41,1,41,1,41,1,41,3,41,349,8,41,1,41,1,41,
        1,42,4,42,354,8,42,11,42,12,42,355,1,42,1,42,1,43,1,43,1,43,0,0,
        44,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,0,67,0,69,
        33,71,34,73,0,75,0,77,0,79,0,81,35,83,36,85,37,87,38,1,0,15,2,0,
        10,10,13,13,1,0,10,10,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,45,
        3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,5,0,10,10,13,
        13,34,34,39,39,92,92,7,0,39,39,92,92,98,98,102,102,110,110,114,114,
        116,116,3,0,34,34,39,39,92,92,2,1,10,10,13,13,3,0,10,10,13,13,34,
        34,1,0,39,39,1,0,34,34,3,0,8,9,12,13,32,32,388,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,
        0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,
        0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,
        0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,
        0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,
        0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,
        0,0,0,87,1,0,0,0,1,89,1,0,0,0,3,97,1,0,0,0,5,101,1,0,0,0,7,112,1,
        0,0,0,9,119,1,0,0,0,11,123,1,0,0,0,13,128,1,0,0,0,15,132,1,0,0,0,
        17,136,1,0,0,0,19,139,1,0,0,0,21,146,1,0,0,0,23,148,1,0,0,0,25,150,
        1,0,0,0,27,152,1,0,0,0,29,154,1,0,0,0,31,207,1,0,0,0,33,209,1,0,
        0,0,35,211,1,0,0,0,37,213,1,0,0,0,39,216,1,0,0,0,41,218,1,0,0,0,
        43,220,1,0,0,0,45,223,1,0,0,0,47,226,1,0,0,0,49,229,1,0,0,0,51,232,
        1,0,0,0,53,234,1,0,0,0,55,236,1,0,0,0,57,238,1,0,0,0,59,240,1,0,
        0,0,61,251,1,0,0,0,63,277,1,0,0,0,65,279,1,0,0,0,67,281,1,0,0,0,
        69,290,1,0,0,0,71,297,1,0,0,0,73,309,1,0,0,0,75,311,1,0,0,0,77,314,
        1,0,0,0,79,317,1,0,0,0,81,321,1,0,0,0,83,335,1,0,0,0,85,353,1,0,
        0,0,87,359,1,0,0,0,89,90,5,100,0,0,90,91,5,121,0,0,91,92,5,110,0,
        0,92,93,5,97,0,0,93,94,5,109,0,0,94,95,5,105,0,0,95,96,5,99,0,0,
        96,2,1,0,0,0,97,98,5,118,0,0,98,99,5,97,0,0,99,100,5,114,0,0,100,
        4,1,0,0,0,101,102,5,35,0,0,102,103,5,35,0,0,103,107,1,0,0,0,104,
        106,8,0,0,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,
        108,1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,6,2,0,0,111,
        6,1,0,0,0,112,113,5,115,0,0,113,114,5,116,0,0,114,115,5,114,0,0,
        115,116,5,105,0,0,116,117,5,110,0,0,117,118,5,103,0,0,118,8,1,0,
        0,0,119,120,5,46,0,0,120,121,5,46,0,0,121,122,5,46,0,0,122,10,1,
        0,0,0,123,124,5,98,0,0,124,125,5,111,0,0,125,126,5,111,0,0,126,127,
        5,108,0,0,127,12,1,0,0,0,128,129,5,110,0,0,129,130,5,111,0,0,130,
        131,5,116,0,0,131,14,1,0,0,0,132,133,5,97,0,0,133,134,5,110,0,0,
        134,135,5,100,0,0,135,16,1,0,0,0,136,137,5,111,0,0,137,138,5,114,
        0,0,138,18,1,0,0,0,139,140,5,110,0,0,140,141,5,117,0,0,141,142,5,
        109,0,0,142,143,5,98,0,0,143,144,5,101,0,0,144,145,5,114,0,0,145,
        20,1,0,0,0,146,147,5,43,0,0,147,22,1,0,0,0,148,149,5,45,0,0,149,
        24,1,0,0,0,150,151,5,42,0,0,151,26,1,0,0,0,152,153,5,47,0,0,153,
        28,1,0,0,0,154,155,5,37,0,0,155,30,1,0,0,0,156,157,5,114,0,0,157,
        158,5,101,0,0,158,159,5,116,0,0,159,160,5,117,0,0,160,161,5,114,
        0,0,161,208,5,110,0,0,162,163,5,102,0,0,163,164,5,117,0,0,164,165,
        5,110,0,0,165,208,5,99,0,0,166,167,5,102,0,0,167,168,5,111,0,0,168,
        208,5,114,0,0,169,170,5,117,0,0,170,171,5,110,0,0,171,172,5,116,
        0,0,172,173,5,105,0,0,173,208,5,108,0,0,174,175,5,98,0,0,175,208,
        5,121,0,0,176,177,5,98,0,0,177,178,5,114,0,0,178,179,5,101,0,0,179,
        180,5,97,0,0,180,208,5,107,0,0,181,182,5,99,0,0,182,183,5,111,0,
        0,183,184,5,110,0,0,184,185,5,116,0,0,185,186,5,105,0,0,186,187,
        5,110,0,0,187,188,5,117,0,0,188,208,5,101,0,0,189,190,5,105,0,0,
        190,208,5,102,0,0,191,192,5,101,0,0,192,193,5,108,0,0,193,194,5,
        115,0,0,194,208,5,101,0,0,195,196,5,101,0,0,196,197,5,108,0,0,197,
        198,5,105,0,0,198,208,5,102,0,0,199,200,5,98,0,0,200,201,5,101,0,
        0,201,202,5,103,0,0,202,203,5,105,0,0,203,208,5,110,0,0,204,205,
        5,101,0,0,205,206,5,110,0,0,206,208,5,100,0,0,207,156,1,0,0,0,207,
        162,1,0,0,0,207,166,1,0,0,0,207,169,1,0,0,0,207,174,1,0,0,0,207,
        176,1,0,0,0,207,181,1,0,0,0,207,189,1,0,0,0,207,191,1,0,0,0,207,
        195,1,0,0,0,207,199,1,0,0,0,207,204,1,0,0,0,208,32,1,0,0,0,209,210,
        7,1,0,0,210,34,1,0,0,0,211,212,5,61,0,0,212,36,1,0,0,0,213,214,5,
        33,0,0,214,215,5,61,0,0,215,38,1,0,0,0,216,217,5,60,0,0,217,40,1,
        0,0,0,218,219,5,62,0,0,219,42,1,0,0,0,220,221,5,60,0,0,221,222,5,
        61,0,0,222,44,1,0,0,0,223,224,5,62,0,0,224,225,5,61,0,0,225,46,1,
        0,0,0,226,227,5,61,0,0,227,228,5,61,0,0,228,48,1,0,0,0,229,230,5,
        60,0,0,230,231,5,45,0,0,231,50,1,0,0,0,232,233,5,40,0,0,233,52,1,
        0,0,0,234,235,5,41,0,0,235,54,1,0,0,0,236,237,5,91,0,0,237,56,1,
        0,0,0,238,239,5,93,0,0,239,58,1,0,0,0,240,241,5,44,0,0,241,60,1,
        0,0,0,242,243,5,116,0,0,243,244,5,114,0,0,244,245,5,117,0,0,245,
        252,5,101,0,0,246,247,5,102,0,0,247,248,5,97,0,0,248,249,5,108,0,
        0,249,250,5,115,0,0,250,252,5,101,0,0,251,242,1,0,0,0,251,246,1,
        0,0,0,252,62,1,0,0,0,253,255,3,65,32,0,254,253,1,0,0,0,255,256,1,
        0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,265,1,0,0,0,258,262,5,
        46,0,0,259,261,3,65,32,0,260,259,1,0,0,0,261,264,1,0,0,0,262,260,
        1,0,0,0,262,263,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,265,258,
        1,0,0,0,265,266,1,0,0,0,266,268,1,0,0,0,267,269,3,67,33,0,268,267,
        1,0,0,0,268,269,1,0,0,0,269,278,1,0,0,0,270,272,3,65,32,0,271,270,
        1,0,0,0,272,273,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,275,
        1,0,0,0,275,276,3,67,33,0,276,278,1,0,0,0,277,254,1,0,0,0,277,271,
        1,0,0,0,278,64,1,0,0,0,279,280,7,2,0,0,280,66,1,0,0,0,281,283,7,
        3,0,0,282,284,7,4,0,0,283,282,1,0,0,0,283,284,1,0,0,0,284,286,1,
        0,0,0,285,287,3,65,32,0,286,285,1,0,0,0,287,288,1,0,0,0,288,286,
        1,0,0,0,288,289,1,0,0,0,289,68,1,0,0,0,290,294,7,5,0,0,291,293,7,
        6,0,0,292,291,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,295,1,
        0,0,0,295,70,1,0,0,0,296,294,1,0,0,0,297,303,3,73,36,0,298,302,8,
        7,0,0,299,302,3,77,38,0,300,302,3,75,37,0,301,298,1,0,0,0,301,299,
        1,0,0,0,301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,
        1,0,0,0,304,306,1,0,0,0,305,303,1,0,0,0,306,307,3,73,36,0,307,308,
        6,35,1,0,308,72,1,0,0,0,309,310,5,34,0,0,310,74,1,0,0,0,311,312,
        5,39,0,0,312,313,5,34,0,0,313,76,1,0,0,0,314,315,5,92,0,0,315,316,
        7,8,0,0,316,78,1,0,0,0,317,318,5,92,0,0,318,319,5,92,0,0,319,320,
        8,8,0,0,320,80,1,0,0,0,321,327,3,73,36,0,322,326,8,9,0,0,323,326,
        3,75,37,0,324,326,3,77,38,0,325,322,1,0,0,0,325,323,1,0,0,0,325,
        324,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,
        331,1,0,0,0,329,327,1,0,0,0,330,332,7,10,0,0,331,330,1,0,0,0,332,
        333,1,0,0,0,333,334,6,40,2,0,334,82,1,0,0,0,335,341,3,73,36,0,336,
        340,8,11,0,0,337,340,3,75,37,0,338,340,3,77,38,0,339,336,1,0,0,0,
        339,337,1,0,0,0,339,338,1,0,0,0,340,343,1,0,0,0,341,339,1,0,0,0,
        341,342,1,0,0,0,342,348,1,0,0,0,343,341,1,0,0,0,344,345,5,92,0,0,
        345,349,8,8,0,0,346,347,7,12,0,0,347,349,8,13,0,0,348,344,1,0,0,
        0,348,346,1,0,0,0,349,350,1,0,0,0,350,351,6,41,3,0,351,84,1,0,0,
        0,352,354,7,14,0,0,353,352,1,0,0,0,354,355,1,0,0,0,355,353,1,0,0,
        0,355,356,1,0,0,0,356,357,1,0,0,0,357,358,6,42,0,0,358,86,1,0,0,
        0,359,360,9,0,0,0,360,361,6,43,4,0,361,88,1,0,0,0,22,0,107,207,251,
        256,262,265,268,273,277,283,288,294,301,303,325,327,331,339,341,
        348,355,5,6,0,0,1,35,0,1,40,1,1,41,2,1,43,3
    ]

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
        self.checkVersion("4.13.1")
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
     


