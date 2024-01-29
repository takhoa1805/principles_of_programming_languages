import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):    
    def test_simple_program(self):
        """Free tests"""
        input = """
        number a
        number num <- expression
        bool num
        bool boo <- expression
        string str
        string str <- expression
        var a <- expression
        dynamic dyn 
        dynamic dyn <- expression
        number a[10]
        number a[5] <- arrayexpression
        number a[2,3]
        number a[2,3,4,5] <- arrayexpression
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2001))

    # def test_declared(self): # test case 201 -> 220
    #     """declared"""    
        
    #     #! biến
    #     input = """ 
    #         number VoTien
            
    #         ## VO Tien
    #         number VoTien <- 0
    #         bool a[122,15]
    #         bool a[122,15] <- 1
    #         string b[3]
    #         string b[3] <- 2
    #         var i <- 0
    #         dynamic i
    #         dynamic i <- 0
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 201))   
        
    #     input = """ 
    #         var VoTien
            
    #     """
    #     expect = "Error on line 2 col 23: \n"
    #     self.assertTrue(TestParser.test(input, expect, 202))   
        
    #     input = """ 
    #         dynamic VoTien[5] <- 3
    #     """
    #     expect = "Error on line 2 col 26: ["
    #     self.assertTrue(TestParser.test(input, expect, 203))         

    #     input = """ 
    #         bool a["string"]
    #         bool a[[1,2]]
    #         bool a[1+1]
    #     """
    #     expect = "Error on line 2 col 19: string"
    #     self.assertTrue(TestParser.test(input, expect, 204))   
        
    #     input = """ 
    #         bool a[1,]
    #     """
    #     expect = "Error on line 2 col 21: ]"
    #     self.assertTrue(TestParser.test(input, expect, 205)) 

    #     input = """ 
    #         var a[1]
    #     """
    #     expect = "Error on line 2 col 17: ["
    #     self.assertTrue(TestParser.test(input, expect, 206))  
        
         