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
        param =[['readNumber','writeNumber','readBool','writeBool','readString','writeString']]
        print(ast.decl)

        if ast.decl is None:
            raise NoEntryPoint()

        for decl in ast.decl:
            self.visit(decl,param)

        for ids in param:
            if 'main' not in ids:
                raise NoEntryPoint()

        print("param after program: " + str(param))
        # print(ast)
        

    def visitVarDecl(self, ast:VarDecl, param):
        name = self.getIdName(ast.name,param)
        print("Var decl is called: name("+str(name)+") type(" + str(ast.varType)+") - modifier(" + str(ast.modifier) +")")
        varType = ast.varType
        modifier = ast.modifier

        # CHECK FOR UNDECLARATION OF BOTH VAR AND FUNC
        if ast.varInit is not None:
            self.visit(ast.varInit,param)


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

        print("Name: " + str(name))
        print("Current scope: " + str(param[0]))

        if name in param[0]:
            raise Redeclared('Function',name)
        
        env = [[]] + param

        # To check redeclaration in function's parameters.
        for decl in ast.param:
            self.myVisitParameter(decl,env)

        # # To travel through every statements
        # for stmt in body:
        #     self.visit(stmt,env)

        if (ast.body is None):
            body = []
        else: 
            body = self.visit(ast.body,env)

        param[0] += [name]

        

    def visitNumberType(self, ast:NumberType, param):
        return NumberType()

    def visitBoolType(self, ast:BoolType, param):
        return BoolType()

    def visitStringType(self, ast:StringType, param):
        return StringType()

    # IN DECLARATION
    def visitArrayType(self, ast:ArrayType, param):
        print("Visit array type")
        print("Array size: " + str(ast.size))
        print("Array element type: " + str(ast.eleType))
        
        size_list = ast.size

        for size in size_list:
            self.visit(size,param)

        eleType = self.visit(ast.eleType,param)

        return eleType

    # VISIT BINARY OPERATORS
    def visitBinaryOp(self, ast:BinaryOp, param):
        print("Visit Binary op: " + str(ast.op))

        # CHECKING UNDECLARED
        left = self.visit(ast.left,param)
        right = self.visit(ast.right,param)

    # VISIT UNARY OPERATORS
    def visitUnaryOp(self, ast:UnaryOp, param):
        print("Visit unary op: " + str(ast.op))

        # CHECKING UNDECLARED
        oeprand = self.visit(ast.operand,param)



    def visitCallExpr(self, ast:CallExpr, param):
        print("Visit call expr")
        name = self.getIdName(ast.name,param)
        args = ast.args
        print("Call expr with name = " + str(name) +" expr = "+ str(args))
        self.visitFunctionId(ast.name,param)
        
        for id in args:
            self.visit(id,param)

        



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
        raise Undeclared("Identifier",str(ast.name))
        
    # VISIT FUNCTION IDENTIFIER ===> FOR FUNCTION UNDECLARATION CHECKING ONLY
    def visitFunctionId(self,ast:Id,param):
        print("Visited function id: " + str(ast.name))
        print("Identifier environment: " + str(param))
        for id in param:
            if(ast.name in id):
                return
        raise Undeclared("Function",str(ast.name))

    # IN EXPRESSION
    def visitArrayCell(self, ast:ArrayCell, param):
        print("Visit array cell")
        self.visit(ast.arr, param)
        idx_list = ast.idx

        for idx in idx_list:
            self.visit(idx,param)

    # STATEMENT BLOCK 
    def visitBlock(self, ast:Block, param):
        print("Visit statement block: " + str(ast.stmt))
        stmt_list = ast.stmt

        for stmt in stmt_list:
            self.visit(stmt,param)

        return ast.stmt

    # IF STATEMENT
    def visitIf(self, ast:If, param):
        print("Visit if statement " + str(ast))

        # CHECK UNDECLARED IDENTIFIER
        expr = self.visit(ast.expr,param)

        # VISIT ALL STATEMENTS
        thenStmt = self.visit(ast.thenStmt,param)
        elifStmt_list = ast.elifStmt
        for elifStmt in elifStmt_list:
            self.visit(elifStmt[0],param)
            self.visit(elifStmt[1],param)

        if (ast.elseStmt is not None):
            elseStmt = self.visit(ast.elseStmt,param)
        



    # FOR STATEMENT
    def visitFor(self, ast:For, param):
        print("Visit for statement")
        # VISIT EVERY COMPONENT
        
        # IDENTIFIER IN FOR LOOP MUST BE DEFINED
        name = self.getIdName(ast.name,param)

        # IS IN LOOP FLAG AT FIRST ELEMENT
        env =[[True]]+[[name]] + param


        condExpr = self.visit(ast.condExpr,env)
        updExpr = self.visit(ast.updExpr,env)
        body = self.visit(ast.body,env)

        


    #CONTINUE STATEMENT
    def visitContinue(self, ast:Continue, param):
        print("Visit continue statement: " + str(ast))
        print(param)
        if len(param[0]) == 0 or  not param[0][0]:
            raise MustInLoop(ast)

    # BREAK STATEMENT
    def visitBreak(self, ast:Break, param):
        print("Visit break statement: " + str(ast))
        if len(param[0]) == 0 or  not param[0][0]:
            raise MustInLoop(ast)


    # RETURN STATEMENT
    def visitReturn(self, ast:Return, param):
        print("Visit return statement")
        # VISIT EXPRESSION
        expr = self.visit(ast.expr,param)

    # ASSIGN STATEMENT
    def visitAssign(self, ast:Assign, param):
        print("Visit assign statement")
        # CHECK IF RHS EXPRESSION CONTAINS UNDECLARED IDENTIFIER
        rhs = self.visit(ast.rhs,param)
        # CHECK IF LHS EXPRESSION CONTAINS UNDECLARED IDENTIFIER
        lhs = self.visit(ast.lhs,param)


    # VISIT FUNCTION CALL STATEMENT
    def visitCallStmt(self, ast:CallStmt, param):
        print("Visit function call statement")

        # VISIT EVERY COMPONENTS
        name = self.getIdName(ast.name,param)
        self.visitFunctionId(ast.name,param)
        args = ast.args

        for id in args:
            self.visit(id,param)

        print("Call expr with name = " + str(name) +" expr = "+ str(args))
        
        




    def visitNumberLiteral(self, ast:NumberLiteral, param):
        return NumberType()

    def visitBooleanLiteral(self, ast:BooleanLiteral, param):
        return BoolType()

    def visitStringLiteral(self, ast:StringLiteral, param):
        return StringType()

    def visitArrayLiteral(self, ast:ArrayLiteral, param):
        print("Visit array literal: " + str(ast))
