import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_a(self):
    #     """test"""
    #     input = """
    #     func main()
    #         a <- 1
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 200)) 

    # def test_declared(self): # test case 201 -> 220
    #     """declared"""    
        

        

    #     input = """ 
    #         func main(number a) break ##12
    #     """
    #     expect = "Error on line 2 col 38: ##12"
    #     self.assertTrue(TestParser.test(input, expect, 211))    

    #     input = """ 
    #         func main(number a) ##12
    #             break
    #     """
    #     expect = "Error on line 2 col 32: ##12"
    #     self.assertTrue(TestParser.test(input, expect, 212))    
        
    #     input = """ 
    #         ##12
    #         func main(number a) 
    #             ##12
                
    #             break
    #             ##12
    #             ##12
    #         func main(number a)
    #         ##12        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 213))                  

    #     input = """ 
    #         ## 12
            
    #         var a <- 1 ## 12
    #         ## 12
    #     """
    #     expect = "Error on line 4 col 23: ## 12"
    #     self.assertTrue(TestParser.test(input, expect, 214))   
        
    #     input = """var a <- 1"""
    #     expect = "Error on line 1 col 10: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 215))  

    #     input = """func main(number a) """
    #     expect = "Error on line 1 col 20: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 216))  
             
             
             
             
                            
       
        
        
    #     #! test for break Continue
    #     input = """
    #     func main()
    #         for i until i >= 10 by 1 + 1
    #             a <- 1
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 237))    
        
    #     input = """
    #     func main()
    #         for i[1] until i >= 10 by 1 + 1
    #             a <- 1
    #     """
    #     expect = "Error on line 3 col 17: ["
    #     self.assertTrue(TestParser.test(input, expect, 238))    

    #     input = """
    #     func main()
    #         for i+1 until i >= 10 by 1 + 1
    #             a <- 1
    #     """
    #     expect = "Error on line 3 col 17: +"
    #     self.assertTrue(TestParser.test(input, expect, 239)) 
        
    #     input = """
    #     func main()
    #     begin 
    #         break
    #         continue
    #         for i until i >= 10 by 1 + 1
    #             begin
    #                 break
    #                 continue
    #             end
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 240))  
        
    #     input = """
    #     func main()
    #         for i until i >= 10 by 1 + 1
    #     """
    #     expect = "Error on line 4 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 241))  
        
        
    #     #! return  call_statement
    #     input = """
    #     func main()
    #         return 1 + 1
    #     """    
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 242))

    #     input = """
    #     func main()
    #         main()
    #     """    
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 243))
        
    #     input = """
    #     func main()
    #     begin 
    #         return ([1,2,3]) + 1
    #         return main()
    #         main(1,2)
    #         fun()
    #         main([1,2,3], 1+2, a, c ... e)
    #     end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 244))  
        
    #     input = """
    #     func main()
    #         return func()
    #     """
    #     expect = "Error on line 3 col 19: func"
    #     self.assertTrue(TestParser.test(input, expect, 245))      
        
    #     input = """
    #     func main()
    #         return break
    #     """
    #     expect = "Error on line 3 col 19: break"
    #     self.assertTrue(TestParser.test(input, expect, 246)) 
        
    #     #! return  block
    #     input = """
    #     func main()
    #         begin
    #             begin
    #                 begin
    #                     x <- 1
    #                 end
                    
    #                 begin
    #                     return true
    #                 end
                    
    #                 return false
    #             end
                
    #             begin
    #             end
    #             return true
    #         end
    #     """    
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 247))
     
    # def test_NewLine(self): # test 250 -> ...
    #     """new line"""
    #     input = """
    #     func main() aPI <- 3.14
    #     """
    #     expect = "Error on line 2 col 20: aPI"
    #     self.assertTrue(TestParser.test(input, expect, 250))          

    
    # def test_Source_Code(self): # test 270 -> ...
    #     """Source_Code"""
    #     input = """
    #     func areDivisors(number num1, number num2)
    #         return (num1 % num2 = 0 ... num2 % num1 = 0)
    #     func main()
    #         begin
    #             var num1 <- readNumber()
    #             var num2 <- readNumber()
    #             if areDivisors(num1, num2) printString("Yes")
    #             else printString("No")
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 270))   
        
        
    #     input = """
    #         func isPrime(number x)
    #         func main()
    #             begin
    #                 number x <- readNumber()
    #                 if isPrime(x) printString("Yes")
    #                 else printString("No")
    #             end
    #         func isPrime(number x)
    #         begin
    #         if x <= 1 return false
    #         var i <- 2
    #         for i until i > x / 2 by 1
    #         begin
    #         if x % i = 0 return false
    #         end
    #         return true
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 271))  

        # input = """
        # func a() return 1
        # """
        # expect = "Error on line 2 col 17: return"
        # self.assertTrue(TestParser.test(input, expect, 272))   
        
        # input = """
        # number x <- x number x <- y
        # """
        # expect = "Error on line 2 col 22: number"
        # self.assertTrue(TestParser.test(input, expect, 272)) 
        
        # input = """
        # func a()
        # begin
        # end
        
        # func a()
        # begin

        #     number x <- x
            
        # end
        
        # func a()
        # begin end
        # """
        # expect = "Error on line 14 col 14: end"
        # self.assertTrue(TestParser.test(input, expect, 272))  
        

        # input = """    
        # func a()
        # begin
        #     break continue
        # end
        # """
        # expect = "Error on line 4 col 18: continue"
        # self.assertTrue(TestParser.test(input, expect, 272)) 
        
        # input = """    
        # func a()
        # begin
        #     return 1 break
        # end
        # """
        # expect = "Error on line 4 col 21: break"
        # self.assertTrue(TestParser.test(input, expect, 272))   
        
        # input = """    
        # func a()
        # begin
        #     if x <= 1 return false
        #     if x <= 1 
        #         return false
        # end
        # """
        # expect = "Error on line 4 col 21: break"
        # self.assertTrue(TestParser.test(input, expect, 272))  