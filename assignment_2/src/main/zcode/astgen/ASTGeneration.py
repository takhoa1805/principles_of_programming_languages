from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


#MODIFY THIS FILE TO GENERATE PARSE TREE

class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])
    
    def visitDecllist(self,ctx: ZCodeParser.DecllistContext):
        pass

    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        pass

    def visitVardecl(self,ctx:ZCodeParser.VardeclContext):
        pass

    def visitArrlist(self, ctx:ZCodeParser.ArrlistContext):
        pass

    def visitArray_expression(self,ctx:ZCodeParser.Array_expressionContext):
        pass

    def visitArrlist_expression(self,ctx:ZCodeParser.Arrlist_expressionContext):
        pass

    def visitExpression(self,ctx:ZCodeParser.ExpressionContext):
        pass

    def visitSign_operands(self,ctx:ZCodeParser.Sign_operandsContext):
        pass

    def visitNot_operands(self, ctx:ZCodeParser.Not_operandsContext):
        pass

    def visitIndex_operators(self,ctx:ZCodeParser.Index_operatorsContext):
        pass

    def visitFunc_call(self,ctx: ZCodeParser.Func_callContext):
        pass

    #THIS IS OBSOLETE
    def visitSign_operands(self,ctx:ZCodeParser.Sign_operandsContext):
        pass

    #param_list: param_prime | ;
    def visitParam_list(self,ctx: ZCodeParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.param_prime())

    #param_prime: param COMMA param_prime | param;
    def visitParam_prime(self,ctx: ZCodeParser.Param_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.param_prime())

    #param: expression;
    def visitParam(self,ctx: ZCodeParser.ParamContext):
        return self.visit(ctx.expression())

    #THIS IS OBSOLETE
    def visitNon_rel_operators(self,ctx:ZCodeParser.Non_rel_operatorsContext):
        pass

    #THIS IS OBSOLETE
    def visitNon_str_operators(self,ctx: ZCodeParser.Non_str_operatorsContext):
        pass

    #THIS IS OBSOLETE
    def visitNon_associative_operands(self,ctx: ZCodeParser.Non_associative_operandsContext):
        pass

    #typ: BOOL_TYPE | NUMBER_TYPE | STRING_TYPE;
    def visitTyp(self,ctx:ZCodeParser.TypContext):
        if ctx.BOOL_TYPE():
            return BoolType()
        elif ctx.NUMBER_TYPE():
            return NumberType()
        elif ctx.STRING_TYPE():
            return StringType()
        else: return None

    #literal: STRING | NUMBER | BOOLEAN | IDENTIFIER;
    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        if ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.NUMBER():
            value = float(ctx.NUMBER().getText())
            return NumberLiteral(value)
        elif ctx.BOOLEAN():
            value = ctx.BOOLEAN().getText() == 'true'
            return BooleanLiteral(value)
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return None

    #mul_operators: MUL_OPERATOR | DIV_OPERATOR | MOD_OPERATOR;
    def visitMul_operators(self,ctx: ZCodeParser.Mul_operatorsContext):
        if ctx.MUL_OPERATOR():
            return ctx.MUL_OPERATOR().getText()
        elif ctx.DIV_OPERATOR():
            return ctx.DIV_OPERATOR().getText()
        elif ctx.MOD_OPERATOR():
            return ctx.MOD_OPERATOR().getText()
        else: 
            return None

    #add_operators: ADD_OPERATOR | SUB_OPERATOR;
    def visitAdd_operators(self,ctx: ZCodeParser.Add_operatorsContext):
        if ctx.ADD_OPERATOR():
            return ctx.ADD_OPERATOR().getText()
        elif ctx.SUB_OPERATOR():
            return ctx.SUB_OPERATOR().getText()
        else: return None

    #logic_operators: AND_OPERATOR | OR_OPERATOR;   
    def visitLogic_operators(self, ctx: ZCodeParser.Logic_operatorsContext):
        if ctx.OR_OPERATOR():
            return ctx.OR_OPERATOR().getText()
        elif ctx.AND_OPERATOR():
            return ctx.AND_OPERATOR().getText()
        else: return None

    # rel_operators: 
    # 	EQ_OPERATOR 
    # 	| 
    # 	SEQ_OPERATOR 
    # 	| 
    # 	NEQ_OPERATOR 
    # 	| 
    # 	LT_OPERATOR
    # 	|
    # 	GT_OPERATOR
    # 	|
    # 	LEQ_OPERATOR
    # 	|
    # 	GEQ_OPERATOR
    # ;
    def visitRel_operators(self, ctx: ZCodeParser.Rel_operatorsContext):
        if ctx.EQ_OPERATOR():
            return ctx.EQ_OPERATOR().getText()
        elif ctx.SEQ_OPERATOR():
            return ctx.SEQ_OPERATOR().getText()
        elif ctx.NEQ_OPERATOR():
            return ctx.NEQ_OPERATOR().getText()
        elif ctx.LT_OPERATOR():
            return ctx.LT_OPERATOR().getText()
        elif ctx.GT_OPERATOR():
            return ctx.GT_OPERATOR().getText()
        elif ctx.LEQ_OPERATOR():
            return ctx.LEQ_OPERATOR().getText()
        elif ctx.GEQ_OPERATOR():
            return ctx.GEQ_OPERATOR().getText()
        else:
            return None

    #str_operators: STRING_OPERATOR;
    def visitStr_operators(self, ctx: ZCodeParser.Str_operatorsContext):
        return ctx.STRING_OPERATOR()

    #funcdecl: 'func' IDENTIFIER OPEN_PARENTHESIS param_decl_list CLOSE_PARENTHESIS newline_list body  newline_list;
    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = self.viit(ctx.param_decl_list())
        body = self.visit(ctx.body()) if ctx.body() else None
        return FuncDecl(name,param,body)

    #param_decl_list: param_decl_prime | ;
    def visitParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return self.visit(ctx.param_decl_prime())

    # param_decl_prime: 
    # 	param_single_decl COMMA param_decl_prime 
    # 	| 
    # 	param_single_decl
    # ;
    def visitParam_decl_prime(self, ctx:ZCodeParser.Param_decl_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param_single_decl())]
        else:
            return [self.visit(ctx.param_single_decl())] + self.visit(ctx.param_decl_prime())

    # param_single_decl:
    # 	//Declaration only
    # 	typ IDENTIFIER 
    # 	|
    # 	//Array declaration only
    # 	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET 
    # ;
    def visitParam_single_decl(self, ctx:ZCodeParser.Param_single_declContext):
        if ctx.getChildCount() == 2:
            name = Id(ctx.IDENTIFIER().getText())
            varType = self.visit(ctx.typ())
            return VarDecl(name,varType,None,None)
        else:
            name = Id(ctx.IDENTIFIER().getText())
            eleType = self.visit(ctx.typ())
            size = self.visit(ctx.arrlist())
            varType = ArrayType(size,eleType)
            return VarDecl(name,varType,None,None)
    
    #SKIP THIS AS PROGRAM IGNORES NEWLINES
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass

    #body: statement_block | ret |  ;
    def visitBody(self,ctx:ZCodeParser.BodyContext):
        if ctx.statement_block():
            return self.visit(ctx.statement_block())
        elif ctx.ret():
            return self.visit(ctx.ret())
        else:
            return None

    #statement_block: BEGIN statement_list END NEWLINE newline_list;
    def visitStatement_block(self, ctx: ZCodeParser.Statement_blockContext):
        stmt = self.visit(ctx.statement_list())
        return Block(stmt)

    #statement_list: newline_list statement newline_list statement_list | newline_list;
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        if ctx.getChildCount() == 1:
            return []
        else:
            return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())
    
    # statement: 
    # 	vardecl
    # 	|
    # 	assignment_statement 
    # 	|
    # 	if_statement 
    # 	|
    # 	for_statement 
    # 	|
    # 	break_statement 
    # 	|
    # 	continue_statement 
    # 	|
    # 	return_statement 
    # 	|
    # 	func_call_statement 
    # 	|
    # 	statement_block
    # ;
    def visitStatement(self,ctx:ZCodeParser.StatementContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.func_call_statement():
            return self.visit(ctx.func_call_statement())
        elif ctx.statement_block():
            return self.visit(ctx.statement_block())
        
        return None

    #ret: RETURN expression | RETURN;
    def visitRet(self,ctx:ZCodeParser.RetContext):
        if ctx.getChildCount() == 1:
            return Return(None)
        else:
            return Return(self.visit(ctx.expression()))

    #return_statement: ret NEWLINE newline_list;
    def visitReturn_statement(self,ctx:ZCodeParser.Return_statementContext):
        return self.visit(ctx.ret())

    #func_call_statement: func_call NEWLINE newline_list;
    def visitFunc_call_statement(self,ctx:ZCodeParser.Func_call_statementContext):
        return self.visit(ctx.func_call())

    #assignment_statement: lhs ASSIGN_OPERATOR rhs NEWLINE newline_list;
    def visitAssignment_statement(self,ctx: ZCodeParser.Assignment_statementContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.rhs())
        return Assign(lhs,rhs)

    # lhs: expression;
    def visitLhs(self,ctx:ZCodeParser.LhsContext):
        return self.visit(ctx.expression())


    #rhs: expression;
    def visitRhs(self,ctx:ZCodeParser.RhsContext):
        return self.visit(ctx.expression())

    #if_statement: IF OPEN_PARENTHESIS expression CLOSE_PARENTHESIS if_body elif_statement_list else_statement newline_list;
    def visitIf_statement(self,ctx:ZCodeParser.If_statementContext):
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.if_body())        
        elifStmt = self.visit(ctx.elif_statement_list())
        elseStmt = self.visit(ctx.else_statement())
        return If(expr,thenStmt,elifStmt,elseStmt)

    # if_body:
    # 	statement
    # 	|
    # 	statement_block
    # 	|
    # 	NEWLINE
    # ;
    def visitIf_body(self,ctx:ZCodeParser.If_bodyContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        elif ctx.statement_block():
            return self.visit(ctx.statement_block())
        else:
            return None

    #elif_statement_list: elif_statement elif_statement_list |  ;
    def visitElif_statement_list(self,ctx:ZCodeParser.Elif_statement_listContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [self.visit(ctx.elif_statement())] + self.visit(ctx.elif_statement_list())
    
    #elif_statement: ELIF OPEN_PARENTHESIS expression CLOSE_PARENTHESIS if_body;
    def visitElif_statement(self,ctx:ZCodeParser.Elif_statementContext):
        expr = self.visit(ctx.expression())
        stmt = self.visit(ctx.if_body())
        return (expr,stmt)

    #else_statement: ELSE if_body |  ;
    def visitElse_statement(self,ctx:ZCodeParser.Else_statementContext):
        if ctx.getChildCount() == 0:
            return None
        else:
            return self.visit(ctx.if_body())

    #for_statement: FOR IDENTIFIER UNTIL expression BY expression newline_list for_body;
    def visitFor_statement(self,ctx:ZCodeParser.For_statementContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = self.visit(ctx.expression(0))
        updExpr = self.visit(ctx.expression(1))
        body = self.visit(ctx.for_body())
        return For(name,condExpr,updExpr,body)

    # for_body: 	
    # 	statement
    # 	|
    # 	statement_block
    # 	|
    # 	NEWLINE
    # ;
    def visitFor_body(self,ctx:ZCodeParser.For_bodyContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        elif ctx.statement_block():
            return self.visit(ctx.statement_block())
        else:
            return None
    
    #break_statement: BREAK_STATEMENT NEWLINE newline_list;
    def visitBreak_statement(self,ctx:ZCodeParser.Break_statementContext):
        return Break()

    #continue_statement: CONTINUE_STATEMENT NEWLINE newline_list;
    def visitContinue_statement(self,ctx:ZCodeParser.Continue_statementContext):
        return Continue()

