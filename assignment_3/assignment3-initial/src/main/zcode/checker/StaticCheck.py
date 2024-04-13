from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


# MODIFY THIS FILE FOR STATIC CHECKER



class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast: Program) -> None:
        self.ast = ast
        self.env =[[]]

    def check(self):
        self.visit(self.ast,self.env)



    def visitProgram(self, ast:Program, param):
        param =[[]]
        print(ast.decl)
        for decl in ast.decl:
            self.visit(decl,param)
        # print(ast)
        

    def visitVarDecl(self, ast:VarDecl, param):
        print("Var decl is called")

        name = self.visit(ast.name,param)
        if name in param[0]:
            raise Redeclared('Variable',name)

        param[0] += [name]

    def myVisitParameter(self,ast:VarDecl,param):
        print("Param decl is called")

        name = self.visit(ast.name,param)
        if name in param[0]:
            raise Redeclared('Parameter',name)
        param[0] += [name] 

    def visitFuncDecl(self, ast: FuncDecl, param):
        print("Func decl is called")
        name = self.visit(ast.name,param)
        body = self.visit(ast.body,param)

        # print(body)

        if name in param[0]:
            raise Redeclared('Function',name)
        
        env = [[]] + param

        # To check redeclaration in function's parameters.
        for decl in ast.param:
            self.myVisitParameter(decl,env)
    
        # # To check redeclaration in function's body
        # for decl in body:
        #     print(decl)
        #     self.visit(decl,env)  

        # To travel through every statements
        for stmt in body:
            self.visit(stmt,env)


        param[0] += [name]

        

    def visitNumberType(self, ast:NumberType, param):
        return NumberType()

    def visitBoolType(self, ast:BoolType, param):
        return BoolType()

    def visitStringType(self, ast:StringType, param):
        return StringType()

    def visitArrayType(self, ast:ArrayType, param):
        print("Visit array type")

    def visitBinaryOp(self, ast:BinaryOp, param):
        print("Visit Binary op")

    def visitUnaryOp(self, ast:UnaryOp, param):
        print("Visit unary op")

    def visitCallExpr(self, ast:CallExpr, param):
        print("Visit call expr")

    def visitId(self, ast: Id, param):
        print("Visited id = " + str(ast.name))
        return ast.name

    def visitArrayCell(self, ast:ArrayCell, param):
        print("Visit array cell")

    def visitBlock(self, ast:Block, param):
        print("Visit statement block ")
        return ast.stmt

    def visitIf(self, ast:If, param):
        print("Visit if statement")

    def visitFor(self, ast:For, param):
        print("Visit for statement")

    def visitContinue(self, ast:Continue, param):
        print("Visit continue statement")

    def visitBreak(self, ast:Break, param):
        print("Visit break statement")


    def visitReturn(self, ast:Return, param):
        print("Visit return statement")

    def visitAssign(self, ast:Assign, param):
        print("Visit assign statement")
        self.visit(ast.lhs,param)

    def visitCallStmt(self, ast:CallStmt, param):
        print("Visit function call statement")

    def visitNumberLiteral(self, ast:NumberLiteral, param):
        return NumberType()

    def visitBooleanLiteral(self, ast:BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast:StringLiteral, param):
        return StringType()

    def visitArrayLiteral(self, ast:ArrayLiteral, param):
        print("Visit array literal")
