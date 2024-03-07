grammar ZCode;

@lexer::header {
from lexererr import *
2113773
}

options {
	language=Python3;
}


program: newline_list decllist EOF;
decllist:  decl decllist | decl ;
decl: vardecl | funcdecl ;


//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
//--------------------------VAR DECLARATION--------------------------//
//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
vardecl: 
	vardecl_only
	|
	vardecl_init
;
vardecl_only:	
	typ IDENTIFIER NEWLINE newline_list
	|
	DYNAMIC_TYPE IDENTIFIER NEWLINE newline_list
	|
	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET NEWLINE newline_list
;
vardecl_init:
	//Declaration with initialization value
	VAR_TYPE IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
	|
	typ IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
	|
	DYNAMIC_TYPE IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
	|
	//Array declaration with initialization values
	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET ASSIGN_OPERATOR expression NEWLINE newline_list
;

arrlist: NUMBER COMMA arrlist | NUMBER;
array_expression: OPEN_BRACKET arrlist CLOSE_BRACKET | arrlist;
arrlist_expression: OPEN_BRACKET array_expression COMMA arrlist_expression CLOSE_BRACKET | array_expression;
array_literal: OPEN_BRACKET array_literal_prime CLOSE_BRACKET | OPEN_BRACKET CLOSE_BRACKET;
array_literal_prime: expression COMMA array_literal_prime | expression;
expression: 
    expression OPEN_BRACKET index_operators CLOSE_BRACKET
	// |
	// IDENTIFIER OPEN_BRACKET index_operators CLOSE_BRACKET
	// |
	// func_call OPEN_BRACKET index_operators CLOSE_BRACKET
	|
	<assoc=right>SUB_OPERATOR expression
	|
	<assoc=right>NOT_OPERATOR expression
	|
	expression mul_operators expression
	|
	expression add_operators expression
	|
	expression logic_operators expression
	|
	expression rel_operators expression
	|
	expression str_operators expression
	|
	IDENTIFIER OPEN_PARENTHESIS  param_list CLOSE_PARENTHESIS
	|
	literal
	|
	array_literal
;
sign_operands: literal | SUB_OPERATOR ;
not_operands: literal | NOT_OPERATOR;
index_operators: expression | expression COMMA index_operators;
func_call: IDENTIFIER OPEN_PARENTHESIS  param_list CLOSE_PARENTHESIS;
param_list: param_prime | ;
param_prime: param COMMA param_prime | param;
param: expression;
non_rel_operators: mul_operators | add_operators | logic_operators |str_operators;
non_str_operators: mul_operators | add_operators | logic_operators |rel_operators;


non_associative_operands: 
	func_call 
	| 
	literal
	|
	func_call OPEN_BRACKET index_operators CLOSE_BRACKET
	|
	literal OPEN_BRACKET index_operators CLOSE_BRACKET
	|
	<assoc=right>SUB_OPERATOR func_call
	|
	<assoc=right>SUB_OPERATOR literal
	|
	<assoc=right>NOT_OPERATOR func_call
	|
	<assoc=right>NOT_OPERATOR literal
;


typ: BOOL_TYPE | NUMBER_TYPE | STRING_TYPE;

literal: STRING | NUMBER | BOOLEAN | IDENTIFIER;

mul_operators: MUL_OPERATOR | DIV_OPERATOR | MOD_OPERATOR;
add_operators: ADD_OPERATOR | SUB_OPERATOR;
logic_operators: AND_OPERATOR | OR_OPERATOR;
rel_operators: 
	EQ_OPERATOR 
	| 
	SEQ_OPERATOR 
	| 
	NEQ_OPERATOR 
	| 
	LT_OPERATOR
	|
	GT_OPERATOR
	|
	LEQ_OPERATOR
	|
	GEQ_OPERATOR
;
str_operators: STRING_OPERATOR;

//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
//-----------------------END OF VAR DECLARATION----------------------//
//-------------------------------------------------------------------//
//-------------------------------------------------------------------//


//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
//-------------------------FUNC DECLARATION--------------------------//
//-------------------------------------------------------------------//
//-------------------------------------------------------------------//

funcdecl: 'func' IDENTIFIER OPEN_PARENTHESIS param_decl_list CLOSE_PARENTHESIS newline_list body  newline_list;


param_decl_list: param_decl_prime | ;
param_decl_prime: 
	param_single_decl COMMA param_decl_prime 
	| 
	param_single_decl
;
param_single_decl:
	//Declaration only
	typ IDENTIFIER 
	|
	//Array declaration only
	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET 
;
newline_list: NEWLINE newline_list |  ;

body: statement_block | ret |  ;

statement_block: BEGIN statement_list END NEWLINE newline_list;
statement_list: newline_list statement newline_list statement_list | newline_list;
statement: 
	vardecl
	|
	assignment_statement 
	|
	if_statement 
	|
	for_statement 
	|
	break_statement 
	|
	continue_statement 
	|
	return_statement 
	|
	func_call_statement 
	|
	statement_block
