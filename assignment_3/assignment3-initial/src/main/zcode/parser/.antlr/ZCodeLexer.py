# Generated from c://Users//takho//Desktop//Work//principles_of_programming_languages//assignment_3//assignment3-initial//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
2113773


def serializedATN():
    return [
        4,0,50,413,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,5,17,221,8,
        17,10,17,12,17,224,9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,
        1,28,3,28,261,8,28,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,32,1,32,
        1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,
        1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,3,42,303,8,42,1,43,4,43,306,8,43,11,43,
        12,43,307,1,43,1,43,5,43,312,8,43,10,43,12,43,315,9,43,3,43,317,
        8,43,1,43,3,43,320,8,43,1,43,4,43,323,8,43,11,43,12,43,324,1,43,
        1,43,3,43,329,8,43,1,44,1,44,1,45,1,45,3,45,335,8,45,1,45,4,45,338,
        8,45,11,45,12,45,339,1,46,1,46,5,46,344,8,46,10,46,12,46,347,9,46,
        1,47,1,47,1,47,1,47,5,47,353,8,47,10,47,12,47,356,9,47,1,47,1,47,
        1,47,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,50,1,51,1,51,1,51,1,51,
        1,52,1,52,1,52,1,52,5,52,377,8,52,10,52,12,52,380,9,52,1,52,3,52,
        383,8,52,1,52,1,52,1,53,1,53,1,53,1,53,5,53,391,8,53,10,53,12,53,
        394,9,53,1,53,1,53,1,53,1,53,3,53,400,8,53,1,53,1,53,1,54,4,54,405,
        8,54,11,54,12,54,406,1,54,1,54,1,55,1,55,1,55,0,0,56,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,
        53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,
        75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,0,91,0,93,45,95,46,
        97,0,99,0,101,0,103,0,105,47,107,48,109,49,111,50,1,0,14,2,0,10,
        10,13,13,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,45,3,0,65,90,95,
        95,97,122,4,0,48,57,65,90,95,95,97,122,5,0,10,10,13,13,34,34,39,
        39,92,92,7,0,39,39,92,92,98,98,102,102,110,110,114,114,116,116,3,
        0,34,34,39,39,92,92,2,1,10,10,13,13,3,0,10,10,13,13,34,34,1,0,39,
        39,1,0,34,34,3,0,8,9,12,13,32,32,429,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,
        0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,
        0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,
        0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,
        0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,
        0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,
        0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,
        0,0,0,0,87,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,1,113,1,0,0,0,3,120,1,0,0,0,
        5,127,1,0,0,0,7,135,1,0,0,0,9,139,1,0,0,0,11,153,1,0,0,0,13,159,
        1,0,0,0,15,168,1,0,0,0,17,173,1,0,0,0,19,179,1,0,0,0,21,183,1,0,
        0,0,23,190,1,0,0,0,25,193,1,0,0,0,27,198,1,0,0,0,29,203,1,0,0,0,
        31,207,1,0,0,0,33,213,1,0,0,0,35,216,1,0,0,0,37,227,1,0,0,0,39,231,
        1,0,0,0,41,236,1,0,0,0,43,240,1,0,0,0,45,244,1,0,0,0,47,247,1,0,
        0,0,49,249,1,0,0,0,51,251,1,0,0,0,53,253,1,0,0,0,55,255,1,0,0,0,
        57,260,1,0,0,0,59,262,1,0,0,0,61,264,1,0,0,0,63,267,1,0,0,0,65,269,
        1,0,0,0,67,271,1,0,0,0,69,274,1,0,0,0,71,277,1,0,0,0,73,280,1,0,
        0,0,75,283,1,0,0,0,77,285,1,0,0,0,79,287,1,0,0,0,81,289,1,0,0,0,
        83,291,1,0,0,0,85,302,1,0,0,0,87,328,1,0,0,0,89,330,1,0,0,0,91,332,
        1,0,0,0,93,341,1,0,0,0,95,348,1,0,0,0,97,360,1,0,0,0,99,362,1,0,
        0,0,101,365,1,0,0,0,103,368,1,0,0,0,105,372,1,0,0,0,107,386,1,0,
        0,0,109,404,1,0,0,0,111,410,1,0,0,0,113,114,5,115,0,0,114,115,5,
        116,0,0,115,116,5,114,0,0,116,117,5,105,0,0,117,118,5,110,0,0,118,
        119,5,103,0,0,119,2,1,0,0,0,120,121,5,110,0,0,121,122,5,117,0,0,
        122,123,5,109,0,0,123,124,5,98,0,0,124,125,5,101,0,0,125,126,5,114,
        0,0,126,4,1,0,0,0,127,128,5,100,0,0,128,129,5,121,0,0,129,130,5,
        110,0,0,130,131,5,97,0,0,131,132,5,109,0,0,132,133,5,105,0,0,133,
        134,5,99,0,0,134,6,1,0,0,0,135,136,5,118,0,0,136,137,5,97,0,0,137,
        138,5,114,0,0,138,8,1,0,0,0,139,140,5,102,0,0,140,141,5,111,0,0,
        141,142,5,114,0,0,142,143,5,32,0,0,143,144,5,115,0,0,144,145,5,116,
        0,0,145,146,5,97,0,0,146,147,5,116,0,0,147,148,5,101,0,0,148,149,
        5,109,0,0,149,150,5,101,0,0,150,151,5,110,0,0,151,152,5,116,0,0,
        152,10,1,0,0,0,153,154,5,98,0,0,154,155,5,114,0,0,155,156,5,101,
        0,0,156,157,5,97,0,0,157,158,5,107,0,0,158,12,1,0,0,0,159,160,5,
        99,0,0,160,161,5,111,0,0,161,162,5,110,0,0,162,163,5,116,0,0,163,
        164,5,105,0,0,164,165,5,110,0,0,165,166,5,117,0,0,166,167,5,101,
        0,0,167,14,1,0,0,0,168,169,5,102,0,0,169,170,5,117,0,0,170,171,5,
        110,0,0,171,172,5,99,0,0,172,16,1,0,0,0,173,174,5,98,0,0,174,175,
        5,101,0,0,175,176,5,103,0,0,176,177,5,105,0,0,177,178,5,110,0,0,
        178,18,1,0,0,0,179,180,5,101,0,0,180,181,5,110,0,0,181,182,5,100,
        0,0,182,20,1,0,0,0,183,184,5,114,0,0,184,185,5,101,0,0,185,186,5,
        116,0,0,186,187,5,117,0,0,187,188,5,114,0,0,188,189,5,110,0,0,189,
        22,1,0,0,0,190,191,5,105,0,0,191,192,5,102,0,0,192,24,1,0,0,0,193,
        194,5,101,0,0,194,195,5,108,0,0,195,196,5,105,0,0,196,197,5,102,
        0,0,197,26,1,0,0,0,198,199,5,101,0,0,199,200,5,108,0,0,200,201,5,
        115,0,0,201,202,5,101,0,0,202,28,1,0,0,0,203,204,5,102,0,0,204,205,
        5,111,0,0,205,206,5,114,0,0,206,30,1,0,0,0,207,208,5,117,0,0,208,
        209,5,110,0,0,209,210,5,116,0,0,210,211,5,105,0,0,211,212,5,108,
        0,0,212,32,1,0,0,0,213,214,5,98,0,0,214,215,5,121,0,0,215,34,1,0,
        0,0,216,217,5,35,0,0,217,218,5,35,0,0,218,222,1,0,0,0,219,221,8,
        0,0,0,220,219,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,
        0,0,0,223,225,1,0,0,0,224,222,1,0,0,0,225,226,6,17,0,0,226,36,1,
        0,0,0,227,228,5,46,0,0,228,229,5,46,0,0,229,230,5,46,0,0,230,38,
        1,0,0,0,231,232,5,98,0,0,232,233,5,111,0,0,233,234,5,111,0,0,234,
        235,5,108,0,0,235,40,1,0,0,0,236,237,5,110,0,0,237,238,5,111,0,0,
        238,239,5,116,0,0,239,42,1,0,0,0,240,241,5,97,0,0,241,242,5,110,
        0,0,242,243,5,100,0,0,243,44,1,0,0,0,244,245,5,111,0,0,245,246,5,
        114,0,0,246,46,1,0,0,0,247,248,5,43,0,0,248,48,1,0,0,0,249,250,5,
        45,0,0,250,50,1,0,0,0,251,252,5,42,0,0,252,52,1,0,0,0,253,254,5,
        47,0,0,254,54,1,0,0,0,255,256,5,37,0,0,256,56,1,0,0,0,257,261,5,
        10,0,0,258,259,5,13,0,0,259,261,5,10,0,0,260,257,1,0,0,0,260,258,
        1,0,0,0,261,58,1,0,0,0,262,263,5,61,0,0,263,60,1,0,0,0,264,265,5,
        33,0,0,265,266,5,61,0,0,266,62,1,0,0,0,267,268,5,60,0,0,268,64,1,
        0,0,0,269,270,5,62,0,0,270,66,1,0,0,0,271,272,5,60,0,0,272,273,5,
        61,0,0,273,68,1,0,0,0,274,275,5,62,0,0,275,276,5,61,0,0,276,70,1,
        0,0,0,277,278,5,61,0,0,278,279,5,61,0,0,279,72,1,0,0,0,280,281,5,
        60,0,0,281,282,5,45,0,0,282,74,1,0,0,0,283,284,5,40,0,0,284,76,1,
        0,0,0,285,286,5,41,0,0,286,78,1,0,0,0,287,288,5,91,0,0,288,80,1,
        0,0,0,289,290,5,93,0,0,290,82,1,0,0,0,291,292,5,44,0,0,292,84,1,
        0,0,0,293,294,5,116,0,0,294,295,5,114,0,0,295,296,5,117,0,0,296,
        303,5,101,0,0,297,298,5,102,0,0,298,299,5,97,0,0,299,300,5,108,0,
        0,300,301,5,115,0,0,301,303,5,101,0,0,302,293,1,0,0,0,302,297,1,
        0,0,0,303,86,1,0,0,0,304,306,3,89,44,0,305,304,1,0,0,0,306,307,1,
        0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,316,1,0,0,0,309,313,5,
        46,0,0,310,312,3,89,44,0,311,310,1,0,0,0,312,315,1,0,0,0,313,311,
        1,0,0,0,313,314,1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,316,309,
        1,0,0,0,316,317,1,0,0,0,317,319,1,0,0,0,318,320,3,91,45,0,319,318,
        1,0,0,0,319,320,1,0,0,0,320,329,1,0,0,0,321,323,3,89,44,0,322,321,
        1,0,0,0,323,324,1,0,0,0,324,322,1,0,0,0,324,325,1,0,0,0,325,326,
        1,0,0,0,326,327,3,91,45,0,327,329,1,0,0,0,328,305,1,0,0,0,328,322,
        1,0,0,0,329,88,1,0,0,0,330,331,7,1,0,0,331,90,1,0,0,0,332,334,7,
        2,0,0,333,335,7,3,0,0,334,333,1,0,0,0,334,335,1,0,0,0,335,337,1,
        0,0,0,336,338,3,89,44,0,337,336,1,0,0,0,338,339,1,0,0,0,339,337,
        1,0,0,0,339,340,1,0,0,0,340,92,1,0,0,0,341,345,7,4,0,0,342,344,7,
        5,0,0,343,342,1,0,0,0,344,347,1,0,0,0,345,343,1,0,0,0,345,346,1,
        0,0,0,346,94,1,0,0,0,347,345,1,0,0,0,348,354,3,97,48,0,349,353,8,
        6,0,0,350,353,3,101,50,0,351,353,3,99,49,0,352,349,1,0,0,0,352,350,
        1,0,0,0,352,351,1,0,0,0,353,356,1,0,0,0,354,352,1,0,0,0,354,355,
        1,0,0,0,355,357,1,0,0,0,356,354,1,0,0,0,357,358,3,97,48,0,358,359,
        6,47,1,0,359,96,1,0,0,0,360,361,5,34,0,0,361,98,1,0,0,0,362,363,
        5,39,0,0,363,364,5,34,0,0,364,100,1,0,0,0,365,366,5,92,0,0,366,367,
        7,7,0,0,367,102,1,0,0,0,368,369,5,92,0,0,369,370,5,92,0,0,370,371,
        8,7,0,0,371,104,1,0,0,0,372,378,3,97,48,0,373,377,8,8,0,0,374,377,
        3,99,49,0,375,377,3,101,50,0,376,373,1,0,0,0,376,374,1,0,0,0,376,
        375,1,0,0,0,377,380,1,0,0,0,378,376,1,0,0,0,378,379,1,0,0,0,379,
        382,1,0,0,0,380,378,1,0,0,0,381,383,7,9,0,0,382,381,1,0,0,0,383,
        384,1,0,0,0,384,385,6,52,2,0,385,106,1,0,0,0,386,392,3,97,48,0,387,
        391,8,10,0,0,388,391,3,99,49,0,389,391,3,101,50,0,390,387,1,0,0,
        0,390,388,1,0,0,0,390,389,1,0,0,0,391,394,1,0,0,0,392,390,1,0,0,
        0,392,393,1,0,0,0,393,399,1,0,0,0,394,392,1,0,0,0,395,396,5,92,0,
        0,396,400,8,7,0,0,397,398,7,11,0,0,398,400,8,12,0,0,399,395,1,0,
        0,0,399,397,1,0,0,0,400,401,1,0,0,0,401,402,6,53,3,0,402,108,1,0,
        0,0,403,405,7,13,0,0,404,403,1,0,0,0,405,406,1,0,0,0,406,404,1,0,
        0,0,406,407,1,0,0,0,407,408,1,0,0,0,408,409,6,54,0,0,409,110,1,0,
        0,0,410,411,9,0,0,0,411,412,6,55,4,0,412,112,1,0,0,0,22,0,222,260,
        302,307,313,316,319,324,328,334,339,345,352,354,376,378,382,390,
        392,399,406,5,6,0,0,1,47,0,1,52,1,1,53,2,1,55,3
    ]

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
        self.checkVersion("4.13.1")
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
     


