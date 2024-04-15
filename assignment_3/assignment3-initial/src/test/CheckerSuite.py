import unittest
from TestUtils import TestChecker
from AST import *

# MODIFY THIS FILE FOR TESTCASES

class CheckerSuite(unittest.TestCase):
#     def test_general(self):
#         input = """
# func f(number j)
# begin
# end

# func main()
# begin
#     a(5)
# end
# """
#         expect ="Undeclared Function: a"
#         self.assertTrue(TestChecker.test(input, expect, 400))


# TEST UNDECLARATION

    def test_undeclared_1(self):
        input = """
number a <- f(2)

func f(number x)
begin
end

func main()
    begin

    end

"""
        expect="Undeclared Function: f"
        self.assertTrue(TestChecker.test(input,expect,401))

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
#         expect ="Undeclared Function: g"
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
#         expect = "Undeclared Identifier: a"
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



    # TEST REDECLARATION
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