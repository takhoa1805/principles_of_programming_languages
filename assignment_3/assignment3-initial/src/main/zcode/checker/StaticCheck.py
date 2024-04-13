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


        if name in param[0]:
            raise Redeclared('Function',name)
        
        env = [[]] + param

        # To check redeclaration in function's parameters.
        for decl in ast.param:
            self.myVisitParameter(decl,env)
    
        # To check redeclaration in function's body
        for decl in body:
            self.visit(decl,env)  

        for stmt in body:
            print(stmt)


        param[0] += [name]

        

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        print("Visit Binary op")

    def visitUnaryOp(self, ast, param):
        print("Visit unary op")

    def visitCallExpr(self, ast, param):
        print("Visit call expr")

    def visitId(self, ast: Id, param):
        print("Visited id = " + str(ast.name))
        return ast.name

    def visitArrayCell(self, ast, param):
        print("Visit array cell")

    def visitBlock(self, ast:Block, param):
        print("Visit statement block ")
        # print(ast)
        return ast.stmt

    def visitIf(self, ast, param):
        print("Visit if statement")

    def visitFor(self, ast, param):
        print("Visit for statement")

    def visitContinue(self, ast, param):
        print("Visit continue statement")

    def visitBreak(self, ast, param):
        print("Visit break statement")


    def visitReturn(self, ast, param):
        print("Visit return statement")

    def visitAssign(self, ast, param):
        print("Visit assign statement")

    def visitCallStmt(self, ast, param):
        print("Visit function call statement")

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        print("Visit array literal")
