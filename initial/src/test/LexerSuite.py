import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifiers(self):
        """test identifiers"""  
        #TRUE ID
        self.assertTrue(TestLexer.test("A _ a az AZ aZ _a a_ a1 _1 A1", "A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>", 11))     

        ##FALSE ID
        self.assertTrue(TestLexer.test("1Tienc", "1,Tienc,<EOF>", 12))
        self.assertTrue(TestLexer.test("11Tienc", "11,Tienc,<EOF>", 13))
        self.assertTrue(TestLexer.test(".something","Error Token .",14))
        self.assertTrue(TestLexer.test("some.thing","some,Error Token .",15))
    
    def test_comments(self):
        """test comments"""
        #TRUE COMMENTS
        self.assertTrue(TestLexer.test("##THIS IS A COMMENT","##THIS IS A COMMENT,<EOF>",21))
        self.assertTrue(TestLexer.test("###THIS IS A COMMENT #","###THIS IS A COMMENT #,<EOF>",22))
        self.assertTrue(TestLexer.test("##Variable a\nnumber a\n ","##Variable a,\n,number,a,\n,<EOF>",23))
        self.assertTrue(TestLexer.test("number a ##Variable a","number,a,##Variable a,<EOF>",24))


        #FALSE COMMENTS
        self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",25))     
        self.assertTrue(TestLexer.test("some#thing","some,Error Token #",26))


    def test_keywords(self):
        """test keywords"""
        # TRUE KEYWORDS
        self.assertTrue(TestLexer.test("+-*/%not and or =<-!=<<=>>=...==", "+,-,*,/,%,not,and,or,=,<-,!=,<,<=,>,>=,...,==,<EOF>", 31))     
        self.assertTrue(TestLexer.test("a+b-c/d%20", "a,+,b,-,c,/,d,%,20,<EOF>", 32))     
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 33))  
        self.assertTrue(TestLexer.test("true is not false", "true,is,not,false,<EOF>", 34))  

        # FALSE KEYWORDS
        self.assertTrue(TestLexer.test("and &", "and,Error Token &", 35))  


    def test_numbers(self):
        """test numbers"""
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 41))     
        self.assertTrue(TestLexer.test("12.3e-3", "12.3e-3,<EOF>", 42))   
        self.assertTrue(TestLexer.test("12.2h-3","12.2,h,-,3,<EOF>",43))

    

    def test_separators(self):
        """test separators"""   
        self.assertTrue(TestLexer.test("[(,,)]","[,(,,,,,),],<EOF>",51))
    
    def test_strings(self):
        """test strings"""
        #Simple tests
        self.assertTrue(TestLexer.test(""" "'"Vo '" Tien '"" ""","'\"Vo '\" Tien '\",<EOF>",61))
        self.assertTrue(TestLexer.test(""" "" """,",<EOF>",62)) # chuỗi rỗng
        self.assertTrue(TestLexer.test(""" "This string contains legal escapce sequeces \\b \\f \\r \\n \\t \\\' \\\\" ""","This string contains legal escapce sequeces \\b \\f \\r \\n \\t \\\' \\\\,<EOF>",63)) 
        self.assertTrue(TestLexer.test(""" "Vo  Tien" ""","Vo  Tien,<EOF>",64))
        self.assertTrue(TestLexer.test(""" "He asked me: '"Where is John?'"" ""","He asked me: '\"Where is John?'\",<EOF>",65))
        
        # Unclosed string
        self.assertTrue(TestLexer.test(""" "Vo  Tien ""","Unclosed String: Vo  Tien ",66))
        self.assertTrue(TestLexer.test(""" "Vo \n" """, "Unclosed String: Vo ", 67))
        self.assertTrue(TestLexer.test(""" "Vo \n Tien" """, "Unclosed String: Vo ", 68))
        self.assertTrue(TestLexer.test(""" "Vo  """, "Unclosed String: Vo  ", 69))
        self.assertTrue(TestLexer.test(""" "Vo \\n \n """, "Unclosed String: Vo \\n ", 610))
        self.assertTrue(TestLexer.test(""" "Vo \\n \\b """, "Unclosed String: Vo \\n \\b ", 611))
        self.assertTrue(TestLexer.test(""" "Vovo \\n \\n \n" """, "Unclosed String: Vovo \\n \\n ", 612))

        # # #Complex test
        self.assertTrue(TestLexer.test(" \"This \\nString \\nHas \\nFour lines\" \n","This \\nString \\nHas \\nFour lines,\n,<EOF>",613))
        self.assertTrue(TestLexer.test("String a = \"this is a string 123\"\n","String,a,=,this is a string 123,\n,<EOF>",614))
        self.assertTrue(TestLexer.test("String a = \"this is a string 123\n","String,a,=,Unclosed String: this is a string 123",615))
        self.assertTrue(TestLexer.test("String a = \"this is a string 123\\n","String,a,=,Unclosed String: this is a string 123\\n",616))

        #Illegal escape
        self.assertTrue(TestLexer.test(""" "Tien \\1"  """, "Illegal Escape In String: Tien \\1", 617))
        self.assertTrue(TestLexer.test(""" "Tien \\2 \\n \n """, "Illegal Escape In String: Tien \\2", 618))
        self.assertTrue(TestLexer.test(""" "Tien \\e \\n \\r """, "Illegal Escape In String: Tien \\e", 619))        
        self.assertTrue(TestLexer.test(""" "Tien \\321 \\n \\r """, "Illegal Escape In String: Tien \\3", 620))
        self.assertTrue(TestLexer.test(""" "Tien \\"1 " """, "Illegal Escape In String: Tien \\\"", 621))          
        self.assertTrue(TestLexer.test(""" "Tien ' " " """, "Illegal Escape In String: Tien ' ", 622))
        self.assertTrue(TestLexer.test(""" "Tien \\' ""1 """, "Tien \\' ,Unclosed String: 1 ", 623))  
        


    def test_all(self):
        """test anything"""
        # self.assertTrue(TestLexer.test(""" "" """,",<EOF>",1001)) # chuỗi rỗng
        # self.assertTrue(TestLexer.test(""" "Vo """, "Unclosed String: Vo ", 1001))


    def test_case_0(self):
        input = """
dynamic
number for >=	false	continue - "abcd"	else func	not % bool break end	bool number true	continue
    """
        expect = "\n,dynamic,\n,number,for,>=,false,continue,-,abcd,else,func,not,%,bool,break,end,bool,number,true,continue,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,100))
        except:
            print("fail testcase 0")
        
    def test_case_1(self):
        input = """	else	] >=
%
!= ) (
begin >= for dynamic a1	bool	[	%
continue break	by	number	and + number "abcd"	string a1	< by	(
not	>=	bool	bool +
func or return	(	)	!= !=	false - ,
...	by	93.20e-324 = 
 [
false	string	/ number and	continue >
[	<-	=
    """
        expect = "else,],>=,\n,%,\n,!=,),(,\n,begin,>=,for,dynamic,a1,bool,[,%,\n,continue,break,by,number,and,+,number,abcd,string,a1,<,by,(,\n,not,>=,bool,bool,+,\n,func,or,return,(,),!=,!=,false,-,,,\n,...,by,93.20e-324,=,\n,[,\n,false,string,/,number,and,continue,>,\n,[,<-,=,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,101))
        except:
            print("fail testcase 1")
        
    def test_case_2(self):
        input = """	begin false	/
<- for	!= = begin for elif	* if until 42e-2809 <-	else end a1
, else	... ... else
>= func	>=	( <-	<- / == <	=	bool var	<-	== a1
begin
( <- not

 [ ] end false +
bool	+ for	true + )	...	/	bool if 59
    """
        expect = "begin,false,/,\n,<-,for,!=,=,begin,for,elif,*,if,until,42e-2809,<-,else,end,a1,\n,,,else,...,...,else,\n,>=,func,>=,(,<-,<-,/,==,<,=,bool,var,<-,==,a1,\n,begin,\n,(,<-,not,\n,\n,[,],end,false,+,\n,bool,+,for,true,+,),...,/,bool,if,59,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,102))
        except:
            print("fail testcase 2")
        
    def test_case_3(self):
        input = """
dynamic break
*	<
( + , elif end number	for
until	return elif	by	dynamic	
	!=	% return	, <=
) else else >=
not	number by	string 
 func	break	if and until - elif ) (	- % 
 true
> not / not	return	=	<	]	continue var [	by false "abcd"	begin
false return	< begin elif	false	!= ( false , var
== true break != else <=	...	+	( var	begin + -	true != % not	*	func	string a1	continue
true	[	/	else	"abcd"	bool 

    """
        expect = "\n,dynamic,break,\n,*,<,\n,(,+,,,elif,end,number,for,\n,until,return,elif,by,dynamic,\n,!=,%,return,,,<=,\n,),else,else,>=,\n,not,number,by,string,\n,func,break,if,and,until,-,elif,),(,-,%,\n,true,\n,>,not,/,not,return,=,<,],continue,var,[,by,false,abcd,begin,\n,false,return,<,begin,elif,false,!=,(,false,,,var,\n,==,true,break,!=,else,<=,...,+,(,var,begin,+,-,true,!=,%,not,*,func,string,a1,continue,\n,true,[,/,else,abcd,bool,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,103))
        except:
            print("fail testcase 3")
        
    def test_case_4(self):
        input = """ end ]
and by	]	,
<=
[
= not	<- var	27.5	> = + <- ( var	+	end >= end
    """
        expect = "end,],\n,and,by,],,,\n,<=,\n,[,\n,=,not,<-,var,27.5,>,=,+,<-,(,var,+,end,>=,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,104))
        except:
            print("fail testcase 4")
        
    def test_case_5(self):
        input = """ until	if func until	true	/ , *	) number ,
return	continue	begin and if break , / not continue
4
by >=	<= by	+ if
dynamic	%
%	[	+	for by end begin <- until	continue false	... var 
 false	
	dynamic	by <
,	begin until	(	%	true = not	)	until until else	...
and ,
number
return [
else "abcd"	a1 else	not bool < string	=	== continue	]	number	<
= elif until ( ...	begin	51E-3136	and	continue false
    """
        expect = "until,if,func,until,true,/,,,*,),number,,,\n,return,continue,begin,and,if,break,,,/,not,continue,\n,4,\n,by,>=,<=,by,+,if,\n,dynamic,%,\n,%,[,+,for,by,end,begin,<-,until,continue,false,...,var,\n,false,\n,dynamic,by,<,\n,,,begin,until,(,%,true,=,not,),until,until,else,...,\n,and,,,\n,number,\n,return,[,\n,else,abcd,a1,else,not,bool,<,string,=,==,continue,],number,<,\n,=,elif,until,(,...,begin,51E-3136,and,continue,false,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,105))
        except:
            print("fail testcase 5")
        
    def test_case_6(self):
        input = """ +
<= 
 "abcd" bool * else break ...	]	string	and	else	number
,
60	... bool	- <	/ 112.71 * by if * ] <-	func	true break
) <- if
until !=
begin [ ,	dynamic dynamic	a1
func	>= 87.11e-5184 > = >= 
	var ==
    """
        expect = "+,\n,<=,\n,abcd,bool,*,else,break,...,],string,and,else,number,\n,,,\n,60,...,bool,-,<,/,112.71,*,by,if,*,],<-,func,true,break,\n,),<-,if,\n,until,!=,\n,begin,[,,,dynamic,dynamic,a1,\n,func,>=,87.11e-5184,>,=,>=,\n,var,==,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,106))
        except:
            print("fail testcase 6")
        
    def test_case_7(self):
        input = """ break	a1 %	!=	
 <- <=	func number
not	not dynamic if number "abcd" ( <- >= end and
"abcd" !=
<-
*
not if	... return ]	) "abcd" var begin	<-
/ >= 
 >=	+ string	==	elif	... >=	>= <= continue func bool if %
[ = 
	<= "abcd"

 if
...	( [	(	true	>	>=	by "abcd" dynamic 62.75
break +	<= [ elif	by + dynamic	continue ,	elif
number
bool	> [	
 by	true	continue and

	%
( string bool
    """
        expect = "break,a1,%,!=,\n,<-,<=,func,number,\n,not,not,dynamic,if,number,abcd,(,<-,>=,end,and,\n,abcd,!=,\n,<-,\n,*,\n,not,if,...,return,],),abcd,var,begin,<-,\n,/,>=,\n,>=,+,string,==,elif,...,>=,>=,<=,continue,func,bool,if,%,\n,[,=,\n,<=,abcd,\n,\n,if,\n,...,(,[,(,true,>,>=,by,abcd,dynamic,62.75,\n,break,+,<=,[,elif,by,+,dynamic,continue,,,elif,\n,number,\n,bool,>,[,\n,by,true,continue,and,\n,\n,%,\n,(,string,bool,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,107))
        except:
            print("fail testcase 7")
        
    def test_case_8(self):
        input = """	number 15 else	< string ... ( if 
 <= for number	number bool )
number
... =
break
elif if bool
+ , number	var
end + /	
 false elif a1
for	return ...
or	begin bool until	== - * dynamic	dynamic
    """
        expect = "number,15,else,<,string,...,(,if,\n,<=,for,number,number,bool,),\n,number,\n,...,=,\n,break,\n,elif,if,bool,\n,+,,,number,var,\n,end,+,/,\n,false,elif,a1,\n,for,return,...,\n,or,begin,bool,until,==,-,*,dynamic,dynamic,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,108))
        except:
            print("fail testcase 8")
        
    def test_case_9(self):
        input = """	not	!= (
<=	>=	for	if	bool [ dynamic
<	*
dynamic	for *
else
!= =	!= +	false ,	string
var
not	> < not	break	"abcd" until a1 true
/
by
>	bool	else [ number number >= / by *	) bool	>=
a1 func	until
59	continue or	=
begin
    """
        expect = "not,!=,(,\n,<=,>=,for,if,bool,[,dynamic,\n,<,*,\n,dynamic,for,*,\n,else,\n,!=,=,!=,+,false,,,string,\n,var,\n,not,>,<,not,break,abcd,until,a1,true,\n,/,\n,by,\n,>,bool,else,[,number,number,>=,/,by,*,),bool,>=,\n,a1,func,until,\n,59,continue,or,=,\n,begin,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,109))
        except:
            print("fail testcase 9")
        
    def test_case_10(self):
        input = """dynamic abc123
    """
        expect = "dynamic,abc123,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,110))
        except:
            print("fail testcase 10")
        
    def test_case_11(self):
        input = """dynamic 1ae
    """
        expect = "dynamic,1,ae,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,111))
        except:
            print("fail testcase 11")
        
    def test_case_12(self):
        input = """dynamic 1.232eabc
    """
        expect = "dynamic,1.232,eabc,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,112))
        except:
            print("fail testcase 12")
        
    def test_case_13(self):
        input = """dynamic abC1#
    """
        expect = "dynamic,abC1,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,113))
        except:
            print("fail testcase 13")
        
    def test_case_14(self):
        input = """dynamic _abt
    """
        expect = "dynamic,_abt,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,114))
        except:
            print("fail testcase 14")
        
    def test_case_15(self):
        input = """
## comment
func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,## comment,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,115))
        except:
            print("fail testcase 15")
        
    def test_case_16(self):
        input = """

