import unittest
from TestUtils import TestChecker
from AST import *

# MODIFY THIS FILE FOR TESTCASES

class CheckerSuite(unittest.TestCase):
    def test_general(self):
        input = """

func main()
    begin
        number a[5] <- [1,2]
    end


"""
        expect =""
        self.assertTrue(TestChecker.test(input, expect, 400))


# # TEST UNDECLARATION

#     def test_undeclared_1(self):
#         input = """
# number a <- f(2)

# func f(number x)
# begin
# end

# func main()
#     begin

#     end

# """
#         expect="Undeclared Function: f"
#         self.assertTrue(TestChecker.test(input,expect,401))

#     def test_undeclared_2(self):
#         input = """
# func f(number j)
# begin
# end

# func main()
# begin
#     writeNumber(j)
# end
# """
#         expect ="Undeclared Identifier: j"
#         self.assertTrue(TestChecker.test(input,expect,402))

#     def test_undeclared_3(self):
#         input = """
# func f(number j)
# begin
# end

# func main()
# begin
#     dynamic x <- (x - 2) * (x + true)
# end

# """
#         expect ="Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input,expect,403))

#     def test_undeclared_4(self):
#         input = """
# func main()
# begin
#     number x <- f()
# end

# """
#         expect ="Undeclared Function: f"
#         self.assertTrue(TestChecker.test(input,expect,404))

#     def test_undeclared_5(self):
#         input = """
# number x <- 10
# func f(number x)
# begin
#     number x <- x + 20
#     writeNumber(x)
# end
# """
#         expect = "Redeclared Variable: x"
#         self.assertTrue(TestChecker.test(input, expect, 405))


#     def test_undeclared_6(self):
#         input = """
# func test(number x)
# begin
#     var y <- test
#     test(2018)
# end
# """
#         expect = "Undeclared Identifier: test"
#         self.assertTrue(TestChecker.test(input, expect, 406))

#     def test_undeclared_7(self):
#         input = """
# dynamic a
# func main()
# begin
#     number a[2, 3] <- [a, [10, 20, 30]]
#     a <- [1, 9, 6]
#     writeNumber(a[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 407))

#     def test_undeclared_8(self):
#         input = """
# func main()
# begin
#     number x <- (10 + x) * 2
# end
# """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 408))

#     def test_undeclared_9(self):
#         input = """

# func main()
# begin
#     number x <- 5
#     dynamic x <- (x - 2) * (x + true)
# end

# """
#         expect ="Redeclared Variable: x"
#         self.assertTrue(TestChecker.test(input,expect,409))

#     def test_undeclared_10(self):
#         input = """
# func main()
# begin
#     number x <- 54 + f(a,b)
# end
# """
#         expect = "Undeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 410))

#     def test_undeclared_11(self):
#         input = """
# func f(number a)
# begin 
# end
# func main()
# begin
#     f(a)
# end
# """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 411))

#     def test_undeclared_11(self):
#         input = """
# func f(number a)
# begin 
# end
# func main()
# begin
#     number x <- f(a)
# end
# """
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 412))



#     # TEST REDECLARATION
#     def test_redeclared_1(self):
#         input ="""
# number a <- 2
# number b <- 5
# number c

# func main(number a, string b)
# begin   
#     string c
#     number c
# end
# """
#         expect = "Redeclared Variable: c"
#         self.assertTrue(TestChecker.test(input, expect, 421))

#     def test_redeclared_2(self):
#         input ="""
# number a <- 2
# number b <- 5

# func main(number c, string c)
# begin   
#     string c
# end
# """
#         expect = "Redeclared Parameter: c"
#         self.assertTrue(TestChecker.test(input, expect, 422))


#     def test_redeclared_3(self):
#         input = """
# func add(number x, number x)
# begin
# end

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(add(x, y))
# end

# func add(number a, number b)
# begin
#     return a + b
# end
# """
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input, expect, 423))

#     def test_redeclared_4(self):
#         input = """
# func add(number a, number b)
# begin
# end

# func add (number a)
# begin
# end

# func main()
# begin
#     number x <- readNumber()
#     number y <- readNumber()
#     writeNumber(add(x, y))
# end
# """
#         expect = "Redeclared Function: add"
#         self.assertTrue(TestChecker.test(input, expect, 424))

