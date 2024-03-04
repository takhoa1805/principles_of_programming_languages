# Generated from c://Users//takho//Desktop//principles_of_programming_languages//assignment_2//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,485,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,115,8,1,1,2,1,2,3,2,119,8,2,
        1,3,1,3,3,3,123,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,142,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,175,8,5,1,6,1,6,1,6,1,6,3,6,
        181,8,6,1,7,1,7,1,7,1,7,1,7,3,7,188,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,197,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,205,8,9,1,10,1,10,1,
        10,1,10,1,10,3,10,212,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,230,8,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,257,8,
        11,10,11,12,11,260,9,11,1,12,1,12,3,12,264,8,12,1,13,1,13,3,13,268,
        8,13,1,14,1,14,1,14,1,14,1,14,3,14,275,8,14,1,15,1,15,1,15,1,15,
        1,15,1,16,1,16,3,16,284,8,16,1,17,1,17,1,17,1,17,1,17,3,17,291,8,
        17,1,18,1,18,1,19,1,19,1,19,1,19,3,19,299,8,19,1,20,1,20,1,20,1,
        20,3,20,305,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,327,8,
        21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,
        28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,3,
        30,354,8,30,1,31,1,31,1,31,1,31,1,31,3,31,361,8,31,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,3,32,372,8,32,1,33,1,33,1,33,3,33,
        377,8,33,1,34,1,34,1,34,3,34,382,8,34,1,35,1,35,1,35,1,35,1,35,1,
        35,1,36,1,36,1,36,1,36,1,36,1,36,3,36,396,8,36,1,37,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,1,37,3,37,407,8,37,1,38,1,38,1,38,3,38,412,
        8,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,
        1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,
        1,44,1,44,1,45,1,45,1,45,3,45,444,8,45,1,46,1,46,1,46,1,46,3,46,
        450,8,46,1,47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,3,48,461,8,
        48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,3,
        50,475,8,50,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,0,1,22,
        53,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,92,94,96,98,100,102,104,0,6,2,0,1,2,20,20,1,0,43,46,1,0,26,
        28,1,0,24,25,1,0,22,23,1,0,30,36,495,0,106,1,0,0,0,2,114,1,0,0,0,
        4,118,1,0,0,0,6,122,1,0,0,0,8,141,1,0,0,0,10,174,1,0,0,0,12,180,
        1,0,0,0,14,187,1,0,0,0,16,196,1,0,0,0,18,204,1,0,0,0,20,211,1,0,
        0,0,22,229,1,0,0,0,24,263,1,0,0,0,26,267,1,0,0,0,28,274,1,0,0,0,
        30,276,1,0,0,0,32,283,1,0,0,0,34,290,1,0,0,0,36,292,1,0,0,0,38,298,
        1,0,0,0,40,304,1,0,0,0,42,326,1,0,0,0,44,328,1,0,0,0,46,330,1,0,
        0,0,48,332,1,0,0,0,50,334,1,0,0,0,52,336,1,0,0,0,54,338,1,0,0,0,
        56,340,1,0,0,0,58,342,1,0,0,0,60,353,1,0,0,0,62,360,1,0,0,0,64,371,
        1,0,0,0,66,376,1,0,0,0,68,381,1,0,0,0,70,383,1,0,0,0,72,395,1,0,
        0,0,74,406,1,0,0,0,76,411,1,0,0,0,78,413,1,0,0,0,80,417,1,0,0,0,
        82,421,1,0,0,0,84,427,1,0,0,0,86,429,1,0,0,0,88,431,1,0,0,0,90,443,
        1,0,0,0,92,449,1,0,0,0,94,451,1,0,0,0,96,460,1,0,0,0,98,462,1,0,
        0,0,100,474,1,0,0,0,102,476,1,0,0,0,104,480,1,0,0,0,106,107,3,66,
        33,0,107,108,3,2,1,0,108,109,5,0,0,1,109,1,1,0,0,0,110,111,3,4,2,
        0,111,112,3,2,1,0,112,115,1,0,0,0,113,115,3,4,2,0,114,110,1,0,0,
        0,114,113,1,0,0,0,115,3,1,0,0,0,116,119,3,6,3,0,117,119,3,58,29,
        0,118,116,1,0,0,0,118,117,1,0,0,0,119,5,1,0,0,0,120,123,3,8,4,0,
        121,123,3,10,5,0,122,120,1,0,0,0,122,121,1,0,0,0,123,7,1,0,0,0,124,
        125,3,44,22,0,125,126,5,45,0,0,126,127,5,29,0,0,127,128,3,66,33,
        0,128,142,1,0,0,0,129,130,5,3,0,0,130,131,5,45,0,0,131,132,5,29,
        0,0,132,142,3,66,33,0,133,134,3,44,22,0,134,135,5,45,0,0,135,136,
        5,40,0,0,136,137,3,12,6,0,137,138,5,41,0,0,138,139,5,29,0,0,139,
        140,3,66,33,0,140,142,1,0,0,0,141,124,1,0,0,0,141,129,1,0,0,0,141,
        133,1,0,0,0,142,9,1,0,0,0,143,144,5,4,0,0,144,145,5,45,0,0,145,146,
        5,37,0,0,146,147,3,22,11,0,147,148,5,29,0,0,148,149,3,66,33,0,149,
        175,1,0,0,0,150,151,3,44,22,0,151,152,5,45,0,0,152,153,5,37,0,0,
        153,154,3,22,11,0,154,155,5,29,0,0,155,156,3,66,33,0,156,175,1,0,
        0,0,157,158,5,3,0,0,158,159,5,45,0,0,159,160,5,37,0,0,160,161,3,
        22,11,0,161,162,5,29,0,0,162,163,3,66,33,0,163,175,1,0,0,0,164,165,
        3,44,22,0,165,166,5,45,0,0,166,167,5,40,0,0,167,168,3,12,6,0,168,
        169,5,41,0,0,169,170,5,37,0,0,170,171,3,22,11,0,171,172,5,29,0,0,
        172,173,3,66,33,0,173,175,1,0,0,0,174,143,1,0,0,0,174,150,1,0,0,
        0,174,157,1,0,0,0,174,164,1,0,0,0,175,11,1,0,0,0,176,177,5,44,0,
        0,177,178,5,42,0,0,178,181,3,12,6,0,179,181,5,44,0,0,180,176,1,0,
        0,0,180,179,1,0,0,0,181,13,1,0,0,0,182,183,5,40,0,0,183,184,3,12,
        6,0,184,185,5,41,0,0,185,188,1,0,0,0,186,188,3,12,6,0,187,182,1,
        0,0,0,187,186,1,0,0,0,188,15,1,0,0,0,189,190,5,40,0,0,190,191,3,
        14,7,0,191,192,5,42,0,0,192,193,3,16,8,0,193,194,5,41,0,0,194,197,
        1,0,0,0,195,197,3,14,7,0,196,189,1,0,0,0,196,195,1,0,0,0,197,17,
        1,0,0,0,198,199,5,40,0,0,199,200,3,20,10,0,200,201,5,41,0,0,201,
        205,1,0,0,0,202,203,5,40,0,0,203,205,5,41,0,0,204,198,1,0,0,0,204,
        202,1,0,0,0,205,19,1,0,0,0,206,207,3,22,11,0,207,208,5,42,0,0,208,
        209,3,20,10,0,209,212,1,0,0,0,210,212,3,22,11,0,211,206,1,0,0,0,
        211,210,1,0,0,0,212,21,1,0,0,0,213,214,6,11,-1,0,214,215,5,38,0,
        0,215,216,3,22,11,0,216,217,5,39,0,0,217,230,1,0,0,0,218,219,5,25,
        0,0,219,230,3,22,11,10,220,221,5,21,0,0,221,230,3,22,11,9,222,223,
        5,45,0,0,223,224,5,38,0,0,224,225,3,32,16,0,225,226,5,39,0,0,226,
        230,1,0,0,0,227,230,3,46,23,0,228,230,3,18,9,0,229,213,1,0,0,0,229,
        218,1,0,0,0,229,220,1,0,0,0,229,222,1,0,0,0,229,227,1,0,0,0,229,
        228,1,0,0,0,230,258,1,0,0,0,231,232,10,8,0,0,232,233,3,48,24,0,233,
        234,3,22,11,9,234,257,1,0,0,0,235,236,10,7,0,0,236,237,3,50,25,0,
        237,238,3,22,11,8,238,257,1,0,0,0,239,240,10,6,0,0,240,241,3,52,
        26,0,241,242,3,22,11,7,242,257,1,0,0,0,243,244,10,5,0,0,244,245,
        3,54,27,0,245,246,3,22,11,6,246,257,1,0,0,0,247,248,10,4,0,0,248,
        249,3,56,28,0,249,250,3,22,11,5,250,257,1,0,0,0,251,252,10,12,0,
        0,252,253,5,40,0,0,253,254,3,28,14,0,254,255,5,41,0,0,255,257,1,
        0,0,0,256,231,1,0,0,0,256,235,1,0,0,0,256,239,1,0,0,0,256,243,1,
        0,0,0,256,247,1,0,0,0,256,251,1,0,0,0,257,260,1,0,0,0,258,256,1,
        0,0,0,258,259,1,0,0,0,259,23,1,0,0,0,260,258,1,0,0,0,261,264,3,46,
        23,0,262,264,5,25,0,0,263,261,1,0,0,0,263,262,1,0,0,0,264,25,1,0,
        0,0,265,268,3,46,23,0,266,268,5,21,0,0,267,265,1,0,0,0,267,266,1,
        0,0,0,268,27,1,0,0,0,269,275,3,22,11,0,270,271,3,22,11,0,271,272,
        5,42,0,0,272,273,3,28,14,0,273,275,1,0,0,0,274,269,1,0,0,0,274,270,
        1,0,0,0,275,29,1,0,0,0,276,277,5,45,0,0,277,278,5,38,0,0,278,279,
        3,32,16,0,279,280,5,39,0,0,280,31,1,0,0,0,281,284,3,34,17,0,282,
        284,1,0,0,0,283,281,1,0,0,0,283,282,1,0,0,0,284,33,1,0,0,0,285,286,
        3,36,18,0,286,287,5,42,0,0,287,288,3,34,17,0,288,291,1,0,0,0,289,
        291,3,36,18,0,290,285,1,0,0,0,290,289,1,0,0,0,291,35,1,0,0,0,292,
        293,3,22,11,0,293,37,1,0,0,0,294,299,3,48,24,0,295,299,3,50,25,0,
        296,299,3,52,26,0,297,299,3,56,28,0,298,294,1,0,0,0,298,295,1,0,
        0,0,298,296,1,0,0,0,298,297,1,0,0,0,299,39,1,0,0,0,300,305,3,48,
        24,0,301,305,3,50,25,0,302,305,3,52,26,0,303,305,3,54,27,0,304,300,
        1,0,0,0,304,301,1,0,0,0,304,302,1,0,0,0,304,303,1,0,0,0,305,41,1,
        0,0,0,306,327,3,30,15,0,307,327,3,46,23,0,308,309,3,30,15,0,309,
        310,5,40,0,0,310,311,3,28,14,0,311,312,5,41,0,0,312,327,1,0,0,0,
        313,314,3,46,23,0,314,315,5,40,0,0,315,316,3,28,14,0,316,317,5,41,
        0,0,317,327,1,0,0,0,318,319,5,25,0,0,319,327,3,30,15,0,320,321,5,
        25,0,0,321,327,3,46,23,0,322,323,5,21,0,0,323,327,3,30,15,0,324,
        325,5,21,0,0,325,327,3,46,23,0,326,306,1,0,0,0,326,307,1,0,0,0,326,
        308,1,0,0,0,326,313,1,0,0,0,326,318,1,0,0,0,326,320,1,0,0,0,326,
        322,1,0,0,0,326,324,1,0,0,0,327,43,1,0,0,0,328,329,7,0,0,0,329,45,
        1,0,0,0,330,331,7,1,0,0,331,47,1,0,0,0,332,333,7,2,0,0,333,49,1,
        0,0,0,334,335,7,3,0,0,335,51,1,0,0,0,336,337,7,4,0,0,337,53,1,0,
        0,0,338,339,7,5,0,0,339,55,1,0,0,0,340,341,5,19,0,0,341,57,1,0,0,
        0,342,343,5,8,0,0,343,344,5,45,0,0,344,345,5,38,0,0,345,346,3,60,
        30,0,346,347,5,39,0,0,347,348,3,66,33,0,348,349,3,68,34,0,349,350,
        3,66,33,0,350,59,1,0,0,0,351,354,3,62,31,0,352,354,1,0,0,0,353,351,
        1,0,0,0,353,352,1,0,0,0,354,61,1,0,0,0,355,356,3,64,32,0,356,357,
        5,42,0,0,357,358,3,62,31,0,358,361,1,0,0,0,359,361,3,64,32,0,360,
        355,1,0,0,0,360,359,1,0,0,0,361,63,1,0,0,0,362,363,3,44,22,0,363,
        364,5,45,0,0,364,372,1,0,0,0,365,366,3,44,22,0,366,367,5,45,0,0,
        367,368,5,40,0,0,368,369,3,12,6,0,369,370,5,41,0,0,370,372,1,0,0,
        0,371,362,1,0,0,0,371,365,1,0,0,0,372,65,1,0,0,0,373,374,5,29,0,
        0,374,377,3,66,33,0,375,377,1,0,0,0,376,373,1,0,0,0,376,375,1,0,
        0,0,377,67,1,0,0,0,378,382,3,70,35,0,379,382,3,76,38,0,380,382,1,
        0,0,0,381,378,1,0,0,0,381,379,1,0,0,0,381,380,1,0,0,0,382,69,1,0,
        0,0,383,384,5,9,0,0,384,385,3,72,36,0,385,386,5,10,0,0,386,387,5,
        29,0,0,387,388,3,66,33,0,388,71,1,0,0,0,389,390,3,66,33,0,390,391,
        3,74,37,0,391,392,3,66,33,0,392,393,3,72,36,0,393,396,1,0,0,0,394,
        396,3,66,33,0,395,389,1,0,0,0,395,394,1,0,0,0,396,73,1,0,0,0,397,
        407,3,6,3,0,398,407,3,82,41,0,399,407,3,88,44,0,400,407,3,98,49,
        0,401,407,3,102,51,0,402,407,3,104,52,0,403,407,3,78,39,0,404,407,
        3,80,40,0,405,407,3,70,35,0,406,397,1,0,0,0,406,398,1,0,0,0,406,
        399,1,0,0,0,406,400,1,0,0,0,406,401,1,0,0,0,406,402,1,0,0,0,406,
        403,1,0,0,0,406,404,1,0,0,0,406,405,1,0,0,0,407,75,1,0,0,0,408,409,
        5,11,0,0,409,412,3,22,11,0,410,412,5,11,0,0,411,408,1,0,0,0,411,
        410,1,0,0,0,412,77,1,0,0,0,413,414,3,76,38,0,414,415,5,29,0,0,415,
        416,3,66,33,0,416,79,1,0,0,0,417,418,3,30,15,0,418,419,5,29,0,0,
        419,420,3,66,33,0,420,81,1,0,0,0,421,422,3,84,42,0,422,423,5,37,
        0,0,423,424,3,86,43,0,424,425,5,29,0,0,425,426,3,66,33,0,426,83,
        1,0,0,0,427,428,3,22,11,0,428,85,1,0,0,0,429,430,3,22,11,0,430,87,
        1,0,0,0,431,432,5,12,0,0,432,433,5,38,0,0,433,434,3,22,11,0,434,
        435,5,39,0,0,435,436,3,90,45,0,436,437,3,92,46,0,437,438,3,96,48,
        0,438,439,3,66,33,0,439,89,1,0,0,0,440,444,3,74,37,0,441,444,3,70,
        35,0,442,444,5,29,0,0,443,440,1,0,0,0,443,441,1,0,0,0,443,442,1,
        0,0,0,444,91,1,0,0,0,445,446,3,94,47,0,446,447,3,92,46,0,447,450,
        1,0,0,0,448,450,1,0,0,0,449,445,1,0,0,0,449,448,1,0,0,0,450,93,1,
        0,0,0,451,452,5,13,0,0,452,453,5,38,0,0,453,454,3,22,11,0,454,455,
        5,39,0,0,455,456,3,90,45,0,456,95,1,0,0,0,457,458,5,14,0,0,458,461,
        3,90,45,0,459,461,1,0,0,0,460,457,1,0,0,0,460,459,1,0,0,0,461,97,
        1,0,0,0,462,463,5,15,0,0,463,464,5,45,0,0,464,465,5,16,0,0,465,466,
        3,22,11,0,466,467,5,17,0,0,467,468,3,22,11,0,468,469,3,66,33,0,469,
        470,3,100,50,0,470,99,1,0,0,0,471,475,3,74,37,0,472,475,3,70,35,
        0,473,475,5,29,0,0,474,471,1,0,0,0,474,472,1,0,0,0,474,473,1,0,0,
        0,475,101,1,0,0,0,476,477,5,6,0,0,477,478,5,29,0,0,478,479,3,66,
        33,0,479,103,1,0,0,0,480,481,5,7,0,0,481,482,5,29,0,0,482,483,3,
        66,33,0,483,105,1,0,0,0,33,114,118,122,141,174,180,187,196,204,211,
        229,256,258,263,267,274,283,290,298,304,326,353,360,371,376,381,
        395,406,411,443,449,460,474
    ]

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
        self.checkVersion("4.13.1")
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecllist" ):
                listener.enterDecllist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecllist" ):
                listener.exitDecllist(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.vardecl()
                pass
            elif token in [8]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl_only" ):
                listener.enterVardecl_only(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl_only" ):
                listener.exitVardecl_only(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl_init" ):
                listener.enterVardecl_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl_init" ):
                listener.exitVardecl_init(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrlist" ):
                listener.enterArrlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrlist" ):
                listener.exitArrlist(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_expression" ):
                listener.enterArray_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_expression" ):
                listener.exitArray_expression(self)




    def array_expression(self):

        localctx = ZCodeParser.Array_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_expression)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 183
                self.arrlist()
                self.state = 184
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass
            elif token in [44]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrlist_expression" ):
                listener.enterArrlist_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrlist_expression" ):
                listener.exitArrlist_expression(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_literal" ):
                listener.enterArray_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_literal" ):
                listener.exitArray_literal(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_literal_prime" ):
                listener.enterArray_literal_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_literal_prime" ):
                listener.exitArray_literal_prime(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign_operands" ):
                listener.enterSign_operands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign_operands" ):
                listener.exitSign_operands(self)




    def sign_operands(self):

        localctx = ZCodeParser.Sign_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_sign_operands)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.literal()
                pass
            elif token in [25]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_operands" ):
                listener.enterNot_operands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_operands" ):
                listener.exitNot_operands(self)




    def not_operands(self):

        localctx = ZCodeParser.Not_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_not_operands)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.literal()
                pass
            elif token in [21]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_operators" ):
                listener.enterIndex_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_operators" ):
                listener.exitIndex_operators(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param_list)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 25, 38, 40, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.param_prime()
                pass
            elif token in [39]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_prime" ):
                listener.enterParam_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_prime" ):
                listener.exitParam_prime(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_rel_operators" ):
                listener.enterNon_rel_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_rel_operators" ):
                listener.exitNon_rel_operators(self)




    def non_rel_operators(self):

        localctx = ZCodeParser.Non_rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_non_rel_operators)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.mul_operators()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.add_operators()
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.logic_operators()
                pass
            elif token in [19]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_str_operators" ):
                listener.enterNon_str_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_str_operators" ):
                listener.exitNon_str_operators(self)




    def non_str_operators(self):

        localctx = ZCodeParser.Non_str_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_non_str_operators)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.mul_operators()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.add_operators()
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.logic_operators()
                pass
            elif token in [30, 31, 32, 33, 34, 35, 36]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_associative_operands" ):
                listener.enterNon_associative_operands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_associative_operands" ):
                listener.exitNon_associative_operands(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048582) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 131941395333120) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_operators" ):
                listener.enterMul_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_operators" ):
                listener.exitMul_operators(self)




    def mul_operators(self):

        localctx = ZCodeParser.Mul_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mul_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_operators" ):
                listener.enterAdd_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_operators" ):
                listener.exitAdd_operators(self)




    def add_operators(self):

        localctx = ZCodeParser.Add_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_add_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_operators" ):
                listener.enterLogic_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_operators" ):
                listener.exitLogic_operators(self)




    def logic_operators(self):

        localctx = ZCodeParser.Logic_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_operators" ):
                listener.enterRel_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_operators" ):
                listener.exitRel_operators(self)




    def rel_operators(self):

        localctx = ZCodeParser.Rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_rel_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 136365211648) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_operators" ):
                listener.enterStr_operators(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_operators" ):
                listener.exitStr_operators(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdecl" ):
                listener.enterFuncdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdecl" ):
                listener.exitFuncdecl(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_decl_list" ):
                listener.enterParam_decl_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_decl_list" ):
                listener.exitParam_decl_list(self)




    def param_decl_list(self):

        localctx = ZCodeParser.Param_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param_decl_list)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.param_decl_prime()
                pass
            elif token in [39]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_decl_prime" ):
                listener.enterParam_decl_prime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_decl_prime" ):
                listener.exitParam_decl_prime(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_single_decl" ):
                listener.enterParam_single_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_single_decl" ):
                listener.exitParam_single_decl(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline_list" ):
                listener.enterNewline_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline_list" ):
                listener.exitNewline_list(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_body)
        try:
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.statement_block()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.ret()
                pass
            elif token in [-1, 1, 2, 3, 4, 8, 20, 29]:
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_block" ):
                listener.enterStatement_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_block" ):
                listener.exitStatement_block(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call_statement" ):
                listener.enterFunc_call_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call_statement" ):
                listener.exitFunc_call_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhs" ):
                listener.enterRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhs" ):
                listener.exitRhs(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_body" ):
                listener.enterIf_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_body" ):
                listener.exitIf_body(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_statement_list" ):
                listener.enterElif_statement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_statement_list" ):
                listener.exitElif_statement_list(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_statement" ):
                listener.enterElif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_statement" ):
                listener.exitElif_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_body" ):
                listener.enterFor_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_body" ):
                listener.exitFor_body(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)




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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_statement" ):
                listener.enterContinue_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_statement" ):
                listener.exitContinue_statement(self)




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
         




