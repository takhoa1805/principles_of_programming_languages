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
        
    def test_Expression(self):
        """Expression Expression Expression"""
        input = """
            var x <- 1
            var x <- "123"
            var x <- true
            var x <- false
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
                    VarDecl(Id("x"), None, "var",  StringLiteral("123")),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 312))
        
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 313))   
        
        input = """   
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)]), ArrayLiteral([NumberLiteral(1.0)])])),
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(1.0)])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 314))  
        
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("<=", NumberLiteral(1.0), StringLiteral("2"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("-", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)), NumberLiteral(4.0))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1.0))))),
                    VarDecl(Id("x"), None, "var",  UnaryOp("not", UnaryOp("not", NumberLiteral(1.0)))),
                    VarDecl(Id("x"), None, "var",  Id("x")),
                    VarDecl(Id("x"), None, "var",  ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 315))  
        
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(1.0)), NumberLiteral(2.0)), BinaryOp("<=", NumberLiteral(4.0), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5.0), BinaryOp("*", Id("a"), NumberLiteral(3.0))), Id("c")), UnaryOp("-", NumberLiteral(1.0))), UnaryOp("not", UnaryOp("-", NumberLiteral(2.0)))))))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 316))  
        
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0))])), NumberLiteral(2.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 317))  
        
        input = """
            var x <- fun()
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), []))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 318)) 
        
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), StringLiteral("a")]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 319)) 
        
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  CallExpr(Id("fun"), [CallExpr(Id("fun"), [])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 320)) 
        
        input = """
            var x <- 2 ... 3 ... 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", BinaryOp("...", NumberLiteral(2.0), NumberLiteral(3.0)), NumberLiteral(4.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 321)) 

    def test_Statements(self):
        """Statements Statements Statements"""
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue()]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 322))

        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                        Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 323))
        
        input = """
            func main()
                begin
                    return  1 + 1
                    return
                end
            func main()
                return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0))),
                    Return()])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 324))

        input = """
            func main()
                begin
                    main(a)
                    main(1,1)
                end
            func main()
                begin
                main()
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [Id("a")]),
                    CallStmt(Id("main"), [NumberLiteral(1.0), NumberLiteral(1.0)])])),
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 325))
        
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
            func main()
                begin
                a[1+1, 3] <- 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Assign(Id("a"), NumberLiteral(1.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1.0)]), NumberLiteral(2.0)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(3.0), NumberLiteral(2.0)]), BinaryOp("+", NumberLiteral(4.0), NumberLiteral(2.0)))])),
                    FuncDecl(Id("main"), [], Block([
                    Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), NumberLiteral(3.0)]), NumberLiteral(1.0))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 326))
        
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2.0)), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(1.0)), CallStmt(Id("print"), [NumberLiteral(1.0)]))])),
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1.0)]), Block([
                    CallStmt(Id("print"), [NumberLiteral(1.0)])]))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 327))
        
        input = """
            func main()
                begin
                    if (true) return 1
                end
            func main()
                begin
                    if (true) return 2
                    else return 3
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [] , None)])),
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(2.0)), [] ,Return(NumberLiteral(3.0)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 328))
        

        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 1
                    elif (true) return 1
                    else return 1
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1.0)), 
                       [(BooleanLiteral(True),Return(NumberLiteral(1.0))),
                        (BooleanLiteral(True),Return(NumberLiteral(1.0)))] 
                    ,Return(NumberLiteral(1.0)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 329))     
        
        input = """
            var c <- a[1,2]
            var c <- fun()[1,2]
            var c <- fun(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("c"), None, "var", ArrayCell(Id("a"), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), []), [NumberLiteral(1.0), NumberLiteral(2.0)])),
            VarDecl(Id("c"), None, "var", ArrayCell(CallExpr(Id("fun"), [NumberLiteral(1.0), NumberLiteral(2.0)]), [NumberLiteral(1.0), NumberLiteral(3.0)]))
        ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 330))    
        
        input = """
            func main()
            begin
                var c <- 2e5
                dynamic c <- 2.56
                dynamic c
                number c[2e2, 2] <- 3.6
                string c[3.823]
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block(
                [VarDecl(Id("c"), None, "var", NumberLiteral(200000.0)), 
                 VarDecl(Id("c"), None, "dynamic", NumberLiteral(2.56)), 
                 VarDecl(Id("c"), None, "dynamic"),
                 VarDecl(Id("c"), ArrayType([200.0, 2.0], NumberType()), None, NumberLiteral(3.6)),
                 VarDecl(Id("c"), ArrayType([3.823], StringType()), None)
            ]))]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 331))  

    def test_for_statements(self):
        """For Statements"""
        input = """
            func main()
            begin 
                for i until i < 10 by 1
                    print(i)
            end
        """
        expect = str(Program([
           FuncDecl(Id("main"), [], Block([
               For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("print"), [Id("i")]))
           ]))
        ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 332))  


        input = """
            func main()
            begin 
                for i until i < 10 by 1
                    print(i)
                    var a <- 5
            end
        """
        expect = str(Program([
           FuncDecl(Id("main"), [], Block([
               For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), CallStmt(Id("print"), [Id("i")])), VarDecl(Id("a"),None,"var",NumberLiteral(5.0))
           ]))
        ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 333))

        input = """
        func main()
            begin

                number arr[5] <- [1, 2, 3, 4, 5]

                var index <- 2

                
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"),[],Block([
                VarDecl(Id("arr"),ArrayType([5.0],NumberType()),None,ArrayLiteral([NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0),NumberLiteral(5.0)])),
                VarDecl(Id("index"),None,"var",NumberLiteral(2.0))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 334))  

        
        input = """
        func main()
            begin
                var x <- (1 + 2) * (3 - 4) / (5 % 6)
                print(x)
            end
        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("x"), None, "var", BinaryOp("/", BinaryOp("*", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("-", NumberLiteral(3.0), NumberLiteral(4.0))), BinaryOp("%", NumberLiteral(5.0), NumberLiteral(6.0)))), CallStmt(Id("print"), [Id("x")])]))]))
        self.assertTrue(TestAST.test(input, expect, 335))


        input = """
        func foo()
            begin
                var x <- (1 + 2) * (3 - 4) / (5 % 6)
                print(x)
            end
        """
        expect = str(Program([FuncDecl(Id("foo"), [], Block([VarDecl(Id("x"), None, "var", BinaryOp("/", BinaryOp("*", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), BinaryOp("-", NumberLiteral(3.0), NumberLiteral(4.0))), BinaryOp("%", NumberLiteral(5.0), NumberLiteral(6.0)))), CallStmt(Id("print"), [Id("x")])]))]))
        self.assertTrue(TestAST.test(input, expect, 336))



        input = """
            var x <- 1 + 2 +3
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("+", BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(3.0)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 337)) 

        input = """func main()
                begin
                    ##this is a comment
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([]))]))
        self.assertTrue(TestAST.test(input,expect,338))  
    
        input = """func main() 
                begin
                    break 
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block(["Break"]))]))
        self.assertTrue(TestAST.test(input,expect,339)) 

        input = """func main() 
                begin
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([]))]))
        self.assertTrue(TestAST.test(input,expect,339)) 

        input = """func main()
                begin
                    dynamic a <- 1
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), None, "dynamic", NumberLiteral(1.0))]))]))
        self.assertTrue(TestAST.test(input,expect,340)) 

        input = """func main()
                begin
                    begin
                        begin
                           i <- i + 1
                        end
                    end
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([Block([Block([Assign(Id("i"), BinaryOp("+", Id("i"), NumberLiteral(1.0)))])])]))]))
        self.assertTrue(TestAST.test(input,expect,341))
    
        input = """
                func main()
                begin
                    number a <- 0
                    if (1 < 2) if (2 < 3) a <- 1
                    if (5 < 6) a <- 2
                    else a <- 3
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(0.0)), 
                If((BinaryOp("<", NumberLiteral(1.0), NumberLiteral(2.0))), 
                   If((BinaryOp("<", NumberLiteral(2.0), NumberLiteral(3.0))), Assign(Id("a"), NumberLiteral(1.0)), [], None), [], None), 
                If((BinaryOp("<", NumberLiteral(5.0), NumberLiteral(6.0))), Assign(Id("a"), NumberLiteral(2.0)), [], Assign(Id("a"), NumberLiteral(3.0)))]))]))
        self.assertTrue(TestAST.test(input,expect,342)) 


        input ="""func main()
                begin
                    readNumber()
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([CallStmt(Id("readNumber"), [])]))]))
        self.assertTrue(TestAST.test(input,expect,343))    
    
        input ="""func main()
                begin
                    readNumber(5)
                end
                """
        expect =str(Program([FuncDecl(Id("main"), [], Block([CallStmt(Id("readNumber"), [NumberLiteral(5.0)])]))]))
        self.assertTrue(TestAST.test(input,expect,344))

        input ="""func add(number a, number b)
                return a + b
            func main()
            begin
                number a <- 10
                number b <- 3
                number sum <- add(a, b)
                print(sum)
            end
                """
        expect =str(Program([FuncDecl(Id("add"), [VarDecl(Id("a"), NumberType(), None, None), VarDecl(Id("b"), NumberType(), None, None)], Return(BinaryOp("+", Id("a"), Id("b")))), FuncDecl(Id("main"), [], Block([VarDecl(Id("a"), NumberType(), None, NumberLiteral(10.0)), VarDecl(Id("b"), NumberType(), None, NumberLiteral(3.0)), VarDecl(Id("sum"), NumberType(), None, CallExpr(Id("add"), [Id("a"), Id("b")])), CallStmt(Id("print"), [Id("sum")])]))]))
        self.assertTrue(TestAST.test(input,expect,345))   
  
        input = """func check(bool flag, number a, number b)
            begin
                if (flag) return a
                else return b
            end
        """
        expect = str(Program([FuncDecl(Id("check"), [VarDecl(Id("flag"), BoolType()),VarDecl(Id("a"), NumberType()), VarDecl(Id("b"), NumberType())], Block([If(Id("flag"), Return(Id("a")), [], Return(Id("b")))]))]))
        self.assertTrue(TestAST.test(input, expect, 346))