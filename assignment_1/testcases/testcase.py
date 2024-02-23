import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase): 

    def test_case_0(self):
        input = """ or % / else	break	by	+	< !=	until	and
end begin	func
+ +	>
-
== elif <- <= (	break ( [	<-	for begin elif	and	"abcd"
by	end / "abcd" string	,	104 elif = and != false	not	else [ else
... /	if < until by for return until	<=
else <=	[ != >=	- < 36
return >= begin	"abcd" =
<	func	begin
break
    """
        expect = "or,%,/,else,break,by,+,<,!=,until,and,\n,end,begin,func,\n,+,+,>,\n,-,\n,==,elif,<-,<=,(,break,(,[,<-,for,begin,elif,and,abcd,\n,by,end,/,abcd,string,,,104,elif,=,and,!=,false,not,else,[,else,\n,...,/,if,<,until,by,for,return,until,<=,\n,else,<=,[,!=,>=,-,<,36,\n,return,>=,begin,abcd,=,\n,<,func,begin,\n,break,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,100))
        except:
            print("fail testcase 0")
        
    def test_case_1(self):
        input = """	

==	func
>= var
...	break	not 105 <-	=	]	string "abcd" ] until	<
begin ) "abcd" != continue


"abcd" number >=	break var bool end , < break end	- 33.53e324	!= not

	]
string (
bool [ number
==	(
begin
by	if -	if	>=
24.69	false +	/ not continue	and ]	]
<= end bool	<-	continue
(
bool else not ==
begin for
if true	=	func begin ...
( * or	for until elif	[
) for
    """
        expect = "\n,\n,==,func,\n,>=,var,\n,...,break,not,105,<-,=,],string,abcd,],until,<,\n,begin,),abcd,!=,continue,\n,\n,\n,abcd,number,>=,break,var,bool,end,,,<,break,end,-,33.53e324,!=,not,\n,\n,],\n,string,(,\n,bool,[,number,\n,==,(,\n,begin,\n,by,if,-,if,>=,\n,24.69,false,+,/,not,continue,and,],],\n,<=,end,bool,<-,continue,\n,(,\n,bool,else,not,==,\n,begin,for,\n,if,true,=,func,begin,...,\n,(,*,or,for,until,elif,[,\n,),for,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,101))
        except:
            print("fail testcase 1")
        
    def test_case_2(self):
        input = """
=	begin + dynamic 
 -	*
return	/ - break
= 14 return else return 
 <-
or *	+	elif	string >	bool	continue	77E5776 a1 or
<- == or continue	true /	continue	continue func
string	break "abcd"
>=	==
until	-	/ bool	begin
<- ( 
 ) ==	by
and and	!=	if false
a1 >=	<=	(
%	not dynamic
* until	continue
for return	return	] <-	end	func <=	var or	> if	dynamic
break	begin dynamic	continue	127e-6561	begin
    """
        expect = "\n,=,begin,+,dynamic,\n,-,*,\n,return,/,-,break,\n,=,14,return,else,return,\n,<-,\n,or,*,+,elif,string,>,bool,continue,77E5776,a1,or,\n,<-,==,or,continue,true,/,continue,continue,func,\n,string,break,abcd,\n,>=,==,\n,until,-,/,bool,begin,\n,<-,(,\n,),==,by,\n,and,and,!=,if,false,\n,a1,>=,<=,(,\n,%,not,dynamic,\n,*,until,continue,\n,for,return,return,],<-,end,func,<=,var,or,>,if,dynamic,\n,break,begin,dynamic,continue,127e-6561,begin,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,102))
        except:
            print("fail testcase 2")
        
    def test_case_3(self):
        input = """ , by	,
/	until	false ]
-	= and =	return dynamic	continue	or	>	<- <= a1	by ) % ) break a1	/ ,	>= string true	] by [	/	return + for +	break a1	( >
>
)	+	
	, number until 118e-3025 bool 

=	>= func end bool *
==	true
end end	<= number -	>=	
	)	
 %	
	not + true
, <= not bool	>
until % +
    """
        expect = ",,by,,,\n,/,until,false,],\n,-,=,and,=,return,dynamic,continue,or,>,<-,<=,a1,by,),%,),break,a1,/,,,>=,string,true,],by,[,/,return,+,for,+,break,a1,(,>,\n,>,\n,),+,\n,,,number,until,118e-3025,bool,\n,\n,=,>=,func,end,bool,*,\n,==,true,\n,end,end,<=,number,-,>=,\n,),\n,%,\n,not,+,true,\n,,,<=,not,bool,>,\n,until,%,+,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,103))
        except:
            print("fail testcase 3")
        
    def test_case_4(self):
        input = """
elif not	true break	false !=	by	) 21.75	not	if	, <- ,	a1 == ,	>	/ /
by true begin < <=	(	or until	,	var	else -
, "abcd" string
(	by	continue elif until elif ==	<= not	

not	break	if
if begin
% true [	a1	88E-400 func begin bool	
	== true	* -
    """
        expect = "\n,elif,not,true,break,false,!=,by,),21.75,not,if,,,<-,,,a1,==,,,>,/,/,\n,by,true,begin,<,<=,(,or,until,,,var,else,-,\n,,,abcd,string,\n,(,by,continue,elif,until,elif,==,<=,not,\n,\n,not,break,if,\n,if,begin,\n,%,true,[,a1,88E-400,func,begin,bool,\n,==,true,*,-,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,104))
        except:
            print("fail testcase 4")
        
    def test_case_5(self):
        input = """	<=	/ -
bool	until

 by a1 bool	"abcd" elif , *
var or
if * ==	for until
not	!=
    """
        expect = "<=,/,-,\n,bool,until,\n,\n,by,a1,bool,abcd,elif,,,*,\n,var,or,\n,if,*,==,for,until,\n,not,!=,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,105))
        except:
            print("fail testcase 5")
        
    def test_case_6(self):
        input = """ or bool
string	>
<= var ...
number	/ string +	begin	begin	return	/	else	... by
break	until	[ [ ] / string
for true == for != =
break
or
end ...
by return ... func or continue
if end until
if else ==	<=
... 
	)	<- <=	"abcd" and
"abcd"	a1
]	- return [	else break
    """
        expect = "or,bool,\n,string,>,\n,<=,var,...,\n,number,/,string,+,begin,begin,return,/,else,...,by,\n,break,until,[,[,],/,string,\n,for,true,==,for,!=,=,\n,break,\n,or,\n,end,...,\n,by,return,...,func,or,continue,\n,if,end,until,\n,if,else,==,<=,\n,...,\n,),<-,<=,abcd,and,\n,abcd,a1,\n,],-,return,[,else,break,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,106))
        except:
            print("fail testcase 6")
        
    def test_case_7(self):
        input = """	)	until return 140.52E-900 =
number	,
a1 and	86e-9025
- for (	) < dynamic / "abcd" 
	"abcd"	!= continue < != string break return var ]	bool *
else break	if	% % var
    """
        expect = "),until,return,140.52E-900,=,\n,number,,,\n,a1,and,86e-9025,\n,-,for,(,),<,dynamic,/,abcd,\n,abcd,!=,continue,<,!=,string,break,return,var,],bool,*,\n,else,break,if,%,%,var,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,107))
        except:
            print("fail testcase 7")
        
    def test_case_8(self):
        input = """ func	true	continue	or	or elif	<=
-
dynamic
==	elif	<=	<- end	<- dynamic bool	+ or a1 true break until
*	% ==
dynamic	*	not or	var 14e-3844	a1 begin elif = ]
bool for "abcd"	until	number end	(
elif
    """
        expect = "func,true,continue,or,or,elif,<=,\n,-,\n,dynamic,\n,==,elif,<=,<-,end,<-,dynamic,bool,+,or,a1,true,break,until,\n,*,%,==,\n,dynamic,*,not,or,var,14e-3844,a1,begin,elif,=,],\n,bool,for,abcd,until,number,end,(,\n,elif,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,108))
        except:
            print("fail testcase 8")
        
    def test_case_9(self):
        input = """	>= )	-	] elif until else	<= string
%	dynamic	string + false	a1
,
% continue begin != else
+ ] < func else
[	if for	17E-1764 func dynamic	"abcd" number
until , ) != break
if
var	> [	func	string 61e625
    """
        expect = ">=,),-,],elif,until,else,<=,string,\n,%,dynamic,string,+,false,a1,\n,,,\n,%,continue,begin,!=,else,\n,+,],<,func,else,\n,[,if,for,17E-1764,func,dynamic,abcd,number,\n,until,,,),!=,break,\n,if,\n,var,>,[,func,string,61e625,\n,<EOF>"
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
        input = """string a<-"k0ZZ'\"s a
    """
        expect = "string,a,<-,Unclosed String: k0ZZ'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,120))
        except:
            print("fail testcase 20")
        
    def test_case_21(self):
        input = """string a<-"q0Fk'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: q0Fk'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,121))
        except:
            print("fail testcase 21")
        
    def test_case_22(self):
        input = """string a<-"g55p'\"s\"
    """
        expect = "string,a,<-,g55p'\"s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,122))
        except:
            print("fail testcase 22")
        
    def test_case_23(self):
        input = """string a<-"Z7M8'\"s a
    """
        expect = "string,a,<-,Unclosed String: Z7M8'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,123))
        except:
            print("fail testcase 23")
        
    def test_case_24(self):
        input = """string a<-"ZWGi'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: ZWGi'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,124))
        except:
            print("fail testcase 24")
        
    def test_case_25(self):
        input = """string a<-"wCbw'\"s a
    """
        expect = "string,a,<-,Unclosed String: wCbw'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,125))
        except:
            print("fail testcase 25")
        
    def test_case_26(self):
        input = """string a<-"I84x\"s a
    """
        expect = "string,a,<-,I84x,s,a,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,126))
        except:
            print("fail testcase 26")
        
    def test_case_27(self):
        input = """string a<-"RcMC'\"s\"
    """
        expect = "string,a,<-,RcMC'\"s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,127))
        except:
            print("fail testcase 27")
        
    def test_case_28(self):
        input = """string a<-"UjdZ'\"s a
    """
        expect = "string,a,<-,Unclosed String: UjdZ'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,128))
        except:
            print("fail testcase 28")
        
    def test_case_29(self):
        input = """string a<-"RL9u'\"s a
    """
        expect = "string,a,<-,Unclosed String: RL9u'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,129))
        except:
            print("fail testcase 29")
        
    def test_case_30(self):
        input = """ if by dynamic if }
    """
        expect = "if,by,dynamic,if,Error Token }"
        try:
            self.assertTrue(TestLexer.test(input,expect,130))
        except:
            print("fail testcase 30")
        
    def test_case_31(self):
        input = """ ( == / true )
 if |
    """
        expect = "(,==,/,true,),\n,if,Error Token |"
        try:
            self.assertTrue(TestLexer.test(input,expect,131))
        except:
            print("fail testcase 31")
        
    def test_case_32(self):
        input = """ % string / , , + ... > break {
    """
        expect = "%,string,/,,,,,+,...,>,break,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,132))
        except:
            print("fail testcase 32")
        
    def test_case_33(self):
        input = """ func false bool func dynamic for < func '
    """
        expect = "func,false,bool,func,dynamic,for,<,func,Error Token '"
        try:
            self.assertTrue(TestLexer.test(input,expect,133))
        except:
            print("fail testcase 33")
        
    def test_case_34(self):
        input = """ and for until dynamic ;
    """
        expect = "and,for,until,dynamic,Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,134))
        except:
            print("fail testcase 34")
        
    def test_case_35(self):
        input = """ until {
    """
        expect = "until,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,135))
        except:
            print("fail testcase 35")
        
    def test_case_36(self):
        input = """ ~
    """
        expect = "Error Token ~"
        try:
            self.assertTrue(TestLexer.test(input,expect,136))
        except:
            print("fail testcase 36")
        
    def test_case_37(self):
        input = """ false ( false var for - $
    """
        expect = "false,(,false,var,for,-,Error Token $"
        try:
            self.assertTrue(TestLexer.test(input,expect,137))
        except:
            print("fail testcase 37")
        
    def test_case_38(self):
        input = """ or or true % else [ == var }
    """
        expect = "or,or,true,%,else,[,==,var,Error Token }"
        try:
            self.assertTrue(TestLexer.test(input,expect,138))
        except:
            print("fail testcase 38")
        
    def test_case_39(self):
        input = """ ) {
    """
        expect = "),Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,139))
        except:
            print("fail testcase 39")
        
    def test_case_40(self):
        input = """
 |
    """
        expect = "\n,Error Token |"
        try:
            self.assertTrue(TestLexer.test(input,expect,140))
        except:
            print("fail testcase 40")
        
    def test_case_41(self):
        input = """ @
    """
        expect = "Error Token @"
        try:
            self.assertTrue(TestLexer.test(input,expect,141))
        except:
            print("fail testcase 41")
        
    def test_case_42(self):
        input = """ ] not * continue string < var * by '
    """
        expect = "],not,*,continue,string,<,var,*,by,Error Token '"
        try:
            self.assertTrue(TestLexer.test(input,expect,142))
        except:
            print("fail testcase 42")
        
    def test_case_43(self):
        input = """ by ) ] - - !
    """
        expect = "by,),],-,-,Error Token !"
        try:
            self.assertTrue(TestLexer.test(input,expect,143))
        except:
            print("fail testcase 43")
        
    def test_case_44(self):
        input = """ < elif * ... <- {
    """
        expect = "<,elif,*,...,<-,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,144))
        except:
            print("fail testcase 44")
        
    def test_case_45(self):
        input = """ number not == string STRINGLIT or $
    """
        expect = "number,not,==,string,STRINGLIT,or,Error Token $"
        try:
            self.assertTrue(TestLexer.test(input,expect,145))
        except:
            print("fail testcase 45")
        
    def test_case_46(self):
        input = """
 string by
 STRINGLIT ~
    """
        expect = "\n,string,by,\n,STRINGLIT,Error Token ~"
        try:
            self.assertTrue(TestLexer.test(input,expect,146))
        except:
            print("fail testcase 46")
        
    def test_case_47(self):
        input = """ / >= ] return break not !
    """
        expect = "/,>=,],return,break,not,Error Token !"
        try:
            self.assertTrue(TestLexer.test(input,expect,147))
        except:
            print("fail testcase 47")
        
    def test_case_48(self):
        input = """ ( + - else $
    """
        expect = "(,+,-,else,Error Token $"
        try:
            self.assertTrue(TestLexer.test(input,expect,148))
        except:
            print("fail testcase 48")
        
    def test_case_49(self):
        input = """ NUMLIT % % for return , &
    """
        expect = "NUMLIT,%,%,for,return,,,Error Token &"
        try:
            self.assertTrue(TestLexer.test(input,expect,149))
        except:
            print("fail testcase 49")
        
    def test_case_50(self):
        input = """string s <- " pfaHa6A \\c "
    """
        expect = "string,s,<-,Illegal Escape In String:  pfaHa6A \\c"
        try:
            self.assertTrue(TestLexer.test(input,expect,150))
        except:
            print("fail testcase 50")
        
    def test_case_51(self):
        input = """string s <- " Sp \\  "
    """
        expect = "string,s,<-,Illegal Escape In String:  Sp \\ "
        try:
            self.assertTrue(TestLexer.test(input,expect,151))
        except:
            print("fail testcase 51")
        
    def test_case_52(self):
        input = """string s <- " n5dejFXJ \\A "
    """
        expect = "string,s,<-,Illegal Escape In String:  n5dejFXJ \\A"
        try:
            self.assertTrue(TestLexer.test(input,expect,152))
        except:
            print("fail testcase 52")
        
    def test_case_53(self):
        input = """string s <- " bY6pC \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  bY6pC \\("
        try:
            self.assertTrue(TestLexer.test(input,expect,153))
        except:
            print("fail testcase 53")
        
    def test_case_54(self):
        input = """string s <- " Qv2yi \\A "
    """
        expect = "string,s,<-,Illegal Escape In String:  Qv2yi \\A"
        try:
            self.assertTrue(TestLexer.test(input,expect,154))
        except:
            print("fail testcase 54")
        
    def test_case_55(self):
        input = """string s <- " 9b8m \\c "
    """
        expect = "string,s,<-,Illegal Escape In String:  9b8m \\c"
        try:
            self.assertTrue(TestLexer.test(input,expect,155))
        except:
            print("fail testcase 55")
        
    def test_case_56(self):
        input = """string s <- "  \\~ "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\~"
        try:
            self.assertTrue(TestLexer.test(input,expect,156))
        except:
            print("fail testcase 56")
        
    def test_case_57(self):
        input = """string s <- " PqYGo \\z "
    """
        expect = "string,s,<-,Illegal Escape In String:  PqYGo \\z"
        try:
            self.assertTrue(TestLexer.test(input,expect,157))
        except:
            print("fail testcase 57")
        
    def test_case_58(self):
        input = """string s <- " prDy \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  prDy \\("
        try:
            self.assertTrue(TestLexer.test(input,expect,158))
        except:
            print("fail testcase 58")
        
    def test_case_59(self):
        input = """string s <- " w \\\" "
    """
        expect = "string,s,<-,Illegal Escape In String:  w \\\""
        try:
            self.assertTrue(TestLexer.test(input,expect,159))
        except:
            print("fail testcase 59")
        
    def test_case_60(self):
        input = """string s <- " 4tSQ8 \\# "
    """
        expect = "string,s,<-,Illegal Escape In String:  4tSQ8 \\#"
        try:
            self.assertTrue(TestLexer.test(input,expect,160))
        except:
            print("fail testcase 60")
        
    def test_case_61(self):
        input = """string s <- "  \\- "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\-"
        try:
            self.assertTrue(TestLexer.test(input,expect,161))
        except:
            print("fail testcase 61")
        
    def test_case_62(self):
        input = """string s <- " EV4j \\A "
    """
        expect = "string,s,<-,Illegal Escape In String:  EV4j \\A"
        try:
            self.assertTrue(TestLexer.test(input,expect,162))
        except:
            print("fail testcase 62")
        
    def test_case_63(self):
        input = """string s <- " t1rbSu6Nd \\9 "
    """
        expect = "string,s,<-,Illegal Escape In String:  t1rbSu6Nd \\9"
        try:
            self.assertTrue(TestLexer.test(input,expect,163))
        except:
            print("fail testcase 63")
        
    def test_case_64(self):
        input = """string s <- " hVSqKvSF \\( "
    """
        expect = "string,s,<-,Illegal Escape In String:  hVSqKvSF \\("
        try:
            self.assertTrue(TestLexer.test(input,expect,164))
        except:
            print("fail testcase 64")
        
    def test_case_65(self):
        input = """string s <- " JUwKZ \\| "
    """
        expect = "string,s,<-,Illegal Escape In String:  JUwKZ \\|"
        try:
            self.assertTrue(TestLexer.test(input,expect,165))
        except:
            print("fail testcase 65")
        
    def test_case_66(self):
        input = """string s <- " 8 \\z "
    """
        expect = "string,s,<-,Illegal Escape In String:  8 \\z"
        try:
            self.assertTrue(TestLexer.test(input,expect,166))
        except:
            print("fail testcase 66")
        
    def test_case_67(self):
        input = """string s <- " THZ6RJ \\a "
    """
        expect = "string,s,<-,Illegal Escape In String:  THZ6RJ \\a"
        try:
            self.assertTrue(TestLexer.test(input,expect,167))
        except:
            print("fail testcase 67")
        
    def test_case_68(self):
        input = """string s <- " IqO6TFT4 \\| "
    """
        expect = "string,s,<-,Illegal Escape In String:  IqO6TFT4 \\|"
        try:
            self.assertTrue(TestLexer.test(input,expect,168))
        except:
            print("fail testcase 68")
        
    def test_case_69(self):
        input = """string s <- " t \\\" "
    """
        expect = "string,s,<-,Illegal Escape In String:  t \\\""
        try:
            self.assertTrue(TestLexer.test(input,expect,169))
        except:
            print("fail testcase 69")
        
    def test_case_70(self):
        input = """numberC0
    """
        expect = "numberC0,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,170))
        except:
            print("fail testcase 70")
        
    def test_case_71(self):
        input = """continue0i
    """
        expect = "continue0i,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,171))
        except:
            print("fail testcase 71")
        
    def test_case_72(self):
        input = """andTr
    """
        expect = "andTr,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,172))
        except:
            print("fail testcase 72")
        
    def test_case_73(self):
        input = """falseRX
    """
        expect = "falseRX,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,173))
        except:
            print("fail testcase 73")
        
    def test_case_74(self):
        input = """untill2
    """
        expect = "untill2,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,174))
        except:
            print("fail testcase 74")
        
    def test_case_75(self):
        input = """until6W
    """
        expect = "until6W,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,175))
        except:
            print("fail testcase 75")
        
    def test_case_76(self):
        input = """boolzo
    """
        expect = "boolzo,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,176))
        except:
            print("fail testcase 76")
        
    def test_case_77(self):
        input = """falsePY
    """
        expect = "falsePY,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,177))
        except:
            print("fail testcase 77")
        
    def test_case_78(self):
        input = """breakMm
    """
        expect = "breakMm,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,178))
        except:
            print("fail testcase 78")
        
    def test_case_79(self):
        input = """falsecc
    """
        expect = "falsecc,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,179))
        except:
            print("fail testcase 79")
        
    def test_case_80(self):
        input = """func fvqncn5(ptUUivo,pt9ChWy) \n begin \nvaU7DLz <--855\n end
    """
        expect = "func,fvqncn5,(,ptUUivo,,,pt9ChWy,),\n,begin,\n,vaU7DLz,<-,-,855,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,180))
        except:
            print("fail testcase 80")
        
    def test_case_81(self):
        input = """dynamic veW6opk <--2684
    """
        expect = "dynamic,veW6opk,<-,-,2684,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,181))
        except:
            print("fail testcase 81")
        
    def test_case_82(self):
        input = """var vu7gJDP <--2198
    """
        expect = "var,vu7gJDP,<-,-,2198,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,182))
        except:
            print("fail testcase 82")
        
    def test_case_83(self):
        input = """boolean vcyRO8h <--602
    """
        expect = "boolean,vcyRO8h,<-,-,602,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,183))
        except:
            print("fail testcase 83")
        
    def test_case_84(self):
        input = """func fBCSTGA() \n begin \nvruhQfr <--1594\n end
    """
        expect = "func,fBCSTGA,(,),\n,begin,\n,vruhQfr,<-,-,1594,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,184))
        except:
            print("fail testcase 84")
        
    def test_case_85(self):
        input = """vKnuTA5 <-1692
    """
        expect = "vKnuTA5,<-,1692,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,185))
        except:
            print("fail testcase 85")
        
    def test_case_86(self):
        input = """func fyaWVXf(pASAqXI,pddN5GE,pBkmU5b,pUmCUbw) \n begin \nboolean v9gbiqR <-1567\n end
    """
        expect = "func,fyaWVXf,(,pASAqXI,,,pddN5GE,,,pBkmU5b,,,pUmCUbw,),\n,begin,\n,boolean,v9gbiqR,<-,1567,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,186))
        except:
            print("fail testcase 86")
        
    def test_case_87(self):
        input = """func fbGxRrI(pY3P53C,pTBwimE,p5wpsJ9,pIOdPI7) \n begin \nfunc f966j3M(pYGGpUM) \n begin \nnumber veAcmxu <--1305\n end\n end
    """
        expect = "func,fbGxRrI,(,pY3P53C,,,pTBwimE,,,p5wpsJ9,,,pIOdPI7,),\n,begin,\n,func,f966j3M,(,pYGGpUM,),\n,begin,\n,number,veAcmxu,<-,-,1305,\n,end,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,187))
        except:
            print("fail testcase 87")
        
    def test_case_88(self):
        input = """var vEUOiSM <-1954
    """
        expect = "var,vEUOiSM,<-,1954,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,188))
        except:
            print("fail testcase 88")
        
    def test_case_89(self):
        input = """func f5sDsfe(pcJahdt,pYxCvWJ,p57SP6i) \n begin \nvar vMs8lZD <-1400\n end
    """
        expect = "func,f5sDsfe,(,pcJahdt,,,pYxCvWJ,,,p57SP6i,),\n,begin,\n,var,vMs8lZD,<-,1400,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,189))
        except:
            print("fail testcase 89")
        
    def test_case_90(self):
        input = """dynamic v0R1Fkf <--2682
    """
        expect = "dynamic,v0R1Fkf,<-,-,2682,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,190))
        except:
            print("fail testcase 90")
        
    def test_case_91(self):
        input = """vRRAldr <-892
    """
        expect = "vRRAldr,<-,892,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,191))
        except:
            print("fail testcase 91")
        
    def test_case_92(self):
        input = """dynamic vS3cy5G <--955
    """
        expect = "dynamic,vS3cy5G,<-,-,955,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,192))
        except:
            print("fail testcase 92")
        
    def test_case_93(self):
        input = """vCEm26B <--2185
    """
        expect = "vCEm26B,<-,-,2185,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,193))
        except:
            print("fail testcase 93")
        
    def test_case_94(self):
        input = """string vX1tzDl <-2639
    """
        expect = "string,vX1tzDl,<-,2639,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,194))
        except:
            print("fail testcase 94")
        
    def test_case_95(self):
        input = """number vrL1Gnl <--422
    """
        expect = "number,vrL1Gnl,<-,-,422,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,195))
        except:
            print("fail testcase 95")
        
    def test_case_96(self):
        input = """func f34EcjP(pr8awFc,plW6yde,pVcaEGI) \n begin \nboolean vkalqR0 <-1266\n end
    """
        expect = "func,f34EcjP,(,pr8awFc,,,plW6yde,,,pVcaEGI,),\n,begin,\n,boolean,vkalqR0,<-,1266,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,196))
        except:
            print("fail testcase 96")
        
    def test_case_97(self):
        input = """func fZqIQfa(pHpoVVB,pHtEA1E,pEBXR5t) \n begin \nvVsy9Pd <--305\n end
    """
        expect = "func,fZqIQfa,(,pHpoVVB,,,pHtEA1E,,,pEBXR5t,),\n,begin,\n,vVsy9Pd,<-,-,305,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,197))
        except:
            print("fail testcase 97")
        
    def test_case_98(self):
        input = """vuUubbN <--2292
    """
        expect = "vuUubbN,<-,-,2292,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,198))
        except:
            print("fail testcase 98")
        
    def test_case_99(self):
        input = """func fZLeUdZ(ptrxFis,pj5FrHz) \n begin \nfunc f00OuIX(pA5rlvz,p9NPDXK,pnUWwcQ) \n begin \nfunc fs1jLiX(pTsNij3,pmJ1zAf) \n begin \nfunc fDjZ5Vv(ppESuLq,pWRHLi6,pzj9Fj1) \n begin \nvSSETUv <--2462\n end\n end\n end\n end
    """
        expect = "func,fZLeUdZ,(,ptrxFis,,,pj5FrHz,),\n,begin,\n,func,f00OuIX,(,pA5rlvz,,,p9NPDXK,,,pnUWwcQ,),\n,begin,\n,func,fs1jLiX,(,pTsNij3,,,pmJ1zAf,),\n,begin,\n,func,fDjZ5Vv,(,ppESuLq,,,pWRHLi6,,,pzj9Fj1,),\n,begin,\n,vSSETUv,<-,-,2462,\n,end,\n,end,\n,end,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,199))
        except:
            print("fail testcase 99")
        