;

ret: RETURN expression | RETURN;
return_statement: ret NEWLINE newline_list;
func_call_statement: func_call NEWLINE newline_list;

assignment_statement: lhs ASSIGN_OPERATOR rhs NEWLINE newline_list;
lhs: expression;
rhs: expression;

// if_statement: IF OPEN_PARENTHESIS expression CLOSE_PARENTHESIS if_body elif_statement_list else_statement NEWLINE newline_list;
if_statement: IF OPEN_PARENTHESIS expression CLOSE_PARENTHESIS if_body elif_statement_list else_statement newline_list;

if_body:
	statement
	|
	statement_block
	|
	NEWLINE
;

elif_statement_list: elif_statement elif_statement_list |  ;
elif_statement: ELIF OPEN_PARENTHESIS expression CLOSE_PARENTHESIS if_body;
else_statement: ELSE if_body |  ;


for_statement: FOR IDENTIFIER UNTIL expression BY expression newline_list for_body;
for_body: 	
	statement
	|
	statement_block
	|
	NEWLINE
;

break_statement: BREAK_STATEMENT NEWLINE newline_list;
continue_statement: CONTINUE_STATEMENT NEWLINE newline_list;

//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
//-----------------------END OF FUNC DECLARATION---------------------//
//-------------------------------------------------------------------//
//-------------------------------------------------------------------//



//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
//-------------------------------LEXER-------------------------------//
//-------------------------------------------------------------------//
//-------------------------------------------------------------------//


STRING_TYPE: 'string';
NUMBER_TYPE: 'number';
DYNAMIC_TYPE: 'dynamic';
VAR_TYPE: 'var';


FOR_STATEMENT: 'for statement';
BREAK_STATEMENT: 'break';
CONTINUE_STATEMENT: 'continue';


FUNC: 'func';
BEGIN: 'begin';
END: 'end';
RETURN: 'return';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
FOR: 'for';
UNTIL: 'until';
BY: 'by';


//COMMENT
COMMENT: '##' ~[\r\n]* -> skip;

// STRING DEFINITIONS
STRING_OPERATOR: 
	'...'
;

// BOOLEAN DEFINITIONS
BOOL_TYPE: 'bool';
NOT_OPERATOR: 'not';
AND_OPERATOR: 'and';
OR_OPERATOR: 'or';

// NUMERIC DEFINITIONS
ADD_OPERATOR: '+' ;
SUB_OPERATOR: '-';
MUL_OPERATOR: '*';
DIV_OPERATOR: '/';
MOD_OPERATOR: '%';



NEWLINE: '\n' | '\r\n';

//OPERATORS
EQ_OPERATOR: '=';
NEQ_OPERATOR: '!=';
LT_OPERATOR: '<';
GT_OPERATOR: '>';
LEQ_OPERATOR: '<=';
GEQ_OPERATOR: '>=';
SEQ_OPERATOR: '==';

ASSIGN_OPERATOR:
	'<-'
;
//SEPARATORS
OPEN_PARENTHESIS: '(' ;
CLOSE_PARENTHESIS: ')';
OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';
COMMA: ',';

//LITERALS
BOOLEAN:'true'|'false';

NUMBER: DIGIT+ ('.' DIGIT*)? EXPONENT? | DIGIT+ EXPONENT ;
fragment DIGIT: [0-9];
fragment EXPONENT: [eE][+-]? DIGIT+;

//IDENTIFIERS
IDENTIFIER: [a-zA-Z_] [A-Za-z0-9_]*;

//STRING_LIT: '"' (~[\r\n\f\\'"] | '\\' [bfrnt\\'] | '\'"')* '"' {self.text = self.text[1:-1];};
STRING: DOUBLE_QUOTE (~[\n\r"\\'] |LEGAL_ESCAPE_SEQUENCE | DOUBLE_QUOTE_NOTATION)* DOUBLE_QUOTE
{
	self.text = self.text[1:-1]
	#print("this is a string: "+self.text)
};
fragment DOUBLE_QUOTE: '"';
fragment DOUBLE_QUOTE_NOTATION: '\'"';
fragment LEGAL_ESCAPE_SEQUENCE: '\\'[bfrnt'\\];
fragment ILLEGAL_ESCAPE_SEQUENCE: '\\''\\'~[bfrnt'\\];


UNCLOSE_STRING: DOUBLE_QUOTE ((~["\\']|DOUBLE_QUOTE_NOTATION|LEGAL_ESCAPE_SEQUENCE)*([\n\r]| EOF))
{
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
};

ILLEGAL_ESCAPE:  DOUBLE_QUOTE ((~["\n\r]|DOUBLE_QUOTE_NOTATION|LEGAL_ESCAPE_SEQUENCE)*('\\'~[bfrnt'\\] | [']~["]))
{
	self.text = self.text[1:]
	#print("this is illegal escape: "+self.text)
	raise IllegalEscape(self.text)
	
}
;




WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};