#     def test_redeclared_5(self):
#         input = """
# func f(number x)
# begin
# end


# func main()
# begin
# end

# func f(string x)
# begin
#     return x
# end
# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 425))

#     def test_redeclared_6(self):
#         input = """
# func f(number x)
# begin
# end

# number f

# func main()
# begin
# end

# """
#         expect = "Redeclared Variable: f"
#         self.assertTrue(TestChecker.test(input, expect, 426))

#     def test_redeclared_7(self):
#         input = """
# number f

# func f(number x)
# begin
# end

# func main()
# begin
# end

# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 427))

#     def test_redeclared_8(self):
#         input = """
# func f(number arr[10], number x)
# begin
# end

# func main()
# begin
#     dynamic n
#     var i <- 0
#     number arr[10]
#     for i until true by 1
#     begin
#         n <- readNumber()
#         if ((n > 10) or (n <= 0)) writeString("Try again")
#         else break
#     end
    
#     for i until i >= n by 1
#         arr[i] <- readNumber()
    
#     f(arr, n)
# end

# func f(number a[5], number n)
#     return
# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 428))

#     def test_redeclared_9(self):
#         input = """
# var f <- 10
# func f()
#     return

# func main()
# begin
#     dynamic a
#     dynamic b
#     number c
# end
# """
#         expect = "Redeclared Function: f"
#         self.assertTrue(TestChecker.test(input, expect, 429))

#     def test_redeclared_10(self):
#         input = """

# func main()
# begin
#     dynamic a
#     dynamic a
# end
# """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 430))


#     def test_redeclared_11(self):
#         input = """

# func main()
# begin
#     dynamic main
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 431))

#     def test_redeclared_12(self):
#         input = """
# number x <- 5
        
# func main(number x)
# begin
#     dynamic main
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 432))




#     # TEST NO ENTRY POINT
#     def test_noentrypoint_1(self):
#         input ="""
# number a <- 2
# number b <- 5
# var z <- 5

# func f(number a, string b)
# begin   
#     number c <-5
# end
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 441))

#     def test_noentrypoint_2(self):
#         input ="""
# number a <- 2
# number b <- 5
# var z <- 5

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 442))

#     def test_noentrypoint_3(self):
#         input ="""

# func Main()
# begin
# end

# number a <- 5
# number c <- 6


# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 443))


#     def test_noentrypoint_4(self):
#         input ="""

# func Main()
# begin    
#     number a <- 5
#     number c <- 6
# end



# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 444))

#     def test_noentrypoint_5(self):
#         input ="""

# func Main()
# begin    
# end



# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 445))


#     def test_noentrypoint_6(self):
#         input ="""

# var a <- 5

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 446))


#     def test_noentrypoint_7(self):
#         input ="""

# func MAIN()
# begin
# end

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 447))


#     def test_noentrypoint_8(self):
#         input ="""

# var a <- 5

# func MAIN()
# begin
# end

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 448))


#     def test_noentrypoint_9(self):
#         input ="""

# var a <- 5

# func MAIN()
# begin
# end

# number b <- 6

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 449))


#     def test_noentrypoint_10(self):
#         input ="""

# var a <- 5

# func MAIN()
# begin
#     number b <- 5
# end

# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 450))



# #   TEST NOT IN LOOP
#     def test_notinloop_1(self):
#         input = """
# func main()
#     begin
#         for i until i by [1]
#         begin
#             number a <- 5
#             number b <- 6

#             continue
#             break

#         end

#         break
#     end
# """
#         expect ="Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 451))



#     def test_notinloop_2(self):
#         input = """
# func main()
#     begin

#         break
#     end
# """
#         expect ="Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 452))


#     def test_notinloop_3(self):
#         input = """
# func main()
#     begin
#         if (true) begin
#             break
#         end
#         elif (false) begin
#             continue
#         end
#         else return true
#     end
# """
#         expect ="Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 453))


#     def test_notinloop_4(self):
#         input = """
# func main()
#     begin
#         if (true) begin
#             continue
#         end
#         elif (false) begin
#             break
#         end
#         else return true
#     end
# """
#         expect ="Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 454))


#     def test_notinloop_5(self):
#         input = """
# func main()
#     begin
#         if (true) continue
#         else break
#     end
# """
#         expect ="Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 455))


