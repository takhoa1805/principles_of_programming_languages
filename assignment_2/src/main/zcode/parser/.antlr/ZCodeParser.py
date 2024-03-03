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
        4,1,50,458,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,107,
        8,1,1,2,1,2,3,2,111,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,161,8,3,1,4,1,4,1,4,1,4,3,4,167,8,4,
        1,5,1,5,1,5,1,5,1,5,3,5,174,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        183,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,201,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,228,
        8,7,10,7,12,7,231,9,7,1,8,1,8,3,8,235,8,8,1,9,1,9,3,9,239,8,9,1,
        10,1,10,1,10,1,10,1,10,3,10,246,8,10,1,11,1,11,1,11,1,11,1,11,1,
        12,1,12,3,12,255,8,12,1,13,1,13,1,13,1,13,1,13,3,13,262,8,13,1,14,
        1,14,1,15,1,15,1,15,1,15,3,15,270,8,15,1,16,1,16,1,16,1,16,3,16,
        276,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,298,8,17,1,18,
        1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,3,26,325,
        8,26,1,27,1,27,1,27,1,27,1,27,3,27,332,8,27,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,3,28,343,8,28,1,29,1,29,1,29,3,29,348,8,
        29,1,30,1,30,1,30,3,30,353,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,
        32,1,32,1,32,1,32,1,32,1,32,3,32,367,8,32,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,3,33,378,8,33,1,34,1,34,1,34,3,34,383,8,34,
        1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,
        1,37,1,38,1,38,3,38,401,8,38,1,39,1,39,1,40,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,1,40,1,41,1,41,1,41,3,41,417,8,41,1,42,1,42,1,42,
        1,42,3,42,423,8,42,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,
        3,44,434,8,44,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,46,
        1,46,1,46,3,46,448,8,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,
        1,48,0,1,14,49,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,0,6,2,0,1,2,20,20,1,0,43,46,1,0,26,28,
        1,0,24,25,1,0,22,23,1,0,30,36,471,0,98,1,0,0,0,2,106,1,0,0,0,4,110,
        1,0,0,0,6,160,1,0,0,0,8,166,1,0,0,0,10,173,1,0,0,0,12,182,1,0,0,
        0,14,200,1,0,0,0,16,234,1,0,0,0,18,238,1,0,0,0,20,245,1,0,0,0,22,
        247,1,0,0,0,24,254,1,0,0,0,26,261,1,0,0,0,28,263,1,0,0,0,30,269,
        1,0,0,0,32,275,1,0,0,0,34,297,1,0,0,0,36,299,1,0,0,0,38,301,1,0,
        0,0,40,303,1,0,0,0,42,305,1,0,0,0,44,307,1,0,0,0,46,309,1,0,0,0,
        48,311,1,0,0,0,50,313,1,0,0,0,52,324,1,0,0,0,54,331,1,0,0,0,56,342,
        1,0,0,0,58,347,1,0,0,0,60,352,1,0,0,0,62,354,1,0,0,0,64,366,1,0,
        0,0,66,377,1,0,0,0,68,382,1,0,0,0,70,384,1,0,0,0,72,388,1,0,0,0,
        74,392,1,0,0,0,76,400,1,0,0,0,78,402,1,0,0,0,80,404,1,0,0,0,82,416,
        1,0,0,0,84,422,1,0,0,0,86,424,1,0,0,0,88,433,1,0,0,0,90,435,1,0,
        0,0,92,447,1,0,0,0,94,449,1,0,0,0,96,453,1,0,0,0,98,99,3,58,29,0,
        99,100,3,2,1,0,100,101,5,0,0,1,101,1,1,0,0,0,102,103,3,4,2,0,103,
        104,3,2,1,0,104,107,1,0,0,0,105,107,3,4,2,0,106,102,1,0,0,0,106,
        105,1,0,0,0,107,3,1,0,0,0,108,111,3,6,3,0,109,111,3,50,25,0,110,
        108,1,0,0,0,110,109,1,0,0,0,111,5,1,0,0,0,112,113,3,36,18,0,113,
        114,5,45,0,0,114,115,5,29,0,0,115,116,3,58,29,0,116,161,1,0,0,0,
        117,118,5,3,0,0,118,119,5,45,0,0,119,120,5,29,0,0,120,161,3,58,29,
        0,121,122,5,4,0,0,122,123,5,45,0,0,123,124,5,37,0,0,124,125,3,14,
        7,0,125,126,5,29,0,0,126,127,3,58,29,0,127,161,1,0,0,0,128,129,3,
        36,18,0,129,130,5,45,0,0,130,131,5,37,0,0,131,132,3,14,7,0,132,133,
        5,29,0,0,133,134,3,58,29,0,134,161,1,0,0,0,135,136,5,3,0,0,136,137,
        5,45,0,0,137,138,5,37,0,0,138,139,3,14,7,0,139,140,5,29,0,0,140,
        141,3,58,29,0,141,161,1,0,0,0,142,143,3,36,18,0,143,144,5,45,0,0,
        144,145,5,40,0,0,145,146,3,8,4,0,146,147,5,41,0,0,147,148,5,29,0,
        0,148,149,3,58,29,0,149,161,1,0,0,0,150,151,3,36,18,0,151,152,5,
        45,0,0,152,153,5,40,0,0,153,154,3,8,4,0,154,155,5,41,0,0,155,156,
        5,37,0,0,156,157,3,14,7,0,157,158,5,29,0,0,158,159,3,58,29,0,159,
        161,1,0,0,0,160,112,1,0,0,0,160,117,1,0,0,0,160,121,1,0,0,0,160,
        128,1,0,0,0,160,135,1,0,0,0,160,142,1,0,0,0,160,150,1,0,0,0,161,
        7,1,0,0,0,162,163,5,44,0,0,163,164,5,42,0,0,164,167,3,8,4,0,165,
        167,5,44,0,0,166,162,1,0,0,0,166,165,1,0,0,0,167,9,1,0,0,0,168,169,
        5,40,0,0,169,170,3,8,4,0,170,171,5,41,0,0,171,174,1,0,0,0,172,174,
        3,8,4,0,173,168,1,0,0,0,173,172,1,0,0,0,174,11,1,0,0,0,175,176,5,
        40,0,0,176,177,3,10,5,0,177,178,5,42,0,0,178,179,3,12,6,0,179,180,
        5,41,0,0,180,183,1,0,0,0,181,183,3,10,5,0,182,175,1,0,0,0,182,181,
        1,0,0,0,183,13,1,0,0,0,184,185,6,7,-1,0,185,186,5,38,0,0,186,187,
        3,14,7,0,187,188,5,39,0,0,188,201,1,0,0,0,189,190,5,25,0,0,190,201,
        3,14,7,10,191,192,5,21,0,0,192,201,3,14,7,9,193,201,3,10,5,0,194,
        195,5,45,0,0,195,196,5,38,0,0,196,197,3,24,12,0,197,198,5,39,0,0,
        198,201,1,0,0,0,199,201,3,38,19,0,200,184,1,0,0,0,200,189,1,0,0,
        0,200,191,1,0,0,0,200,193,1,0,0,0,200,194,1,0,0,0,200,199,1,0,0,
        0,201,229,1,0,0,0,202,203,10,8,0,0,203,204,3,40,20,0,204,205,3,14,
        7,9,205,228,1,0,0,0,206,207,10,7,0,0,207,208,3,42,21,0,208,209,3,
        14,7,8,209,228,1,0,0,0,210,211,10,6,0,0,211,212,3,44,22,0,212,213,
        3,14,7,7,213,228,1,0,0,0,214,215,10,5,0,0,215,216,3,46,23,0,216,
        217,3,14,7,6,217,228,1,0,0,0,218,219,10,4,0,0,219,220,3,48,24,0,
        220,221,3,14,7,5,221,228,1,0,0,0,222,223,10,12,0,0,223,224,5,40,
        0,0,224,225,3,20,10,0,225,226,5,41,0,0,226,228,1,0,0,0,227,202,1,
        0,0,0,227,206,1,0,0,0,227,210,1,0,0,0,227,214,1,0,0,0,227,218,1,
        0,0,0,227,222,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,
        0,0,0,230,15,1,0,0,0,231,229,1,0,0,0,232,235,3,38,19,0,233,235,5,
        25,0,0,234,232,1,0,0,0,234,233,1,0,0,0,235,17,1,0,0,0,236,239,3,
        38,19,0,237,239,5,21,0,0,238,236,1,0,0,0,238,237,1,0,0,0,239,19,
        1,0,0,0,240,246,3,14,7,0,241,242,3,14,7,0,242,243,5,42,0,0,243,244,
        3,20,10,0,244,246,1,0,0,0,245,240,1,0,0,0,245,241,1,0,0,0,246,21,
        1,0,0,0,247,248,5,45,0,0,248,249,5,38,0,0,249,250,3,24,12,0,250,
        251,5,39,0,0,251,23,1,0,0,0,252,255,3,26,13,0,253,255,1,0,0,0,254,
        252,1,0,0,0,254,253,1,0,0,0,255,25,1,0,0,0,256,257,3,28,14,0,257,
        258,5,42,0,0,258,259,3,26,13,0,259,262,1,0,0,0,260,262,3,28,14,0,
        261,256,1,0,0,0,261,260,1,0,0,0,262,27,1,0,0,0,263,264,3,14,7,0,
        264,29,1,0,0,0,265,270,3,40,20,0,266,270,3,42,21,0,267,270,3,44,
        22,0,268,270,3,48,24,0,269,265,1,0,0,0,269,266,1,0,0,0,269,267,1,
        0,0,0,269,268,1,0,0,0,270,31,1,0,0,0,271,276,3,40,20,0,272,276,3,
        42,21,0,273,276,3,44,22,0,274,276,3,46,23,0,275,271,1,0,0,0,275,
        272,1,0,0,0,275,273,1,0,0,0,275,274,1,0,0,0,276,33,1,0,0,0,277,298,
        3,22,11,0,278,298,3,38,19,0,279,280,3,22,11,0,280,281,5,40,0,0,281,
        282,3,20,10,0,282,283,5,41,0,0,283,298,1,0,0,0,284,285,3,38,19,0,
        285,286,5,40,0,0,286,287,3,20,10,0,287,288,5,41,0,0,288,298,1,0,
        0,0,289,290,5,25,0,0,290,298,3,22,11,0,291,292,5,25,0,0,292,298,
        3,38,19,0,293,294,5,21,0,0,294,298,3,22,11,0,295,296,5,21,0,0,296,
        298,3,38,19,0,297,277,1,0,0,0,297,278,1,0,0,0,297,279,1,0,0,0,297,
        284,1,0,0,0,297,289,1,0,0,0,297,291,1,0,0,0,297,293,1,0,0,0,297,
        295,1,0,0,0,298,35,1,0,0,0,299,300,7,0,0,0,300,37,1,0,0,0,301,302,
        7,1,0,0,302,39,1,0,0,0,303,304,7,2,0,0,304,41,1,0,0,0,305,306,7,
        3,0,0,306,43,1,0,0,0,307,308,7,4,0,0,308,45,1,0,0,0,309,310,7,5,
        0,0,310,47,1,0,0,0,311,312,5,19,0,0,312,49,1,0,0,0,313,314,5,8,0,
        0,314,315,5,45,0,0,315,316,5,38,0,0,316,317,3,52,26,0,317,318,5,
        39,0,0,318,319,3,58,29,0,319,320,3,60,30,0,320,321,3,58,29,0,321,
        51,1,0,0,0,322,325,3,54,27,0,323,325,1,0,0,0,324,322,1,0,0,0,324,
        323,1,0,0,0,325,53,1,0,0,0,326,327,3,56,28,0,327,328,5,42,0,0,328,
        329,3,54,27,0,329,332,1,0,0,0,330,332,3,56,28,0,331,326,1,0,0,0,
        331,330,1,0,0,0,332,55,1,0,0,0,333,334,3,36,18,0,334,335,5,45,0,
        0,335,343,1,0,0,0,336,337,3,36,18,0,337,338,5,45,0,0,338,339,5,40,
        0,0,339,340,3,8,4,0,340,341,5,41,0,0,341,343,1,0,0,0,342,333,1,0,
        0,0,342,336,1,0,0,0,343,57,1,0,0,0,344,345,5,29,0,0,345,348,3,58,
        29,0,346,348,1,0,0,0,347,344,1,0,0,0,347,346,1,0,0,0,348,59,1,0,
        0,0,349,353,3,62,31,0,350,353,3,68,34,0,351,353,1,0,0,0,352,349,
        1,0,0,0,352,350,1,0,0,0,352,351,1,0,0,0,353,61,1,0,0,0,354,355,5,
        9,0,0,355,356,3,64,32,0,356,357,5,10,0,0,357,358,5,29,0,0,358,359,
        3,58,29,0,359,63,1,0,0,0,360,361,3,58,29,0,361,362,3,66,33,0,362,
        363,3,58,29,0,363,364,3,64,32,0,364,367,1,0,0,0,365,367,3,58,29,
        0,366,360,1,0,0,0,366,365,1,0,0,0,367,65,1,0,0,0,368,378,3,6,3,0,
        369,378,3,74,37,0,370,378,3,80,40,0,371,378,3,90,45,0,372,378,3,
        94,47,0,373,378,3,96,48,0,374,378,3,70,35,0,375,378,3,72,36,0,376,
        378,3,62,31,0,377,368,1,0,0,0,377,369,1,0,0,0,377,370,1,0,0,0,377,
        371,1,0,0,0,377,372,1,0,0,0,377,373,1,0,0,0,377,374,1,0,0,0,377,
        375,1,0,0,0,377,376,1,0,0,0,378,67,1,0,0,0,379,380,5,11,0,0,380,
        383,3,14,7,0,381,383,5,11,0,0,382,379,1,0,0,0,382,381,1,0,0,0,383,
        69,1,0,0,0,384,385,3,68,34,0,385,386,5,29,0,0,386,387,3,58,29,0,
        387,71,1,0,0,0,388,389,3,22,11,0,389,390,5,29,0,0,390,391,3,58,29,
        0,391,73,1,0,0,0,392,393,3,76,38,0,393,394,5,37,0,0,394,395,3,78,
        39,0,395,396,5,29,0,0,396,397,3,58,29,0,397,75,1,0,0,0,398,401,5,
        45,0,0,399,401,1,0,0,0,400,398,1,0,0,0,400,399,1,0,0,0,401,77,1,
        0,0,0,402,403,3,14,7,0,403,79,1,0,0,0,404,405,5,12,0,0,405,406,5,
        38,0,0,406,407,3,14,7,0,407,408,5,39,0,0,408,409,3,82,41,0,409,410,
        3,84,42,0,410,411,3,88,44,0,411,412,3,58,29,0,412,81,1,0,0,0,413,
        417,3,66,33,0,414,417,3,62,31,0,415,417,5,29,0,0,416,413,1,0,0,0,
        416,414,1,0,0,0,416,415,1,0,0,0,417,83,1,0,0,0,418,419,3,86,43,0,
        419,420,3,84,42,0,420,423,1,0,0,0,421,423,1,0,0,0,422,418,1,0,0,
        0,422,421,1,0,0,0,423,85,1,0,0,0,424,425,5,13,0,0,425,426,5,38,0,
        0,426,427,3,14,7,0,427,428,5,39,0,0,428,429,3,82,41,0,429,87,1,0,
        0,0,430,431,5,14,0,0,431,434,3,82,41,0,432,434,1,0,0,0,433,430,1,
        0,0,0,433,432,1,0,0,0,434,89,1,0,0,0,435,436,5,15,0,0,436,437,5,
        45,0,0,437,438,5,16,0,0,438,439,3,14,7,0,439,440,5,17,0,0,440,441,
        3,14,7,0,441,442,3,58,29,0,442,443,3,92,46,0,443,91,1,0,0,0,444,
        448,3,66,33,0,445,448,3,62,31,0,446,448,5,29,0,0,447,444,1,0,0,0,
        447,445,1,0,0,0,447,446,1,0,0,0,448,93,1,0,0,0,449,450,5,6,0,0,450,
        451,5,29,0,0,451,452,3,58,29,0,452,95,1,0,0,0,453,454,5,7,0,0,454,
        455,5,29,0,0,455,456,3,58,29,0,456,97,1,0,0,0,30,106,110,160,166,
        173,182,200,227,229,234,238,245,254,261,269,275,297,324,331,342,
        347,352,366,377,382,400,416,422,433,447
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
    RULE_arrlist = 4
    RULE_array_expression = 5
    RULE_arrlist_expression = 6
    RULE_expression = 7
    RULE_sign_operands = 8
    RULE_not_operands = 9
    RULE_index_operators = 10
    RULE_func_call = 11
    RULE_param_list = 12
    RULE_param_prime = 13
    RULE_param = 14
    RULE_non_rel_operators = 15
    RULE_non_str_operators = 16
    RULE_non_associative_operands = 17
    RULE_typ = 18
    RULE_literal = 19
    RULE_mul_operators = 20
    RULE_add_operators = 21
    RULE_logic_operators = 22
    RULE_rel_operators = 23
    RULE_str_operators = 24
    RULE_funcdecl = 25
    RULE_param_decl_list = 26
    RULE_param_decl_prime = 27
    RULE_param_single_decl = 28
    RULE_newline_list = 29
    RULE_body = 30
    RULE_statement_block = 31
    RULE_statement_list = 32
    RULE_statement = 33
    RULE_ret = 34
    RULE_return_statement = 35
    RULE_func_call_statement = 36
    RULE_assignment_statement = 37
    RULE_lhs = 38
    RULE_rhs = 39
    RULE_if_statement = 40
    RULE_if_body = 41
    RULE_elif_statement_list = 42
    RULE_elif_statement = 43
    RULE_else_statement = 44
    RULE_for_statement = 45
    RULE_for_body = 46
    RULE_break_statement = 47
    RULE_continue_statement = 48

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "arrlist", 
                   "array_expression", "arrlist_expression", "expression", 
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




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.newline_list()
            self.state = 99
            self.decllist()
            self.state = 100
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




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.decl()
                self.state = 103
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
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




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.vardecl()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
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

        def VAR_TYPE(self):
            return self.getToken(ZCodeParser.VAR_TYPE, 0)

        def ASSIGN_OPERATOR(self):
            return self.getToken(ZCodeParser.ASSIGN_OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def arrlist(self):
            return self.getTypedRuleContext(ZCodeParser.ArrlistContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.typ()
                self.state = 113
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 114
                self.match(ZCodeParser.NEWLINE)
                self.state = 115
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 118
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 119
                self.match(ZCodeParser.NEWLINE)
                self.state = 120
                self.newline_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(ZCodeParser.VAR_TYPE)
                self.state = 122
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 123
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 124
                self.expression(0)
                self.state = 125
                self.match(ZCodeParser.NEWLINE)
                self.state = 126
                self.newline_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.typ()
                self.state = 129
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 130
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 131
                self.expression(0)
                self.state = 132
                self.match(ZCodeParser.NEWLINE)
                self.state = 133
                self.newline_list()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 136
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 137
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 138
                self.expression(0)
                self.state = 139
                self.match(ZCodeParser.NEWLINE)
                self.state = 140
                self.newline_list()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 142
                self.typ()
                self.state = 143
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 144
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 145
                self.arrlist()
                self.state = 146
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 147
                self.match(ZCodeParser.NEWLINE)
                self.state = 148
                self.newline_list()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 150
                self.typ()
                self.state = 151
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 152
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 153
                self.arrlist()
                self.state = 154
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 155
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 156
                self.expression(0)
                self.state = 157
                self.match(ZCodeParser.NEWLINE)
                self.state = 158
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




    def arrlist(self):

        localctx = ZCodeParser.ArrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrlist)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(ZCodeParser.NUMBER)
                self.state = 163
                self.match(ZCodeParser.COMMA)
                self.state = 164
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
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




    def array_expression(self):

        localctx = ZCodeParser.Array_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_expression)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 169
                self.arrlist()
                self.state = 170
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
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




    def arrlist_expression(self):

        localctx = ZCodeParser.Arrlist_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrlist_expression)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 176
                self.array_expression()
                self.state = 177
                self.match(ZCodeParser.COMMA)
                self.state = 178
                self.arrlist_expression()
                self.state = 179
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.array_expression()
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

        def array_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Array_expressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 185
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 186
                self.expression(0)
                self.state = 187
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 2:
                self.state = 189
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 190
                self.expression(10)
                pass

            elif la_ == 3:
                self.state = 191
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 192
                self.expression(9)
                pass

            elif la_ == 4:
                self.state = 193
                self.array_expression()
                pass

            elif la_ == 5:
                self.state = 194
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 195
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 196
                self.param_list()
                self.state = 197
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 6:
                self.state = 199
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 227
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 202
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 203
                        self.mul_operators()
                        self.state = 204
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 206
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 207
                        self.add_operators()
                        self.state = 208
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 210
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 211
                        self.logic_operators()
                        self.state = 212
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 214
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 215
                        self.rel_operators()
                        self.state = 216
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 218
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 219
                        self.str_operators()
                        self.state = 220
                        self.expression(5)
                        pass

                    elif la_ == 6:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 222
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 223
                        self.match(ZCodeParser.OPEN_BRACKET)
                        self.state = 224
                        self.index_operators()
                        self.state = 225
                        self.match(ZCodeParser.CLOSE_BRACKET)
                        pass

             
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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




    def sign_operands(self):

        localctx = ZCodeParser.Sign_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sign_operands)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.literal()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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




    def not_operands(self):

        localctx = ZCodeParser.Not_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_not_operands)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.literal()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_index_operators)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.expression(0)
                self.state = 242
                self.match(ZCodeParser.COMMA)
                self.state = 243
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




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 248
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 249
            self.param_list()
            self.state = 250
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




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 25, 38, 40, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
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




    def param_prime(self):

        localctx = ZCodeParser.Param_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param_prime)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.param()
                self.state = 257
                self.match(ZCodeParser.COMMA)
                self.state = 258
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
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




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
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




    def non_rel_operators(self):

        localctx = ZCodeParser.Non_rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_non_rel_operators)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.mul_operators()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.add_operators()
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.logic_operators()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
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




    def non_str_operators(self):

        localctx = ZCodeParser.Non_str_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_non_str_operators)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.mul_operators()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.add_operators()
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.logic_operators()
                pass
            elif token in [30, 31, 32, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
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




    def non_associative_operands(self):

        localctx = ZCodeParser.Non_associative_operandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_non_associative_operands)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.func_call()
                self.state = 280
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 281
                self.index_operators()
                self.state = 282
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.literal()
                self.state = 285
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 286
                self.index_operators()
                self.state = 287
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 289
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 290
                self.func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 291
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 292
                self.literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 293
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 294
                self.func_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 295
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 296
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




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
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




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
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




    def mul_operators(self):

        localctx = ZCodeParser.Mul_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mul_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
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




    def add_operators(self):

        localctx = ZCodeParser.Add_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_add_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
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




    def logic_operators(self):

        localctx = ZCodeParser.Logic_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
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




    def rel_operators(self):

        localctx = ZCodeParser.Rel_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_rel_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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




    def str_operators(self):

        localctx = ZCodeParser.Str_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_str_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(ZCodeParser.FUNC)
            self.state = 314
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 315
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 316
            self.param_decl_list()
            self.state = 317
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
            self.state = 318
            self.newline_list()
            self.state = 319
            self.body()
            self.state = 320
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




    def param_decl_list(self):

        localctx = ZCodeParser.Param_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_param_decl_list)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
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




    def param_decl_prime(self):

        localctx = ZCodeParser.Param_decl_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_param_decl_prime)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.param_single_decl()
                self.state = 327
                self.match(ZCodeParser.COMMA)
                self.state = 328
                self.param_decl_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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




    def param_single_decl(self):

        localctx = ZCodeParser.Param_single_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_param_single_decl)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.typ()
                self.state = 334
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.typ()
                self.state = 337
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 338
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 339
                self.arrlist()
                self.state = 340
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




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_newline_list)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(ZCodeParser.NEWLINE)
                self.state = 345
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




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_body)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.statement_block()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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




    def statement_block(self):

        localctx = ZCodeParser.Statement_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statement_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(ZCodeParser.BEGIN)
            self.state = 355
            self.statement_list()
            self.state = 356
            self.match(ZCodeParser.END)
            self.state = 357
            self.match(ZCodeParser.NEWLINE)
            self.state = 358
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




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement_list)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.newline_list()
                self.state = 361
                self.statement()
                self.state = 362
                self.newline_list()
                self.state = 363
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
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




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_statement)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 371
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 372
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 373
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 374
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 375
                self.func_call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 376
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




    def ret(self):

        localctx = ZCodeParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ret)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(ZCodeParser.RETURN)
                self.state = 380
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.ret()
            self.state = 385
            self.match(ZCodeParser.NEWLINE)
            self.state = 386
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




    def func_call_statement(self):

        localctx = ZCodeParser.Func_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_func_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.func_call()
            self.state = 389
            self.match(ZCodeParser.NEWLINE)
            self.state = 390
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




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.lhs()
            self.state = 393
            self.match(ZCodeParser.ASSIGN_OPERATOR)
            self.state = 394
            self.rhs()
            self.state = 395
            self.match(ZCodeParser.NEWLINE)
            self.state = 396
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_lhs)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [37]:
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


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_rhs




    def rhs(self):

        localctx = ZCodeParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(ZCodeParser.IF)
            self.state = 405
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 406
            self.expression(0)
            self.state = 407
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
            self.state = 408
            self.if_body()
            self.state = 409
            self.elif_statement_list()
            self.state = 410
            self.else_statement()
            self.state = 411
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




    def if_body(self):

        localctx = ZCodeParser.If_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_if_body)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.statement_block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
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




    def elif_statement_list(self):

        localctx = ZCodeParser.Elif_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elif_statement_list)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.elif_statement()
                self.state = 419
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




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(ZCodeParser.ELIF)
            self.state = 425
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 426
            self.expression(0)
            self.state = 427
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
            self.state = 428
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




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_else_statement)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(ZCodeParser.ELSE)
                self.state = 431
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




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(ZCodeParser.FOR)
            self.state = 436
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 437
            self.match(ZCodeParser.UNTIL)
            self.state = 438
            self.expression(0)
            self.state = 439
            self.match(ZCodeParser.BY)
            self.state = 440
            self.expression(0)
            self.state = 441
            self.newline_list()
            self.state = 442
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




    def for_body(self):

        localctx = ZCodeParser.For_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_for_body)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.statement_block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
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




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(ZCodeParser.BREAK_STATEMENT)
            self.state = 450
            self.match(ZCodeParser.NEWLINE)
            self.state = 451
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




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(ZCodeParser.CONTINUE_STATEMENT)
            self.state = 454
            self.match(ZCodeParser.NEWLINE)
            self.state = 455
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
        self._predicates[7] = self.expression_sempred
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
         




