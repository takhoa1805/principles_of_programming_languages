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
        number a <- [1,2,3,4]
        
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2001))

        input = """
        
        func main()

        func main(number board[5,5]) 
        begin
        var a <- 5
        a <- 5
        main(board[5][5])
        return main(board(a))
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2002))

        input = """
        func main()
        begin
            if(true) begin
                a <- b
                var a <- 5
                return true
                if(false) begin
                a <- b > 5
                return true
                end
            end 
        end

        func main()
        begin
            if(true) return true
            elif(false) return false
            elif(true) return
            elif(not true) begin
                var a <- 5
                return a
            end
            else return true
            
        end

         
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2003))

        input = """
        func main()
        begin
            var i <- 0
            for i until 1+1 by a begin
            i <- 1000
            if (true)  begin
                break
            end
            elif (false) continue
            else return

            end
            
        end

        func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2004))

        input = """func main() begin
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2005))

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
        expect = "Error on line 2 col 22: \n"
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

        #! hàm và declaration_statement
        input = """ 
            func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var VoTien <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 7 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 207))       
        
        input = """ 
            func main()
            ## VO Tien
            func main()
            ## VO Tien
            func main (bool a)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))  

        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 209))                 

        #! lỗi comment và newline
        input = """ 
            ##12
            ##12
            
            func main(number a) ##12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))   
                

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

    def test_Statements(self): # test 230 -> ...
        """Statements"""
        
        #! test assignment_statement
        input = """
        func main()
        begin
            aPI <- 3.14
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
        input = """
        func main()
            begin
                VoTien <- 1 + 2 + fun()
                VoTien[1+a] <- 1
                VoTien[2][3+4] <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231)) 
        
        input = """
        func main()
        begin
            aPI + 1 <- 3.14
        end
        """
        expect = "Error on line 4 col 20: <-"
        self.assertTrue(TestParser.test(input, expect, 232))
        
        input = """
        func main()
        begin
            aPI()<- 3.14
        end
        """
        expect = "Error on line 4 col 17: <-"
        self.assertTrue(TestParser.test(input, expect, 233))
        
        input = """
        func main()
            (aPI)[2]<- 3.14
        """
        expect = "Error on line 3 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 234))
                
        #! test if_statement 
        input = """
        func main()
            begin   
                if(1+1) api <- 1
                
                if(1+1) api <- 1
                else api <- 1
                
                if (1) api <- 1
                elif (1) api <- 1
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1)   api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))  
        
        input = """
        func main()
            begin   
                if api <- 1
            end
        """
        expect = "Error on line 4 col 19: api"
        self.assertTrue(TestParser.test(input, expect, 236))        

        #! test for break Continue
        input = """
        func main()
        begin
            for i until i >= 10 by 1 + 1
                a <- 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))    
        
        input = """
        func main()
        begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
        end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 238))    

        input = """
        func main()
        begin
            for i+1 until i >= 10 by 1 + 1
                a <- 1
        end
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 239)) 
        
        input = """
        func main()
        begin 
            break
            continue
            for i until i >= 10 by 1 + 1
                begin
                    break
                    continue
                end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))  
        
        input = """
        func main()
        begin
            for i until i >= 10 by 1 + 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))  
        
        
        #! return  call_statement
        input = """
        func main()
            return 1 + 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

        input = """
        func main()
        begin
            main()
        end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        
        input = """
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))  
        
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 245))      
        
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 246)) 
        
        #! return  block
        input = """
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
     
    def test_NewLine(self): # test 250 -> ...
        """new line"""
        input = """
        func main() aPI <- 3.14
        """
        expect = "Error on line 2 col 20: aPI"
        self.assertTrue(TestParser.test(input, expect, 250))          

    
    def test_Source_Code(self): # test 270 -> ...
        """Source_Code"""
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))   
        
        
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false
            end
            return true
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))  

        input = """
        func a() return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))   
        
        input = """
        number x <- x number x <- y
        """
        expect = "Error on line 2 col 22: number"
        self.assertTrue(TestParser.test(input, expect, 273)) 
        
        input = """
        func a()
        begin
        end
        
        func a()
        begin

            number x <- x
            
        end
        
        func a()
        begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))  
        

        input = """    
        func a()
        begin
            break continue
        end
        """
        expect = "Error on line 4 col 18: continue"
        self.assertTrue(TestParser.test(input, expect, 275)) 
        
        input = """    
        func a()
        begin
            return 1 break
        end
        """
        expect = "Error on line 4 col 21: break"
        self.assertTrue(TestParser.test(input, expect, 276))   
        
        input = """    
        func a()
        begin
            if (x <= 1) return false
            if (x <= 1) 
                return false
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))  