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

        # #Complex test
        self.assertTrue(TestLexer.test(" \"This \\nString \\nHas \\nFour lines\" \n","This \\nString \\nHas \\nFour lines,\n,<EOF>",613))
        self.assertTrue(TestLexer.test("String a = \"this is a string 123\"\n","String,a,=,this is a string 123,\n,<EOF>",614))
        self.assertTrue(TestLexer.test("String a = \"this is a string 123\n","String,a,=,Unclosed String: this is a string 123",615))
        self.assertTrue(TestLexer.test("String a = \"this is a string 123\\n","String,a,=,Unclosed String: this is a string 123\\n",616))

        #Illegal escape
        # self.assertTrue(TestLexer.test(""" "Tien \\1"  """, "Illegal Escape In String: Tien \\1", 617))
        # self.assertTrue(TestLexer.test(""" "Tien \\2 \\n \n """, "Illegal Escape In String: Tien \\2", 618))
        # self.assertTrue(TestLexer.test(""" "Tien \\e \\n \\r """, "Illegal Escape In String: Tien \\e", 619))        
        # self.assertTrue(TestLexer.test(""" "Tien \\321 \\n \\r """, "Illegal Escape In String: Tien \\3", 620))
        # self.assertTrue(TestLexer.test(""" "Tien \\"1 " """, "Illegal Escape In String: Tien \\\"", 621))          
        # self.assertTrue(TestLexer.test(""" "Tien ' " " """, "Illegal Escape In String: Tien ' ", 622))
        # self.assertTrue(TestLexer.test(""" "Tien \\' ""1 """, "Tien \\' ,Unclosed String: 1 ", 623))  
        


    def test_all(self):
        """test anything"""
        # self.assertTrue(TestLexer.test(""" "" """,",<EOF>",1001)) # chuỗi rỗng
        # self.assertTrue(TestLexer.test(""" "Vo """, "Unclosed String: Vo ", 1001))

