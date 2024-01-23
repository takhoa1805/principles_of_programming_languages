grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

//Modify ZCode.g4 to detect tokens in ZCode language
//Make 100 testcases for LexerSuite to test your code
//For lexical error, please return the following tokens together with specific lexemes:
//	- ERROR_TOKEN with <unrecognized char> lexeme: when the lexer detects an unrecognized character
//	- UNCLOSE_STRING with <unclosed string> lexeme: when the lexer detects an
// 	 unterminated string. The <unclosed string> lexeme does not include the opening quote.
// – ILLEGAL_ESCAPE with <wrong string> lexeme: when the lexer detects an
// 	 illegal escape in string. The wrong string is from the beginning of the string (without
// 	 the opening quote) to the illegal escape
//You can assume that there is only one error in each testcase.


//WORKING ON ILLEGAL ESCAPE SEQUENCES


program: EOF;
//CÁI GÌ LÀ CỐ ĐỊNH THÌ ĐƯA LÊN ĐẦU: KEYWORDS, PARENTHESES,..

//COMMENT
COMMENT: '##' ~[\r\n]*;

//RESERVED WORDS
KEYWORD: 
	'number'
	|
	'bool'
	|
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
	'if'
	|
	'else'
	|
	'elif'
	|
	'begin'
	|
	'true'
	|
	'false'

;
CHARSET: [\n];

//OPERATORS
OPERATOR:
	'+'
	|
	'-'
	|
	'*'
	|
	'/'
	|
	'%'
	|
	'<-'
	|
	'not'
	|
	'and'
	|
	'or'
	|
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
	'...'
	|
	'=='
;

//SEPARATORS
SEPARATOR: OPEN_BRACKET | CLOSE_BRACKET | OPEN_PARENTHESIS | CLOSE_PARENTHESIS | COMMA;
fragment OPEN_PARENTHESIS: '(' ;
fragment CLOSE_PARENTHESIS: ')';
fragment OPEN_BRACKET: '[';
fragment CLOSE_BRACKET: ']';
fragment COMMA: ',';

//LITERALS
NUMBER: DIGIT+ ('.' DIGIT*)? EXPONENT? | DIGIT+ EXPONENT ;
fragment DIGIT: [0-9];
fragment EXPONENT: [eE][+-]? DIGIT+;


STRING: DOUBLE_QUOTE ((~[\n]|DOUBLE_QUOTE_NOTATION|LEGAL_ESCAPE_SEQUENCE)*LEGAL_ESCAPE_SEQUENCE*) DOUBLE_QUOTE
{
	self.text = self.text[1:-1]
	print("this is a string: "+self.text)
};
fragment DOUBLE_QUOTE: '"';
fragment DOUBLE_QUOTE_NOTATION: '\'"';
fragment LEGAL_ESCAPE_SEQUENCE: '\\\\'[bfrnt'\\];
fragment ILLEGAL_ESCAPE_SEQUENCE: '\\''\\'~[bfrnt'\\];


UNCLOSE_STRING: DOUBLE_QUOTE ((~["]|DOUBLE_QUOTE_NOTATION|LEGAL_ESCAPE_SEQUENCE)*([\n]| EOF))
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

ILLEGAL_ESCAPE:  DOUBLE_QUOTE (((~[\n]|DOUBLE_QUOTE_NOTATION)*LEGAL_ESCAPE_SEQUENCE*)(ILLEGAL_ESCAPE_SEQUENCE))
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