#     def test_notinloop_6(self):
#         input = """
# func main()
#     begin
#         for i until i by [1]
#         begin
#             writeNumber(1)
#             break
#         end
#     end
# """
#         expect =""
#         self.assertTrue(TestChecker.test(input, expect, 456))


#     def test_notinloop_7(self):
#         input = """
# func main()
#     begin
#         for i until i by [1]
#         begin
#             writeNumber(1)
#             if (true) break
#         end
#     end
# """
#         expect =""
#         self.assertTrue(TestChecker.test(input, expect, 457))


#     def test_notinloop_8(self):
#         input = """
# func main()
#     begin
#         for i until i by [1]
#         begin
#             writeNumber(1)
#             if (true) break
#             else begin
#                 continue
#             end
#         end
#     end
# """
#         expect =""
#         self.assertTrue(TestChecker.test(input, expect, 458))


#     def test_notinloop_9(self):
#         input = """
# func main()
#     begin
#         for i until i by [1]
#         begin
#             writeNumber(1)
#             if (true) break
#             else begin
#                 continue
#             end
#         end
#         break
#     end
# """
#         expect ="Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 459))


#     def test_notinloop_10(self):
#         input = """
# func f()
#     begin
#         continue
#     end
# func main()
#     begin
#         for i until i by [1]
#         begin
#             writeNumber(1)
#             if (true) break
#             else begin
#                 continue
#             end
#         end
#         break
#     end
# """
#         expect ="Continue Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 460))



# TEST TYPE MISMATCH IN EXPRESSION

#     def test_typemismatchinexpression_1(self):
#         input = """
# dynamic x
# func main()
# begin
#     x <- [1, 2, 3, 4, 5, 6]
#     var y <- x[0, 0] + 1
#     writeNumber(y)
# end
# """
#         expect ="Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 461))

#     def test_typemismatchinexpression_2(self):
#         input = """
# func f(number x[2, 3])
#     return x[2]

# func main()
# begin
#     number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
#     writeNumber(f()[2])
# end
# """
#         expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
#         self.assertTrue(TestChecker.test(input, expect, 462))


#     def test_typemismatchinexpression_3(self):
#         input = """
# func main()
# begin
#     number x <- 2 + true
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 463))



#     def test_typemismatchinexpression_4(self):
#         input = """
# func main()
# begin
#     var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0))), ArrayLit(ArrayLit(NumLit(6.0), NumLit(7.0), NumLit(8.0)), ArrayLit(NumLit(9.0), NumLit(10.0), NumLit(11.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 464))


#     def test_typemismatchinexpression_5(self):
#         input = """
# func f(number x)
# begin
#     if (x = 0) return 0
#     elif (x = 1) return 1
#     else return f(x - 1) + f(x - 2)
# end
    
# func main()
# begin
#     dynamic a
#     number x <- f(a)
#     a[0] <- [1, 2, 3]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 465))


#     def test_typemismatchinexpression_6(self):
#         input = """
# func main()
# begin
#     dynamic x
#     if (x) writeString("x is infer to true value")
#     else writeString("x is infer to false value")
#     x <- 1 + true
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 466))

#     def test_typemismatchinexpression_7(self):
#         input = """
# func f()
# begin
#     dynamic x
#     x <- (x - 2) * (x + true)
# end
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 467))

#     def test_typemismatchinexpression_8(self):
#         input = """
# number a <- 1 + "Hello"
# func main()
#     return
# """
#         expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(Hello))"
#         self.assertTrue(TestChecker.test(input, expect, 468))


#     def test_typemismatchinexpression_9(self):
#         input = """
# func f(number a[3], number b[3])
#     return

# func main()
# begin
#     f([1, 3, 2], [1, "Hello", 2])
# end
# """
#         expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(Hello), NumLit(2.0))"
#         self.assertTrue(TestChecker.test(input, expect, 469))


#     def test_typemismatchinexpression_10(self):
#         input = """
# func f(number x[2, 3])
#     return x[0]

# func main()
# begin
#     dynamic x <- f([[1, 2, 3], [4, 5, 6]])[2, 3]
#     writeNumber(x)
# end
# """
#         expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))]), [NumLit(2.0), NumLit(3.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 470))