grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


//WORKING ON PARSER

// - block ngoài cùng chỉ có thể có variable/function declaration mà thôi
// - function ends up with a return statement or a block statement. 
//  The nullable list of newline characters can be used to separate the parameter declaration and the body of the function
// ==> một function có thể có 1 hoặc 0 block statement, có thể có 1 hoặc 0 return statement

program: decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl ;


//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
//--------------------------VAR DECLARATION--------------------------//
//-------------------------------------------------------------------//
//-------------------------------------------------------------------//
vardecl: 
	//Declaration only
	typ IDENTIFIER newline_list NEWLINE
	|
	DYNAMIC_TYPE IDENTIFIER newline_list NEWLINE
	|
	//Declaration with initialization value
	VAR_TYPE IDENTIFIER ASSIGN_OPERATOR expression newline_list NEWLINE
	|
	typ IDENTIFIER ASSIGN_OPERATOR expression newline_list NEWLINE
	|
	DYNAMIC_TYPE IDENTIFIER ASSIGN_OPERATOR expression newline_list NEWLINE
	|
	//Array declaration only
	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET newline_list NEWLINE
	|
	//Array declaration with initialization values
	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET ASSIGN_OPERATOR expression newline_list NEWLINE
;
arrlist: NUMBER COMMA arrlist | NUMBER;
expression: 
	expression OPEN_BRACKET index_operators CLOSE_BRACKET
	|
	OPEN_PARENTHESIS expression CLOSE_PARENTHESIS
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
	// |
	// non_associative_operands rel_operators non_associative_operands ===> FOR SEMANTIC STEP?
	|
	expression rel_operators expression
	// |
	// non_associative_operands str_operators non_associative_operands ===> FOR SEMANTIC STEP?
	|
	expression str_operators expression
	|
	func_call
	|
	literal
	
;
sign_operands: literal | SUB_OPERATOR ;
not_operands: literal | NOT_OPERATOR;
index_operators: expression | expression COMMA index_operators;
func_call: IDENTIFIER OPEN_PARENTHESIS  param_list CLOSE_PARENTHESIS;
param_list: param_prime | ;
param_prime: param COMMA param_prime | param;
param: 
	expression
;
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

STRING_TYPE: 'string';
NUMBER_TYPE: 'number';
DYNAMIC_TYPE: 'dynamic';
VAR_TYPE: 'var';

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

// funcdecl: 'func' IDENTIFIER OPEN_PARENTHESIS param_decl_list CLOSE_PARENTHESIS newline_list body ;
funcdecl:'func' IDENTIFIER param_decl newline_list body newline_list NEWLINE;
param_decl: OPEN_PARENTHESIS param_decl_list CLOSE_PARENTHESIS;


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
newline_list: NEWLINE newline_list | ;

body: statement_block | ret | ;

statement_block: 'begin' statement_list 'end' newline_list NEWLINE;
statement_list: statement statement_list | ;
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
;

ret: 'return' expression | 'return';
return_statement: ret newline_list NEWLINE;
func_call_statement: func_call newline_list NEWLINE;

assignment_statement: lhs ASSIGN_OPERATOR rhs newline_list NEWLINE;
lhs: 
	IDENTIFIER
	|
	expression OPEN_BRACKET index_operators CLOSE_BRACKET
;
rhs: expression;

if_statement: 'if statement' newline_list NEWLINE ;
for_statement: 'for statement' newline_list NEWLINE;
break_statement: 'break statement' newline_list NEWLINE;
continue_statement: 'continue statement' newline_list NEWLINE;




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


KEYWORD: 
	'return'
	|
	'func'
	|
	'for'
	|
	'until'
	|
	'by'
	|
	'break'
	|
	'continue'
	|
	'if'
	|
	'else'
	|
	'elif'
	|
	'begin'
	|
	'end'
;
NEWLINE: [\n];

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
};

ILLEGAL_ESCAPE:  DOUBLE_QUOTE ((~["\n\r]|DOUBLE_QUOTE_NOTATION|LEGAL_ESCAPE_SEQUENCE)*('\\'~[bfrnt'\\] | [']~["]))
{
	self.text = self.text[1:]
	print("this is illegal escape: "+self.text)
	raise IllegalEscape(self.text)
	
}
;




WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};