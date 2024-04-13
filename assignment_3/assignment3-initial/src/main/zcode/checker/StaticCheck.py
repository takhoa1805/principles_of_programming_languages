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

        name = self.getIdName(ast.name,param)
        if name in param[0]:
            raise Redeclared('Variable',name)

        param[0] += [name]

    def myVisitParameter(self,ast:VarDecl,param):
        print("Param decl is called")

        name = self.getIdName(ast.name,param)

        if name in param[0]:
            raise Redeclared('Parameter',name)
        param[0] += [name] 

    def visitFuncDecl(self, ast: FuncDecl, param):
        print("Func decl is called")
        name = self.getIdName(ast.name,param)
        body = self.visit(ast.body,param)

        # print(body)

        if name in param[0]:
            raise Redeclared('Function',name)
        
        env = [[]] + param

        # To check redeclaration in function's parameters.
        for decl in ast.param:
            self.myVisitParameter(decl,env)

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

    # VISIT BINARY OPERATORS
    def visitBinaryOp(self, ast:BinaryOp, param):
        print("Visit Binary op")

        # CHECKING UNDECLARED
        left = self.visit(ast.left,param)
        right = self.visit(ast.right,param)

    # VISIT UNARY OPERATORS
    def visitUnaryOp(self, ast:UnaryOp, param):
        print("Visit unary op")

        # CHECKING UNDECLARED
        oeprand = self.visit(ast.operand,param)

    def visitCallExpr(self, ast:CallExpr, param):
        print("Visit call expr")


    # GET IDENTIFER'S NAME => FOR ADDING TO ENV LIST
    def getIdName(self,ast:Id, param):
        print("Get Id's name: "+str(ast.name))
        return ast.name


    # VISIT IDENTIFIER ==> FOR UNDECLARATION CHECKING ONLY
    def visitId(self, ast: Id, param):
        print("Visited id = " + str(ast.name))
        print("Identifier environment: "+str(param))
        for id in param:
            if (ast.name in id):
                return 
        raise Undeclared('Identifier',ast.name)
        

    def visitArrayCell(self, ast:ArrayCell, param):
        print("Visit array cell")

    # STATEMENT BLOCK 
    def visitBlock(self, ast:Block, param):
        print("Visit statement block ")
        return ast.stmt

    # IF STATEMENT
    def visitIf(self, ast:If, param):
        print("Visit if statement")

        # CHECK UNDECLARED IDENTIFIER
        expr = self.visit(ast.expr,param)

        # VISIT ALL STATEMENTS
        thenStmt = self.visit(ast.thenStmt,param)
        elifStmt = self.visit(ast.elifStmt,param)
        elseStmt = self.visit(ast.elseStmt,param)



    # FOR STATEMENT
    def visitFor(self, ast:For, param):
        print("Visit for statement")
        # VISIT EVERY COMPONENT
        
        # IDENTIFIER IN FOR LOOP MUST BE DEFINED
        name = self.getIdName(ast.name,param)
        env =[[name]] + param


        condExpr = self.visit(ast.condExpr,env)
        updExpr = self.visit(ast.updExpr,env)
        body = self.visit(ast.body,env)

        


    #CONTINUE STATEMENT
    def visitContinue(self, ast:Continue, param):
        print("Visit continue statement")

    # BREAK STATEMENT
    def visitBreak(self, ast:Break, param):
        print("Visit break statement")

    # RETURN STATEMENT
    def visitReturn(self, ast:Return, param):
        print("Visit return statement")
        # VISIT EXPRESSION
        expr = self.visit(ast.expr,param)

    # ASSIGN STATEMENT
    def visitAssign(self, ast:Assign, param):
        print("Visit assign statement")
        # CHECK IF LHS EXPRESSION CONTAINS UNDECLARED IDENTIFIER
        lhs = self.visit(ast.lhs,param)
        # CHECK IF RHS EXPRESSION CONTAINS UNDECLARED IDENTIFIER
        rhs = self.visit(ast.rhs,param)

    # VISIT FUNCTION CALL STATEMENT
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
