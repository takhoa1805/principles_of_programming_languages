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


        number a <- a[5]
        number a[5] <- a[b[2,4],3]

        dynamic a <- foo(bar[5])
        var a <- foo()

        var a <- (1)...2
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2001))

    def test_declared(self): # test case 201 -> 220
        """declared"""    
        
        #! biến
        input = """ 
            number VoTien
            
            ## VO Tien
            number VoTien <- 0 ##something
            bool a[122,15]
            bool a[122,15] <- 1
            string b[3]
            string b[3] <- 2
            var i <- 0
            dynamic i
            dynamic i <- 0

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))   
        
        input = """ 
            var VoTien
            
        """
        expect = "Error on line 2 col 23: \n"
        self.assertTrue(TestParser.test(input, expect, 202))   
        
        input = """ 
            dynamic VoTien[5] <- 3
        """
        expect = "Error on line 2 col 26: ["
        self.assertTrue(TestParser.test(input, expect, 203))         

        input = """ 
            bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 204))   
        
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 205)) 

        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 206))  
        

    def test_Expression(self):
        """Expression"""
        #! nối chuỗi không có tính kết hợp
        input = """ var VoTien <- "Vo" ... "Tien" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
        input = """ var VoTien <- "Vo" ... a ... "Tien" 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
        
        # #! so sánh không có tính kết hợp
        input = """ 
            var VoTien <- true > "true" 
            var VoTien <- true >= "true"
            var VoTien <- true = "true"
            var VoTien <- true == "true"
            var VoTien <- true < "true"
            var VoTien <- true <= "true"
            var VoTien <- true >= "true" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        
        input = """ var VoTien <- true > x >= z 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
        
        #! cộng trừ nhân chia và and/or ....
        input = """ 
            var VoTien <- true and "true" or 1 
            var VoTien <- 1 and 2 and 3 or 4 or 4
            var VoTien <- 1 + 2 - 2 + 3 and 3
            var VoTien <- 1 / 2 * 3 % 4
            var VoTien <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
        input = """var VoTien <- true >= "true" and 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216)) 
        
        #! toán tử not và sign   
        input = """ 
            var VoTien <- -1 * not 1
            var VoTien <- not not not----C
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217)) 
        
        input = """var VoTien <- - not 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218)) 
        
        #! toán tử array
        input = """ 
            var VoTien <- a[1] + 1
            var VoTien <- array[1,1+2][1][2,3]
            var VoTien <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var VoTien <- 1[1] + fun()[1,fun()] 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
        input = """var VoTien <- a[]
        """
        expect = "Error on line 1 col 16: ]"
        self.assertTrue(TestParser.test(input, expect, 220)) 
        
        #! hàm 
        input = """ 
            var VoTien <- a()
            var VoTien <- a(1,2)
            var VoTien <- a(x,array[2])[2]
            var VoTien <- a(z,k[2][3] ... 2)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))    
        
        input = """var VoTien <- a()()
        """
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 222))  
        
        #! tổng hợp

        input = """ 
            var VoTien <- a() + 1 / 2 *3 <= 3 ... "v" >= 2
            var VoTien <- a(1,2)[1,2,3 ... 2] + false + true
            var VoTien <- a(x,array[2])[2,3+2,true,false]
            var VoTien <- a(z,k[2][3] ... 2)[true]
            var VoTien <- (a ... 3) ... b and (a >= b) < b[1][2][3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))  

        input = """var VoTien <- a[1]()
        """
        expect = "Error on line 1 col 18: ("
        self.assertTrue(TestParser.test(input, expect, 224))  