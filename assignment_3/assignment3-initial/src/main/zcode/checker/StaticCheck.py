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

    def visitVarDecl(self, ast:VarDecl, param):
        print("Var decl is called")
        name = self.visit(ast.name,param)
        if name in param[0]:
            raise Redeclared('Variable',name)
        param[0] += [name]

    def visitFuncDecl(self, ast: FuncDecl, param):
        print("Func decl is called")
        name = self.visit(ast.name,param)
        if name in param[0]:
            raise Redeclared('Function',name)
        
        env = [[]] + param

        for decl in ast.param:
            self.visit(decl,env)

        print(ast.body)
        
        


    def visitNumberType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast: Id, param):
        return ast.name

    def visitArrayCell(self, ast, param):
        pass

    def visitBlock(self, ast, param):
        pass

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        pass
