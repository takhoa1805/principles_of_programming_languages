import unittest
from TestUtils import TestChecker
from AST import *

# MODIFY THIS FILE FOR TESTCASES

class CheckerSuite(unittest.TestCase):
    def test_general(self):
        input ="""
number a <- 2
number b <- 5

func main(number a, string b)
begin 
    a <- 3
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))

#     def test_undeclared_1(self):
#         input = """
# number a <- f(2)
# func f(number x)

# func main()
#     begin

#     end

# """
#         expect="Undeclared Function: f"
#         self.assertTrue(TestChecker.test(input,expect,401))

#     def test_undeclared_2(self):
#         input = """
# func f(number j)

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
#         expect = "Undeclared Identifier: x"
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
#     number x
#     begin
#         number x <- (10 + x) * 2
#     end
# end
# """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 408))