grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

//Modify ZCode.g4 to detect tokens in ZCode language
//In this phase, you are required to write a recognizer for a program written in ZCode. 
//To complete this phase, you need to:
// - Make 100 testcases for ParserSuite to test your code
// - You can assume that there is at most one error in each testcase

//WORKING ON PARSER


program:  EOF;


//CÁI GÌ LÀ CỐ ĐỊNH THÌ ĐƯA LÊN ĐẦU: KEYWORDS, PARENTHESES,..

//COMMENT
COMMENT: '##' ~[\r\n]*;

//RESERVED WORDS

type: BOOLEAN_TYPE | NUMERIC_TYPE | STRING_TYPE;

// STRING DEFINITIONS
STRING_TYPE: 'string';
STRING_OPERATOR: 
	'...'
;

// BOOLEAN DEFINITIONS
BOOLEAN_TYPE: 'bool';
LOGIC_OPERATOR: 'not' | 'and' | 'or';

// NUMERIC DEFINITIONS
NUMERIC_TYPE: 'number';
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
	'var'
	|
	'dynamic'
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
CHARSET: [\n];

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
SEPARATOR: OPEN_BRACKET | CLOSE_BRACKET | OPEN_PARENTHESIS | CLOSE_PARENTHESIS | COMMA;
fragment OPEN_PARENTHESIS: '(' ;
fragment CLOSE_PARENTHESIS: ')';
fragment OPEN_BRACKET: '[';
fragment CLOSE_BRACKET: ']';
fragment COMMA: ',';

//LITERALS
BOOLEAN:'true'|'false';

NUMBER: DIGIT+ ('.' DIGIT*)? EXPONENT? | DIGIT+ EXPONENT ;
fragment DIGIT: [0-9];
fragment EXPONENT: [eE][+-]? DIGIT+;

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

//IDENTIFIERS
IDENTIFIER: [a-zA-Z_] [A-Za-z0-9_]*;





WS : [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};