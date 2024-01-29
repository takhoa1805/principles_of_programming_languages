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

program:decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl;
vardecl: 
	//Declaration only
	typ IDENTIFIER NEWLINE
	|
	DYNAMIC_TYPE IDENTIFIER NEWLINE
	|
	//Declaration with initialization value
	VAR_TYPE IDENTIFIER ASSIGN_OPERATOR exp NEWLINE
	|
	typ IDENTIFIER ASSIGN_OPERATOR exp NEWLINE
	|
	DYNAMIC_TYPE IDENTIFIER ASSIGN_OPERATOR exp NEWLINE
	|
	//Array declaration only
	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET NEWLINE
	|
	//Array declaration with initialization values
	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET ASSIGN_OPERATOR arrexp NEWLINE
;
arrlist: NUMBER COMMA arrlist | NUMBER;
arrexp: 'arrayexpression';
exp: 'expression';



funcdecl: NEWLINE;

typ: BOOL_TYPE | NUMBER_TYPE | STRING_TYPE;


DYNAMIC_TYPE: 'dynamic';
VAR_TYPE: 'var';
//COMMENT
COMMENT: '##' ~[\r\n]*;

// STRING DEFINITIONS
STRING_TYPE: 'string';
STRING_OPERATOR: 
	'...'
;

// BOOLEAN DEFINITIONS
BOOL_TYPE: 'bool';
LOGIC_OPERATOR: 'not' | 'and' | 'or';

// NUMERIC DEFINITIONS
NUMBER_TYPE: 'number';
ARITHMETIC_OPERATORS: 
	'+'
	|
	'-'
	|
	'*'
	|
	'/'
	|
	'%'

;

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
RELATIONAL_OPERATOR:
	'='
	|
	'!='
	|
	'<'
	|
	'>'
	|
	'<='
	|
	'>='
	|
	'=='
;

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