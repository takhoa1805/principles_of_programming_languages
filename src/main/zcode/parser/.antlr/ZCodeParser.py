# Generated from c://Users//takho//Desktop//principles_of_programming_languages//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
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
        4,1,46,392,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,94,
        8,1,1,2,1,2,3,2,98,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,149,8,3,1,4,1,4,1,4,1,4,3,4,155,8,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,168,8,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,195,8,5,10,5,12,5,198,9,5,1,6,
        1,6,3,6,202,8,6,1,7,1,7,3,7,206,8,7,1,8,1,8,1,8,1,8,1,8,3,8,213,
        8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,222,8,10,1,11,1,11,1,11,1,
        11,1,11,3,11,229,8,11,1,12,1,12,1,13,1,13,1,13,1,13,3,13,237,8,13,
        1,14,1,14,1,14,1,14,3,14,243,8,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,265,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,
        1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,24,1,24,1,24,1,24,1,25,1,25,3,25,295,8,25,1,26,1,26,1,26,1,26,
        1,26,3,26,302,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        3,27,313,8,27,1,28,1,28,1,28,3,28,318,8,28,1,29,1,29,1,29,3,29,323,
        8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,3,31,335,
        8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,345,8,32,1,33,
        1,33,1,33,3,33,350,8,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,
        1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,3,37,
        372,8,37,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,0,1,10,43,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,0,6,2,0,9,10,15,15,1,0,
        39,42,1,0,21,23,1,0,19,20,1,0,17,18,1,0,26,32,401,0,86,1,0,0,0,2,
        93,1,0,0,0,4,97,1,0,0,0,6,148,1,0,0,0,8,154,1,0,0,0,10,167,1,0,0,
        0,12,201,1,0,0,0,14,205,1,0,0,0,16,212,1,0,0,0,18,214,1,0,0,0,20,
        221,1,0,0,0,22,228,1,0,0,0,24,230,1,0,0,0,26,236,1,0,0,0,28,242,
        1,0,0,0,30,264,1,0,0,0,32,266,1,0,0,0,34,268,1,0,0,0,36,270,1,0,
        0,0,38,272,1,0,0,0,40,274,1,0,0,0,42,276,1,0,0,0,44,278,1,0,0,0,
        46,280,1,0,0,0,48,288,1,0,0,0,50,294,1,0,0,0,52,301,1,0,0,0,54,312,
        1,0,0,0,56,317,1,0,0,0,58,322,1,0,0,0,60,324,1,0,0,0,62,334,1,0,
        0,0,64,344,1,0,0,0,66,349,1,0,0,0,68,351,1,0,0,0,70,355,1,0,0,0,
        72,359,1,0,0,0,74,371,1,0,0,0,76,373,1,0,0,0,78,375,1,0,0,0,80,379,
        1,0,0,0,82,383,1,0,0,0,84,387,1,0,0,0,86,87,3,2,1,0,87,88,5,0,0,
        1,88,1,1,0,0,0,89,90,3,4,2,0,90,91,3,2,1,0,91,94,1,0,0,0,92,94,3,
        4,2,0,93,89,1,0,0,0,93,92,1,0,0,0,94,3,1,0,0,0,95,98,3,6,3,0,96,
        98,3,46,23,0,97,95,1,0,0,0,97,96,1,0,0,0,98,5,1,0,0,0,99,100,3,32,
        16,0,100,101,5,41,0,0,101,102,3,56,28,0,102,103,5,25,0,0,103,149,
        1,0,0,0,104,105,5,11,0,0,105,106,5,41,0,0,106,107,3,56,28,0,107,
        108,5,25,0,0,108,149,1,0,0,0,109,110,5,12,0,0,110,111,5,41,0,0,111,
        112,5,33,0,0,112,113,3,10,5,0,113,114,3,56,28,0,114,115,5,25,0,0,
        115,149,1,0,0,0,116,117,3,32,16,0,117,118,5,41,0,0,118,119,5,33,
        0,0,119,120,3,10,5,0,120,121,3,56,28,0,121,122,5,25,0,0,122,149,
        1,0,0,0,123,124,5,11,0,0,124,125,5,41,0,0,125,126,5,33,0,0,126,127,
        3,10,5,0,127,128,3,56,28,0,128,129,5,25,0,0,129,149,1,0,0,0,130,
        131,3,32,16,0,131,132,5,41,0,0,132,133,5,36,0,0,133,134,3,8,4,0,
        134,135,5,37,0,0,135,136,3,56,28,0,136,137,5,25,0,0,137,149,1,0,
        0,0,138,139,3,32,16,0,139,140,5,41,0,0,140,141,5,36,0,0,141,142,
        3,8,4,0,142,143,5,37,0,0,143,144,5,33,0,0,144,145,3,10,5,0,145,146,
        3,56,28,0,146,147,5,25,0,0,147,149,1,0,0,0,148,99,1,0,0,0,148,104,
        1,0,0,0,148,109,1,0,0,0,148,116,1,0,0,0,148,123,1,0,0,0,148,130,
        1,0,0,0,148,138,1,0,0,0,149,7,1,0,0,0,150,151,5,40,0,0,151,152,5,
        38,0,0,152,155,3,8,4,0,153,155,5,40,0,0,154,150,1,0,0,0,154,153,
        1,0,0,0,155,9,1,0,0,0,156,157,6,5,-1,0,157,158,5,34,0,0,158,159,
        3,10,5,0,159,160,5,35,0,0,160,168,1,0,0,0,161,162,5,20,0,0,162,168,
        3,10,5,9,163,164,5,16,0,0,164,168,3,10,5,8,165,168,3,18,9,0,166,
        168,3,34,17,0,167,156,1,0,0,0,167,161,1,0,0,0,167,163,1,0,0,0,167,
        165,1,0,0,0,167,166,1,0,0,0,168,196,1,0,0,0,169,170,10,7,0,0,170,
        171,3,36,18,0,171,172,3,10,5,8,172,195,1,0,0,0,173,174,10,6,0,0,
        174,175,3,38,19,0,175,176,3,10,5,7,176,195,1,0,0,0,177,178,10,5,
        0,0,178,179,3,40,20,0,179,180,3,10,5,6,180,195,1,0,0,0,181,182,10,
        4,0,0,182,183,3,42,21,0,183,184,3,10,5,5,184,195,1,0,0,0,185,186,
        10,3,0,0,186,187,3,44,22,0,187,188,3,10,5,4,188,195,1,0,0,0,189,
        190,10,11,0,0,190,191,5,36,0,0,191,192,3,16,8,0,192,193,5,37,0,0,
        193,195,1,0,0,0,194,169,1,0,0,0,194,173,1,0,0,0,194,177,1,0,0,0,
        194,181,1,0,0,0,194,185,1,0,0,0,194,189,1,0,0,0,195,198,1,0,0,0,
        196,194,1,0,0,0,196,197,1,0,0,0,197,11,1,0,0,0,198,196,1,0,0,0,199,
        202,3,34,17,0,200,202,5,20,0,0,201,199,1,0,0,0,201,200,1,0,0,0,202,
        13,1,0,0,0,203,206,3,34,17,0,204,206,5,16,0,0,205,203,1,0,0,0,205,
        204,1,0,0,0,206,15,1,0,0,0,207,213,3,10,5,0,208,209,3,10,5,0,209,
        210,5,38,0,0,210,211,3,16,8,0,211,213,1,0,0,0,212,207,1,0,0,0,212,
        208,1,0,0,0,213,17,1,0,0,0,214,215,5,41,0,0,215,216,5,34,0,0,216,
        217,3,20,10,0,217,218,5,35,0,0,218,19,1,0,0,0,219,222,3,22,11,0,
        220,222,1,0,0,0,221,219,1,0,0,0,221,220,1,0,0,0,222,21,1,0,0,0,223,
        224,3,24,12,0,224,225,5,38,0,0,225,226,3,22,11,0,226,229,1,0,0,0,
        227,229,3,24,12,0,228,223,1,0,0,0,228,227,1,0,0,0,229,23,1,0,0,0,
        230,231,3,10,5,0,231,25,1,0,0,0,232,237,3,36,18,0,233,237,3,38,19,
        0,234,237,3,40,20,0,235,237,3,44,22,0,236,232,1,0,0,0,236,233,1,
        0,0,0,236,234,1,0,0,0,236,235,1,0,0,0,237,27,1,0,0,0,238,243,3,36,
        18,0,239,243,3,38,19,0,240,243,3,40,20,0,241,243,3,42,21,0,242,238,
        1,0,0,0,242,239,1,0,0,0,242,240,1,0,0,0,242,241,1,0,0,0,243,29,1,
        0,0,0,244,265,3,18,9,0,245,265,3,34,17,0,246,247,3,18,9,0,247,248,
        5,36,0,0,248,249,3,16,8,0,249,250,5,37,0,0,250,265,1,0,0,0,251,252,
        3,34,17,0,252,253,5,36,0,0,253,254,3,16,8,0,254,255,5,37,0,0,255,
        265,1,0,0,0,256,257,5,20,0,0,257,265,3,18,9,0,258,259,5,20,0,0,259,
        265,3,34,17,0,260,261,5,16,0,0,261,265,3,18,9,0,262,263,5,16,0,0,
        263,265,3,34,17,0,264,244,1,0,0,0,264,245,1,0,0,0,264,246,1,0,0,
        0,264,251,1,0,0,0,264,256,1,0,0,0,264,258,1,0,0,0,264,260,1,0,0,
        0,264,262,1,0,0,0,265,31,1,0,0,0,266,267,7,0,0,0,267,33,1,0,0,0,
        268,269,7,1,0,0,269,35,1,0,0,0,270,271,7,2,0,0,271,37,1,0,0,0,272,
        273,7,3,0,0,273,39,1,0,0,0,274,275,7,4,0,0,275,41,1,0,0,0,276,277,
        7,5,0,0,277,43,1,0,0,0,278,279,5,14,0,0,279,45,1,0,0,0,280,281,5,
        1,0,0,281,282,5,41,0,0,282,283,3,48,24,0,283,284,3,56,28,0,284,285,
        3,58,29,0,285,286,3,56,28,0,286,287,5,25,0,0,287,47,1,0,0,0,288,
        289,5,34,0,0,289,290,3,50,25,0,290,291,5,35,0,0,291,49,1,0,0,0,292,
        295,3,52,26,0,293,295,1,0,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,
        51,1,0,0,0,296,297,3,54,27,0,297,298,5,38,0,0,298,299,3,52,26,0,
        299,302,1,0,0,0,300,302,3,54,27,0,301,296,1,0,0,0,301,300,1,0,0,
        0,302,53,1,0,0,0,303,304,3,32,16,0,304,305,5,41,0,0,305,313,1,0,
        0,0,306,307,3,32,16,0,307,308,5,41,0,0,308,309,5,36,0,0,309,310,
        3,8,4,0,310,311,5,37,0,0,311,313,1,0,0,0,312,303,1,0,0,0,312,306,
        1,0,0,0,313,55,1,0,0,0,314,315,5,25,0,0,315,318,3,56,28,0,316,318,
        1,0,0,0,317,314,1,0,0,0,317,316,1,0,0,0,318,57,1,0,0,0,319,323,3,
        60,30,0,320,323,3,66,33,0,321,323,1,0,0,0,322,319,1,0,0,0,322,320,
        1,0,0,0,322,321,1,0,0,0,323,59,1,0,0,0,324,325,5,2,0,0,325,326,3,
        62,31,0,326,327,5,3,0,0,327,328,3,56,28,0,328,329,5,25,0,0,329,61,
        1,0,0,0,330,331,3,64,32,0,331,332,3,62,31,0,332,335,1,0,0,0,333,
        335,1,0,0,0,334,330,1,0,0,0,334,333,1,0,0,0,335,63,1,0,0,0,336,345,
        3,6,3,0,337,345,3,72,36,0,338,345,3,78,39,0,339,345,3,80,40,0,340,
        345,3,82,41,0,341,345,3,84,42,0,342,345,3,68,34,0,343,345,3,70,35,
        0,344,336,1,0,0,0,344,337,1,0,0,0,344,338,1,0,0,0,344,339,1,0,0,
        0,344,340,1,0,0,0,344,341,1,0,0,0,344,342,1,0,0,0,344,343,1,0,0,
        0,345,65,1,0,0,0,346,347,5,4,0,0,347,350,3,10,5,0,348,350,5,4,0,
        0,349,346,1,0,0,0,349,348,1,0,0,0,350,67,1,0,0,0,351,352,3,66,33,
        0,352,353,3,56,28,0,353,354,5,25,0,0,354,69,1,0,0,0,355,356,3,18,
        9,0,356,357,3,56,28,0,357,358,5,25,0,0,358,71,1,0,0,0,359,360,3,
        74,37,0,360,361,5,33,0,0,361,362,3,76,38,0,362,363,3,56,28,0,363,
        364,5,25,0,0,364,73,1,0,0,0,365,372,5,41,0,0,366,367,3,10,5,0,367,
        368,5,36,0,0,368,369,3,16,8,0,369,370,5,37,0,0,370,372,1,0,0,0,371,
        365,1,0,0,0,371,366,1,0,0,0,372,75,1,0,0,0,373,374,3,10,5,0,374,
        77,1,0,0,0,375,376,5,5,0,0,376,377,3,56,28,0,377,378,5,25,0,0,378,
        79,1,0,0,0,379,380,5,6,0,0,380,381,3,56,28,0,381,382,5,25,0,0,382,
        81,1,0,0,0,383,384,5,7,0,0,384,385,3,56,28,0,385,386,5,25,0,0,386,
        83,1,0,0,0,387,388,5,8,0,0,388,389,3,56,28,0,389,390,5,25,0,0,390,
        85,1,0,0,0,24,93,97,148,154,167,194,196,201,205,212,221,228,236,
        242,264,294,301,312,317,322,334,344,349,371
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "'begin'", "'end'", "'return'", 
                     "'if statement'", "'for statement'", "'break statement'", 
                     "'continue statement'", "'string'", "'number'", "'dynamic'", 
                     "'var'", "<INVALID>", "'...'", "'bool'", "'not'", "'and'", 
                     "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "<INVALID>", 
                     "<INVALID>", "'='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'<-'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING_TYPE", "NUMBER_TYPE", "DYNAMIC_TYPE", 
                      "VAR_TYPE", "COMMENT", "STRING_OPERATOR", "BOOL_TYPE", 
                      "NOT_OPERATOR", "AND_OPERATOR", "OR_OPERATOR", "ADD_OPERATOR", 
                      "SUB_OPERATOR", "MUL_OPERATOR", "DIV_OPERATOR", "MOD_OPERATOR", 
                      "KEYWORD", "NEWLINE", "EQ_OPERATOR", "NEQ_OPERATOR", 
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
    RULE_expression = 5
    RULE_sign_operands = 6
    RULE_not_operands = 7
    RULE_index_operators = 8
    RULE_func_call = 9
    RULE_param_list = 10
    RULE_param_prime = 11
    RULE_param = 12
    RULE_non_rel_operators = 13
    RULE_non_str_operators = 14
    RULE_non_associative_operands = 15
    RULE_typ = 16
    RULE_literal = 17
    RULE_mul_operators = 18
    RULE_add_operators = 19
    RULE_logic_operators = 20
    RULE_rel_operators = 21
    RULE_str_operators = 22
    RULE_funcdecl = 23
    RULE_param_decl = 24
    RULE_param_decl_list = 25
    RULE_param_decl_prime = 26
    RULE_param_single_decl = 27
    RULE_newline_list = 28
    RULE_body = 29
    RULE_statement_block = 30
    RULE_statement_list = 31
    RULE_statement = 32
    RULE_ret = 33
    RULE_return_statement = 34
    RULE_func_call_statement = 35
    RULE_assignment_statement = 36
    RULE_lhs = 37
    RULE_rhs = 38
    RULE_if_statement = 39
    RULE_for_statement = 40
    RULE_break_statement = 41
    RULE_continue_statement = 42

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "arrlist", 
                   "expression", "sign_operands", "not_operands", "index_operators", 
                   "func_call", "param_list", "param_prime", "param", "non_rel_operators", 
                   "non_str_operators", "non_associative_operands", "typ", 
                   "literal", "mul_operators", "add_operators", "logic_operators", 
                   "rel_operators", "str_operators", "funcdecl", "param_decl", 
                   "param_decl_list", "param_decl_prime", "param_single_decl", 
                   "newline_list", "body", "statement_block", "statement_list", 
                   "statement", "ret", "return_statement", "func_call_statement", 
                   "assignment_statement", "lhs", "rhs", "if_statement", 
                   "for_statement", "break_statement", "continue_statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    STRING_TYPE=9
    NUMBER_TYPE=10
    DYNAMIC_TYPE=11
    VAR_TYPE=12
    COMMENT=13
    STRING_OPERATOR=14
    BOOL_TYPE=15
    NOT_OPERATOR=16
    AND_OPERATOR=17
    OR_OPERATOR=18
    ADD_OPERATOR=19
    SUB_OPERATOR=20
    MUL_OPERATOR=21
    DIV_OPERATOR=22
    MOD_OPERATOR=23
    KEYWORD=24
    NEWLINE=25
    EQ_OPERATOR=26
    NEQ_OPERATOR=27
    LT_OPERATOR=28
    GT_OPERATOR=29
    LEQ_OPERATOR=30
    GEQ_OPERATOR=31
    SEQ_OPERATOR=32
    ASSIGN_OPERATOR=33
    OPEN_PARENTHESIS=34
    CLOSE_PARENTHESIS=35
    OPEN_BRACKET=36
    CLOSE_BRACKET=37
    COMMA=38
    BOOLEAN=39
    NUMBER=40
    IDENTIFIER=41
    STRING=42
    UNCLOSE_STRING=43
    ILLEGAL_ESCAPE=44
    WS=45
    ERROR_CHAR=46

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
            self.state = 86
            self.decllist()
            self.state = 87
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
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.decl()
                self.state = 90
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.vardecl()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.typ()
                self.state = 100
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 101
                self.newline_list()
                self.state = 102
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 105
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 106
                self.newline_list()
                self.state = 107
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(ZCodeParser.VAR_TYPE)
                self.state = 110
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 111
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 112
                self.expression(0)
                self.state = 113
                self.newline_list()
                self.state = 114
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.typ()
                self.state = 117
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 118
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 119
                self.expression(0)
                self.state = 120
                self.newline_list()
                self.state = 121
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.match(ZCodeParser.DYNAMIC_TYPE)
                self.state = 124
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 125
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 126
                self.expression(0)
                self.state = 127
                self.newline_list()
                self.state = 128
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.typ()
                self.state = 131
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 132
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 133
                self.arrlist()
                self.state = 134
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 135
                self.newline_list()
                self.state = 136
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 138
                self.typ()
                self.state = 139
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 140
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 141
                self.arrlist()
                self.state = 142
                self.match(ZCodeParser.CLOSE_BRACKET)
                self.state = 143
                self.match(ZCodeParser.ASSIGN_OPERATOR)
                self.state = 144
                self.expression(0)
                self.state = 145
                self.newline_list()
                self.state = 146
                self.match(ZCodeParser.NEWLINE)
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
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(ZCodeParser.NUMBER)
                self.state = 151
                self.match(ZCodeParser.COMMA)
                self.state = 152
                self.arrlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(ZCodeParser.NUMBER)
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

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 157
                self.match(ZCodeParser.OPEN_PARENTHESIS)
                self.state = 158
                self.expression(0)
                self.state = 159
                self.match(ZCodeParser.CLOSE_PARENTHESIS)
                pass

            elif la_ == 2:
                self.state = 161
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 162
                self.expression(9)
                pass

            elif la_ == 3:
                self.state = 163
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 164
                self.expression(8)
                pass

            elif la_ == 4:
                self.state = 165
                self.func_call()
                pass

            elif la_ == 5:
                self.state = 166
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 170
                        self.mul_operators()
                        self.state = 171
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 173
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 174
                        self.add_operators()
                        self.state = 175
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 177
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 178
                        self.logic_operators()
                        self.state = 179
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 182
                        self.rel_operators()
                        self.state = 183
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 186
                        self.str_operators()
                        self.state = 187
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = ZCodeParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 190
                        self.match(ZCodeParser.OPEN_BRACKET)
                        self.state = 191
                        self.index_operators()
                        self.state = 192
                        self.match(ZCodeParser.CLOSE_BRACKET)
                        pass

             
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_sign_operands)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.literal()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
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
        self.enterRule(localctx, 14, self.RULE_not_operands)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.literal()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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
        self.enterRule(localctx, 16, self.RULE_index_operators)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.expression(0)
                self.state = 209
                self.match(ZCodeParser.COMMA)
                self.state = 210
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
        self.enterRule(localctx, 18, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 215
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 216
            self.param_list()
            self.state = 217
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
        self.enterRule(localctx, 20, self.RULE_param_list)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 20, 34, 39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.param_prime()
                pass
            elif token in [35]:
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
        self.enterRule(localctx, 22, self.RULE_param_prime)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.param()
                self.state = 224
                self.match(ZCodeParser.COMMA)
                self.state = 225
                self.param_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
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
        self.enterRule(localctx, 26, self.RULE_non_rel_operators)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.mul_operators()
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.add_operators()
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.logic_operators()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
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
        self.enterRule(localctx, 28, self.RULE_non_str_operators)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.mul_operators()
                pass
            elif token in [19, 20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.add_operators()
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.logic_operators()
                pass
            elif token in [26, 27, 28, 29, 30, 31, 32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
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
        self.enterRule(localctx, 30, self.RULE_non_associative_operands)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.func_call()
                self.state = 247
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 248
                self.index_operators()
                self.state = 249
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.literal()
                self.state = 252
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 253
                self.index_operators()
                self.state = 254
                self.match(ZCodeParser.CLOSE_BRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 256
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 257
                self.func_call()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.match(ZCodeParser.SUB_OPERATOR)
                self.state = 259
                self.literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 260
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 261
                self.func_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 262
                self.match(ZCodeParser.NOT_OPERATOR)
                self.state = 263
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
        self.enterRule(localctx, 32, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34304) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8246337208320) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_mul_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_add_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
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
        self.enterRule(localctx, 40, self.RULE_logic_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
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
        self.enterRule(localctx, 42, self.RULE_rel_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8522825728) != 0)):
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
        self.enterRule(localctx, 44, self.RULE_str_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Param_declContext,0)


        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(ZCodeParser.T__0)
            self.state = 281
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 282
            self.param_decl()
            self.state = 283
            self.newline_list()
            self.state = 284
            self.body()
            self.state = 285
            self.newline_list()
            self.state = 286
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PARENTHESIS(self):
            return self.getToken(ZCodeParser.OPEN_PARENTHESIS, 0)

        def param_decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_decl_listContext,0)


        def CLOSE_PARENTHESIS(self):
            return self.getToken(ZCodeParser.CLOSE_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_decl




    def param_decl(self):

        localctx = ZCodeParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ZCodeParser.OPEN_PARENTHESIS)
            self.state = 289
            self.param_decl_list()
            self.state = 290
            self.match(ZCodeParser.CLOSE_PARENTHESIS)
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
        self.enterRule(localctx, 50, self.RULE_param_decl_list)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.param_decl_prime()
                pass
            elif token in [35]:
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
        self.enterRule(localctx, 52, self.RULE_param_decl_prime)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.param_single_decl()
                self.state = 297
                self.match(ZCodeParser.COMMA)
                self.state = 298
                self.param_decl_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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
        self.enterRule(localctx, 54, self.RULE_param_single_decl)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.typ()
                self.state = 304
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.typ()
                self.state = 307
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 308
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 309
                self.arrlist()
                self.state = 310
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
        self.enterRule(localctx, 56, self.RULE_newline_list)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(ZCodeParser.NEWLINE)
                self.state = 315
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
        self.enterRule(localctx, 58, self.RULE_body)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.statement_block()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.ret()
                pass
            elif token in [25]:
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

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_block




    def statement_block(self):

        localctx = ZCodeParser.Statement_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.T__1)
            self.state = 325
            self.statement_list()
            self.state = 326
            self.match(ZCodeParser.T__2)
            self.state = 327
            self.newline_list()
            self.state = 328
            self.match(ZCodeParser.NEWLINE)
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

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statement_list)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 20, 34, 39, 40, 41, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.statement()
                self.state = 331
                self.statement_list()
                pass
            elif token in [3]:
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 339
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 340
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 341
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 342
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 343
                self.func_call_statement()
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ret




    def ret(self):

        localctx = ZCodeParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ret)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(ZCodeParser.T__3)
                self.state = 347
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(ZCodeParser.T__3)
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


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.ret()
            self.state = 352
            self.newline_list()
            self.state = 353
            self.match(ZCodeParser.NEWLINE)
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


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_statement




    def func_call_statement(self):

        localctx = ZCodeParser.Func_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_func_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.func_call()
            self.state = 356
            self.newline_list()
            self.state = 357
            self.match(ZCodeParser.NEWLINE)
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


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.lhs()
            self.state = 360
            self.match(ZCodeParser.ASSIGN_OPERATOR)
            self.state = 361
            self.rhs()
            self.state = 362
            self.newline_list()
            self.state = 363
            self.match(ZCodeParser.NEWLINE)
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def OPEN_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_lhs)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.expression(0)
                self.state = 367
                self.match(ZCodeParser.OPEN_BRACKET)
                self.state = 368
                self.index_operators()
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
        self.enterRule(localctx, 76, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(ZCodeParser.T__4)
            self.state = 376
            self.newline_list()
            self.state = 377
            self.match(ZCodeParser.NEWLINE)
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ZCodeParser.T__5)
            self.state = 380
            self.newline_list()
            self.state = 381
            self.match(ZCodeParser.NEWLINE)
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(ZCodeParser.T__6)
            self.state = 384
            self.newline_list()
            self.state = 385
            self.match(ZCodeParser.NEWLINE)
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

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(ZCodeParser.T__7)
            self.state = 388
            self.newline_list()
            self.state = 389
            self.match(ZCodeParser.NEWLINE)
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
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         




