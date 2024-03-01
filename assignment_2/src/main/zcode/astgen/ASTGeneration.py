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

    def visitParam_list(self,ctx: ZCodeParser.Param_listContext):
        pass

    def visitParam_prime(self,ctx: ZCodeParser.Param_primeContext):
        pass

    def visitParam(self,ctx: ZCodeParser.ParamContext):
        pass

    def visitNon_rel_operators(self,ctx:ZCodeParser.Non_rel_operatorsContext):
        pass

    def visitNon_str_operators(self,ctx: ZCodeParser.Non_str_operatorsContext):
        pass

    def visitNon_associative_operands(self,ctx: ZCodeParser.Non_associative_operandsContext):
        pass

    def visitTyp(self,ctx:ZCodeParser.TypContext):
        pass

    def visitLiteral(self, ctx: ZCodeParser.LiteralContext):
        pass

    def visitMul_operators(self,ctx: ZCodeParser.Mul_operatorsContext):
        pass

    def visitAdd_operators(self,ctx: ZCodeParser.Add_operatorsContext):
        pass

    def visitLogic_operators(self, ctx: ZCodeParser.Logic_operatorsContext):
        pass

    def visitRel_operators(self, ctx: ZCodeParser.Rel_operatorsContext):
        pass

    def visitStr_operators(self, ctx: ZCodeParser.Str_operatorsContext):
        pass

    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext):
        pass

    def visitParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        pass

    def visitParam_decl_prime(self, ctx:ZCodeParser.Param_decl_primeContext):
        pass

    def visitParam_single_decl(self, ctx:ZCodeParser.Param_single_declContext):
        pass

    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass

    def visitBody(self,ctx:ZCodeParser.BodyContext):
        pass

    def visitStatement_block(self, ctx: ZCodeParser.Statement_blockContext):
        pass

    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass
    
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
        pass

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

    # lhs: 
    # 	IDENTIFIER
    # 	|
    # 	expression OPEN_BRACKET index_operators CLOSE_BRACKET
    # ;
    def visitLhs(self,ctx:ZCodeParser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            arr = self.visit(ctx.expression())
            idx = self.visit(ctx.index_operators())
            return ArrayCell(arr,idx)

    #rhs: expression;
    def visitRhs(self,ctx:ZCodeParser.RhsContext):
        return self.visit(ctx.expression())

    #if_statement: IF OPEN_PARENTHESIS expression CLOSE_PARENTHESIS if_body elif_statement_list else_statement newline_list;
    def visitIf_statement(self,ctx:ZCodeParser.If_statementContext):
        expr = self.visit(ctx.expression())
        thenStmt = self.visit(ctx.if_body())        
        elifStmt = self.visit(ctx.elif_statement_list())
        elseStmt = self.visit(ctx.else_statement())
        if len(elseStmt) == 0:
            return If(expr,thenStmt,elifStmt,None)
        else:
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
            return []

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
        if ctx.getChildCount == 0:
            return []
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
        elif ctx.statement_block:
            return self.visit(ctx.statement_block())
        else:
            return []
    
    #break_statement: BREAK_STATEMENT NEWLINE newline_list;
    def visitBreak_statement(self,ctx:ZCodeParser.Break_statementContext):
        return Break()

    #continue_statement: CONTINUE_STATEMENT NEWLINE newline_list;
    def visitContinue_statement(self,ctx:ZCodeParser.Continue_statementContext):
        return Continue()