func main()
begin ## comment
              ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,## comment,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,116))
        except:
            print("fail testcase 16")
        
    def test_case_17(self):
        input = """

func main()
begin 
             ## comment ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,## comment ##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,117))
        except:
            print("fail testcase 17")
        
    def test_case_18(self):
        input = """

func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    ## comment
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,## comment,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,118))
        except:
            print("fail testcase 18")
        
    def test_case_19(self):
        input = """

func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    
end
## comment
    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,## comment,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,119))
        except:
            print("fail testcase 19")
        
    def test_case_20(self):
        input = """string a<-"rMrR\"s a
    """
        expect = "string,a,<-,rMrR,s,a,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,120))
        except:
            print("fail testcase 20")
        
    def test_case_21(self):
        input = """string a<-"SEi8\"s\n\"a
    """
        expect = "string,a,<-,SEi8,s,\n,Unclosed String: a"
        try:
            self.assertTrue(TestLexer.test(input,expect,121))
        except:
            print("fail testcase 21")
        
    def test_case_22(self):
        input = """string a<-"cEAS'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: cEAS'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,122))
        except:
            print("fail testcase 22")
        
    def test_case_23(self):
        input = """string a<-"1Ydg'\"s a
    """
        expect = "string,a,<-,Unclosed String: 1Ydg'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,123))
        except:
            print("fail testcase 23")
        
    def test_case_24(self):
        input = """string a<-"Lzex\"s\n\"a
    """
        expect = "string,a,<-,Lzex,s,\n,Unclosed String: a"
        try:
            self.assertTrue(TestLexer.test(input,expect,124))
        except:
            print("fail testcase 24")
        
    def test_case_25(self):
        input = """string a<-"WuFo\"s a
    """
        expect = "string,a,<-,WuFo,s,a,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,125))
        except:
            print("fail testcase 25")
        
    def test_case_26(self):
        input = """string a<-"Jcbs'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: Jcbs'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,126))
        except:
            print("fail testcase 26")
        
    def test_case_27(self):
        input = """string a<-"BEuU'\"s a
    """
        expect = "string,a,<-,Unclosed String: BEuU'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,127))
        except:
            print("fail testcase 27")
        
    def test_case_28(self):
        input = """string a<-"mJ16'\"s\"
    """
        expect = "string,a,<-,mJ16'\"s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,128))
        except:
            print("fail testcase 28")
        
    def test_case_29(self):
        input = """string a<-"IZ8Q'\"s\"
    """
        expect = "string,a,<-,IZ8Q'\"s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,129))
        except:
            print("fail testcase 29")
        
    def test_case_30(self):
        input = """ true [ ;
    """
        expect = "true,[,Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,130))
        except:
            print("fail testcase 30")
        
    def test_case_31(self):
        input = """ string , func continue not dynamic ... !
    """
        expect = "string,,,func,continue,not,dynamic,...,Error Token !"
        try:
            self.assertTrue(TestLexer.test(input,expect,131))
        except:
            print("fail testcase 31")
        
    def test_case_32(self):
        input = """ = @
    """
        expect = "=,Error Token @"
        try:
            self.assertTrue(TestLexer.test(input,expect,132))
        except:
            print("fail testcase 32")
        
    def test_case_33(self):
        input = """ if ( STRINGLIT #
    """
        expect = "if,(,STRINGLIT,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,133))
        except:
            print("fail testcase 33")
        
    def test_case_34(self):
        input = """ for number % ... continue NUMLIT NUMLIT and end ~
    """
        expect = "for,number,%,...,continue,NUMLIT,NUMLIT,and,end,Error Token ~"
        try:
            self.assertTrue(TestLexer.test(input,expect,134))
        except:
            print("fail testcase 34")
        
    def test_case_35(self):
        input = """ begin ^
    """
        expect = "begin,Error Token ^"
        try:
            self.assertTrue(TestLexer.test(input,expect,135))
        except:
            print("fail testcase 35")
        
    def test_case_36(self):
        input = """ ;
    """
        expect = "Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,136))
        except:
            print("fail testcase 36")
        
    def test_case_37(self):
        input = """ @
    """
        expect = "Error Token @"
        try:
            self.assertTrue(TestLexer.test(input,expect,137))
        except:
            print("fail testcase 37")
        
    def test_case_38(self):
        input = """ number * % {
    """
        expect = "number,*,%,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,138))
        except:
            print("fail testcase 38")
        
    def test_case_39(self):
        input = """ IDENTIFIER - var by ( ^
    """
        expect = "IDENTIFIER,-,var,by,(,Error Token ^"
        try:
            self.assertTrue(TestLexer.test(input,expect,139))
        except:
            print("fail testcase 39")
        
    def test_case_40(self):
        input = """ else elif ... func == |
    """
        expect = "else,elif,...,func,==,Error Token |"
        try:
            self.assertTrue(TestLexer.test(input,expect,140))
        except:
            print("fail testcase 40")
        
    def test_case_41(self):
        input = """ var * &
    """
        expect = "var,*,Error Token &"
        try:
            self.assertTrue(TestLexer.test(input,expect,141))
        except:
            print("fail testcase 41")
        
    def test_case_42(self):
        input = """ elif number dynamic ] ~
    """
        expect = "elif,number,dynamic,],Error Token ~"
        try:
            self.assertTrue(TestLexer.test(input,expect,142))
        except:
            print("fail testcase 42")
        
    def test_case_43(self):
        input = """ - return continue ;
    """
        expect = "-,return,continue,Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,143))
        except:
            print("fail testcase 43")
        
    def test_case_44(self):
        input = """ end ... < ( break if NUMLIT break &
    """
        expect = "end,...,<,(,break,if,NUMLIT,break,Error Token &"
        try:
            self.assertTrue(TestLexer.test(input,expect,144))
        except:
            print("fail testcase 44")
        
    def test_case_45(self):
        input = """ &
    """
        expect = "Error Token &"
        try:
            self.assertTrue(TestLexer.test(input,expect,145))
        except:
            print("fail testcase 45")
        
    def test_case_46(self):
        input = """ - number for number STRINGLIT number '
    """
        expect = "-,number,for,number,STRINGLIT,number,Error Token '"
        try:
            self.assertTrue(TestLexer.test(input,expect,146))
        except:
            print("fail testcase 46")
        
    def test_case_47(self):
        input = """ else , = '
    """
        expect = "else,,,=,Error Token '"
        try:
            self.assertTrue(TestLexer.test(input,expect,147))
        except:
            print("fail testcase 47")
        
    def test_case_48(self):
        input = """ {
    """
        expect = "Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,148))
        except:
            print("fail testcase 48")
        
    def test_case_49(self):
        input = """ ~
    """
        expect = "Error Token ~"
        try:
            self.assertTrue(TestLexer.test(input,expect,149))
        except:
            print("fail testcase 49")
        
    def test_case_50(self):
        input = """string s <- " NLEHTR \\e "
    """
        expect = "string,s,<-,Illegal Escape In String:  NLEHTR \\e"
        try:
            self.assertTrue(TestLexer.test(input,expect,150))
        except:
            print("fail testcase 50")
        
    def test_case_51(self):
        input = """string s <- " Toq3 \\  "
    """
        expect = "string,s,<-,Illegal Escape In String:  Toq3 \\ "
        try:
            self.assertTrue(TestLexer.test(input,expect,151))
        except:
            print("fail testcase 51")
        
    def test_case_52(self):
        input = """string s <- " sxz0PUeV \\z "
    """
        expect = "string,s,<-,Illegal Escape In String:  sxz0PUeV \\z"
        try:
            self.assertTrue(TestLexer.test(input,expect,152))
        except:
            print("fail testcase 52")
        
    def test_case_53(self):
        input = """string s <- "  \\e "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\e"
        try:
            self.assertTrue(TestLexer.test(input,expect,153))
        except:
            print("fail testcase 53")
        
    def test_case_54(self):
        input = """string s <- " zPu \\~ "
    """
        expect = "string,s,<-,Illegal Escape In String:  zPu \\~"
        try:
            self.assertTrue(TestLexer.test(input,expect,154))
        except:
            print("fail testcase 54")
        
    def test_case_55(self):
        input = """string s <- " R \\\" "
    """
        expect = "string,s,<-,Illegal Escape In String:  R \\\""
        try:
            self.assertTrue(TestLexer.test(input,expect,155))
        except:
            print("fail testcase 55")
        
    def test_case_56(self):
        input = """string s <- " fSPwGM \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  fSPwGM \\("
        try:
            self.assertTrue(TestLexer.test(input,expect,156))
        except:
            print("fail testcase 56")
        
    def test_case_57(self):
        input = """string s <- " o \\A "
    """
        expect = "string,s,<-,Illegal Escape In String:  o \\A"
        try:
            self.assertTrue(TestLexer.test(input,expect,157))
        except:
            print("fail testcase 57")
        
    def test_case_58(self):
        input = """string s <- " 05KGosOi \\- "
    """
        expect = "string,s,<-,Illegal Escape In String:  05KGosOi \\-"
        try:
            self.assertTrue(TestLexer.test(input,expect,158))
        except:
            print("fail testcase 58")
        
    def test_case_59(self):
        input = """string s <- " NTiKZQYPJ \\a "
    """
        expect = "string,s,<-,Illegal Escape In String:  NTiKZQYPJ \\a"
        try:
            self.assertTrue(TestLexer.test(input,expect,159))
        except:
            print("fail testcase 59")
        
    def test_case_60(self):
        input = """string s <- " D \\u "
    """
        expect = "string,s,<-,Illegal Escape In String:  D \\u"
        try:
            self.assertTrue(TestLexer.test(input,expect,160))
        except:
            print("fail testcase 60")
        
    def test_case_61(self):
        input = """string s <- " pGHA \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  pGHA \\("
        try:
            self.assertTrue(TestLexer.test(input,expect,161))
        except:
            print("fail testcase 61")
        
    def test_case_62(self):
        input = """string s <- " WYQd \\a "
    """
        expect = "string,s,<-,Illegal Escape In String:  WYQd \\a"
        try:
            self.assertTrue(TestLexer.test(input,expect,162))
        except:
            print("fail testcase 62")
        
    def test_case_63(self):
        input = """string s <- " gIQPs \\  "
    """
        expect = "string,s,<-,Illegal Escape In String:  gIQPs \\ "
        try:
            self.assertTrue(TestLexer.test(input,expect,163))
        except:
            print("fail testcase 63")
        
    def test_case_64(self):
        input = """string s <- " 1GwNrpa \\? "
    """
        expect = "string,s,<-,Illegal Escape In String:  1GwNrpa \\?"
        try:
            self.assertTrue(TestLexer.test(input,expect,164))
        except:
            print("fail testcase 64")
        
    def test_case_65(self):
        input = """string s <- " IWQ \\1 "
    """
        expect = "string,s,<-,Illegal Escape In String:  IWQ \\1"
        try:
            self.assertTrue(TestLexer.test(input,expect,165))
        except:
            print("fail testcase 65")
        
    def test_case_66(self):
        input = """string s <- " 5pkLnQ \\z "
    """
        expect = "string,s,<-,Illegal Escape In String:  5pkLnQ \\z"
        try:
            self.assertTrue(TestLexer.test(input,expect,166))
        except:
            print("fail testcase 66")
        
    def test_case_67(self):
        input = """string s <- " sYuwS7 \\e "
    """
        expect = "string,s,<-,Illegal Escape In String:  sYuwS7 \\e"
        try:
            self.assertTrue(TestLexer.test(input,expect,167))
        except:
            print("fail testcase 67")
        
    def test_case_68(self):
        input = """string s <- " PDj2Du \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  PDj2Du \\("
        try:
            self.assertTrue(TestLexer.test(input,expect,168))
        except:
            print("fail testcase 68")
        
    def test_case_69(self):
        input = """string s <- " Tl9Uz5 \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:  Tl9Uz5 \\="
        try:
            self.assertTrue(TestLexer.test(input,expect,169))
        except:
            print("fail testcase 69")
        
    def test_case_70(self):
        input = """breakGZ
    """
        expect = "breakGZ,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,170))
        except:
            print("fail testcase 70")
        
    def test_case_71(self):
        input = """elsePI
    """
        expect = "elsePI,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,171))
        except:
            print("fail testcase 71")
        
    def test_case_72(self):
        input = """if89
    """
        expect = "if89,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,172))
        except:
            print("fail testcase 72")
        
    def test_case_73(self):
        input = """untilLK
    """
        expect = "untilLK,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,173))
        except:
            print("fail testcase 73")
        
    def test_case_74(self):
        input = """forRg
    """
        expect = "forRg,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,174))
        except:
            print("fail testcase 74")
        
    def test_case_75(self):
        input = """elifyC
    """
        expect = "elifyC,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,175))
        except:
            print("fail testcase 75")
        
    def test_case_76(self):
        input = """returnL6
    """
        expect = "returnL6,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,176))
        except:
            print("fail testcase 76")
        
    def test_case_77(self):
        input = """by2s
    """
        expect = "by2s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,177))
        except:
            print("fail testcase 77")
        
    def test_case_78(self):
        input = """funcHI
    """
        expect = "funcHI,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,178))
        except:
            print("fail testcase 78")
        
    def test_case_79(self):
        input = """and4o
    """
        expect = "and4o,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,179))
        except:
            print("fail testcase 79")
        
    def test_case_80(self):
        input = """func fdqI8Kt(p9RfUSH,pYsYWbY,pUG9RC8) \n begin \nvE29yw1 <-1152\n end
    """
        expect = "func,fdqI8Kt,(,p9RfUSH,,,pYsYWbY,,,pUG9RC8,),\n,begin,\n,vE29yw1,<-,1152,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,180))
        except:
            print("fail testcase 80")
        
    def test_case_81(self):
        input = """func f6ucNTT(pl2mxh0,p3b5WsI,pFhEF4B) \n begin \nv9irZPJ <--2100\n end
    """
        expect = "func,f6ucNTT,(,pl2mxh0,,,p3b5WsI,,,pFhEF4B,),\n,begin,\n,v9irZPJ,<-,-,2100,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,181))
        except:
            print("fail testcase 81")
        
    def test_case_82(self):
        input = """var vSFRGe8 <-1365
    """
        expect = "var,vSFRGe8,<-,1365,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,182))
        except:
            print("fail testcase 82")
        
    def test_case_83(self):
        input = """var vKO5kQV <--2007
    """
        expect = "var,vKO5kQV,<-,-,2007,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,183))
        except:
            print("fail testcase 83")
        
    def test_case_84(self):
        input = """func frxyERL(pO5IYdT) \n begin \nfunc fnguOpH(pwyyVWw,pAfx90L,pRAinaq,pTuLgPf) \n begin \nnumber vVD0AKu <--2344\n end\n end
    """
        expect = "func,frxyERL,(,pO5IYdT,),\n,begin,\n,func,fnguOpH,(,pwyyVWw,,,pAfx90L,,,pRAinaq,,,pTuLgPf,),\n,begin,\n,number,vVD0AKu,<-,-,2344,\n,end,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,184))
        except:
            print("fail testcase 84")
        
    def test_case_85(self):
        input = """voDEV1C <-735
    """
        expect = "voDEV1C,<-,735,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,185))
        except:
            print("fail testcase 85")
        
    def test_case_86(self):
        input = """func fVPfDHy(piD2Pjl,pEAPyVD,pO6MaSX,p9AlkSj) \n begin \nfunc f0mtjA9() \n begin \nstring vXwfhKQ <--843\n end\n end
    """
        expect = "func,fVPfDHy,(,piD2Pjl,,,pEAPyVD,,,pO6MaSX,,,p9AlkSj,),\n,begin,\n,func,f0mtjA9,(,),\n,begin,\n,string,vXwfhKQ,<-,-,843,\n,end,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,186))
        except:
            print("fail testcase 86")
        
    def test_case_87(self):
        input = """func fLUGkon(p9M48kj) \n begin \nboolean vhCZc9l <--2608\n end
    """
        expect = "func,fLUGkon,(,p9M48kj,),\n,begin,\n,boolean,vhCZc9l,<-,-,2608,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,187))
        except:
            print("fail testcase 87")
        
    def test_case_88(self):
        input = """dynamic vcuFwTX <-2397
    """
        expect = "dynamic,vcuFwTX,<-,2397,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,188))
        except:
            print("fail testcase 88")
        
    def test_case_89(self):
        input = """string vdggyb2 <-2304
    """
        expect = "string,vdggyb2,<-,2304,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,189))
        except:
            print("fail testcase 89")
        
    def test_case_90(self):
        input = """vBeCN6v <--1325
    """
        expect = "vBeCN6v,<-,-,1325,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,190))
        except:
            print("fail testcase 90")
        
    def test_case_91(self):
        input = """var v6cdMqk <--253
    """
        expect = "var,v6cdMqk,<-,-,253,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,191))
        except:
            print("fail testcase 91")
        
    def test_case_92(self):
        input = """func fYPzIzp(pS1mCZV,pwbFyZg,pXfOK5w,pfnHxd0) \n begin \nboolean vFaU4f9 <--1119\n end
    """
        expect = "func,fYPzIzp,(,pS1mCZV,,,pwbFyZg,,,pXfOK5w,,,pfnHxd0,),\n,begin,\n,boolean,vFaU4f9,<-,-,1119,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,192))
        except:
            print("fail testcase 92")
        
    def test_case_93(self):
        input = """boolean v7aVZbs <--466
    """
        expect = "boolean,v7aVZbs,<-,-,466,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,193))
        except:
            print("fail testcase 93")
        
    def test_case_94(self):
        input = """func fDCWjib(pTfIR1A,pWkqA5X) \n begin \nnumber vamxGMk <--1330\n end
    """
        expect = "func,fDCWjib,(,pTfIR1A,,,pWkqA5X,),\n,begin,\n,number,vamxGMk,<-,-,1330,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,194))
        except:
            print("fail testcase 94")
        
    def test_case_95(self):
        input = """var vIg2AqE <--1539
    """
        expect = "var,vIg2AqE,<-,-,1539,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,195))
        except:
            print("fail testcase 95")
        
    def test_case_96(self):
        input = """func fAS0rAC() \n begin \nfunc fJTcsXY(pInIgjb,puYAbPb,pjefwIz,pAzhGuc) \n begin \nstring vimAWP6 <--1847\n end\n end
    """
        expect = "func,fAS0rAC,(,),\n,begin,\n,func,fJTcsXY,(,pInIgjb,,,puYAbPb,,,pjefwIz,,,pAzhGuc,),\n,begin,\n,string,vimAWP6,<-,-,1847,\n,end,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,196))
        except:
            print("fail testcase 96")
        
    def test_case_97(self):
        input = """boolean vxhkSRj <--1456
    """
        expect = "boolean,vxhkSRj,<-,-,1456,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,197))
        except:
            print("fail testcase 97")
        
    def test_case_98(self):
        input = """func fXAOSe0(pRgip5m,pqScMKw,pQXTPo6,pJ5RwRn) \n begin \nstring v8FwZSI <--158\n end
    """
        expect = "func,fXAOSe0,(,pRgip5m,,,pqScMKw,,,pQXTPo6,,,pJ5RwRn,),\n,begin,\n,string,v8FwZSI,<-,-,158,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,198))
        except:
            print("fail testcase 98")
        
    def test_case_99(self):
        input = """vdeSGye <-31
    """
        expect = "vdeSGye,<-,31,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,199))
        except:
            print("fail testcase 99")
        