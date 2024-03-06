import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_declared(self):
        """declared  declared  declared  declared"""
        input = """
            number VoTien
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
        input = """
            string VoTien <- 1
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), StringType(), None, NumberLiteral(1.0))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 302))
        
        input = """
            string Votien
            bool Votien
            string Votien <- 1
            bool Votien <- 1
        """
        expect = str(Program([
                VarDecl(Id("Votien"), StringType()),
                VarDecl(Id("Votien"), BoolType()),
                VarDecl(Id("Votien"), StringType(), None, NumberLiteral(1.0)),
                VarDecl(Id("Votien"), BoolType(), None, NumberLiteral(1.0))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 303))
        
        input = """
            string VoTien[5] <- 1
            string VoTien[5]
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), ArrayType([5.0], StringType()), None, NumberLiteral(1.0)),
                VarDecl(Id("VoTien"), ArrayType([5.0], StringType()))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 304))
        
        input = """
            number VoTien[5,3,4.2] <- 1
            bool VoTien[2,3,4]
        """
        expect = str(Program([
                VarDecl(Id("VoTien"), ArrayType([5.0, 3.0, 4.2], NumberType()), None, NumberLiteral(1.0)),
                VarDecl(Id("VoTien"), ArrayType([2.0, 3.0, 4.0], BoolType()))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 305))
        
        input = """
            dynamic Votien <- 1
            dynamic Votien
        """
        expect = str(Program([
                    VarDecl(Id("Votien"), None, "dynamic", NumberLiteral(1.0)),
                    VarDecl(Id("Votien"), None, "dynamic")
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 306))
        
        input = """
            var Votien <- 1
        """
        expect = str(Program([
                    VarDecl(Id("Votien"), None, "var", NumberLiteral(1.0))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 307))
        
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 308))
        
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 309))

        input = """
            func main()
                begin
                break
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Break()]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 310))
                
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number Votien[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("Votien"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 311))
        

