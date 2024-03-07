from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


#MODIFY THIS FILE TO GENERATE PARSE TREE

class ASTGeneration(ZCodeVisitor):

    #program: newline_list decllist EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        decl = self.visit(ctx.decllist())
        return Program(decl)
    
    #decllist:  decl decllist | decl ;   
    def visitDecllist(self,ctx: ZCodeParser.DecllistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        else:
            return [self.visit(ctx.decl())] + self.visit(ctx.decllist())

    #decl: vardecl | funcdecl ;
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        else: return None

    # vardecl: 
    # 	vardecl_only
    # 	|
    # 	vardecl_init
    # ;
    def visitVardecl(self,ctx:ZCodeParser.VardeclContext):
        if ctx.vardecl_only():
            return self.visit(ctx.vardecl_only())
        elif ctx.vardecl_init():
            return self.visit(ctx.vardecl_init())
        else: return None

    # vardecl_only:	
    # 	typ IDENTIFIER NEWLINE newline_list
    # 	|
    # 	DYNAMIC_TYPE IDENTIFIER NEWLINE newline_list
    # 	|
    # 	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET NEWLINE newline_list
    # ;
    def visitVardecl_only(self,ctx:ZCodeParser.Vardecl_onlyContext):
        if ctx.OPEN_BRACKET():
            name = Id(ctx.IDENTIFIER().getText())
            size = self.visit(ctx.arrlist())
            eleType = self.visit(ctx.typ())
            varType = ArrayType(size,eleType)
            return VarDecl(name,varType,None,None)
        elif ctx.DYNAMIC_TYPE():
            name = Id(ctx.IDENTIFIER().getText())
            modifier = ctx.DYNAMIC_TYPE().getText()
            return VarDecl(name,None,modifier,None)
        else:
            name = Id(ctx.IDENTIFIER().getText())
            varType = self.visit(ctx.typ())
            return VarDecl(name,varType,None,None)

    # vardecl_init:
    # 	//Declaration with initialization value
    # 	VAR_TYPE IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
    # 	|
    # 	typ IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
    # 	|
    # 	DYNAMIC_TYPE IDENTIFIER ASSIGN_OPERATOR expression NEWLINE newline_list
    # 	|
    # 	//Array declaration with initialization values
    # 	typ IDENTIFIER OPEN_BRACKET arrlist CLOSE_BRACKET ASSIGN_OPERATOR expression NEWLINE newline_list
    # ;
    def visitVardecl_init(self,ctx:ZCodeParser.Vardecl_initContext):
        if ctx.arrlist():
            name = Id(ctx.IDENTIFIER().getText())
            size = self.visit(ctx.arrlist())
            eleType = self.visit(ctx.typ())
            varType = ArrayType(size,eleType)
            varInit = self.visit(ctx.expression())
            return VarDecl(name,varType,None,varInit)
        elif ctx.DYNAMIC_TYPE():
            name = Id(ctx.IDENTIFIER().getText())
            modifier = ctx.DYNAMIC_TYPE().getText()
            varInit = self.visit(ctx.expression())
            return VarDecl(name,None,modifier,varInit)
        elif ctx.VAR_TYPE():
            name = Id(ctx.IDENTIFIER().getText())
            modifier = ctx.VAR_TYPE().getText()
            varInit = self.visit(ctx.expression())
            return VarDecl(name,None,modifier,varInit)
        else:
            name = Id(ctx.IDENTIFIER().getText())
            varType = self.visit(ctx.typ())
            varInit = self.visit(ctx.expression())
            return VarDecl(name,varType,None,varInit)

    #arrlist: NUMBER COMMA arrlist | NUMBER;
    def visitArrlist(self, ctx:ZCodeParser.ArrlistContext):
        if ctx.getChildCount() == 1:
            value = float(ctx.NUMBER().getText())
            return [value]
        else:
            value = float(ctx.NUMBER().getText())
            return [value] + self.visit(ctx.arrlist())

    #OBSOLETE
    #array_expression: OPEN_BRACKET arrlist CLOSE_BRACKET | arrlist;
    def visitArray_expression(self,ctx:ZCodeParser.Array_expressionContext):
        return None

    #OBSOLETE
    #arrlist_expression: OPEN_BRACKET array_expression COMMA arrlist_expression CLOSE_BRACKET | array_expression;
    def visitArrlist_expression(self,ctx:ZCodeParser.Arrlist_expressionContext):
        return None

    #array_literal: OPEN_BRACKET array_literal_prime CLOSE_BRACKET | OPEN_BRACKET CLOSE_BRACKET;
    def visitArray_literal(self,ctx:ZCodeParser.Array_literalContext):
        if ctx.array_literal_prime():
            value = self.visit(ctx.array_literal_prime())
            return ArrayLiteral(value)
        else:
            return ArrayLiteral([])

    #array_literal_prime: expression COMMA array_literal_prime | expression;
    def visitArray_literal_prime(self,ctx:ZCodeParser.Array_literal_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.array_literal_prime())

    # expression: 
    # 	expression OPEN_BRACKET index_operators CLOSE_BRACKET	
    #   |
    #   IDENTIFIER OPEN_BRACKET index_operators CLOSE_BRACKET
    #   |
    #   func_call OPEN_BRACKET index_operators CLOSE_BRACKET
    # 	|
    # 	OPEN_PARENTHESIS expression CLOSE_PARENTHESIS
    # 	|
    # 	<assoc=right>SUB_OPERATOR expression
    # 	|
    # 	<assoc=right>NOT_OPERATOR expression
    # 	|
    # 	expression mul_operators expression
    # 	|
    # 	expression add_operators expression
    # 	|
    # 	expression logic_operators expression
    # 	|
    # 	expression rel_operators expression
    # 	|
    # 	expression str_operators expression
    # 	|
    # 	IDENTIFIER OPEN_PARENTHESIS  param_list CLOSE_PARENTHESIS
    # 	|
    # 	literal
    # 	|
    # 	array_literal
    # ;
    def visitExpression(self,ctx:ZCodeParser.ExpressionContext):
        if ctx.index_operators():
            arr = self.visit(ctx.expression())
            idx = self.visit(index_operators())
            # print("expression with index operators is called")
            return ArrayCell(arr,idx)
        
        elif ctx.OPEN_PARENTHESIS():
            return self.visit(ctx.expression())
        
        elif ctx.SUB_OPERATOR():
            op = ctx.SUB_OPERATOR().getText()
            print("unary op is called" + op)
            operand = self.visit(ctx.expression())
            return UnaryOp(op,operand)
        
        elif ctx.NOT_OPERATOR():
            op = ctx.NOT_OPERATOR().getText()
            operand = self.visit(ctx.expression())
            return UnaryOp(op,operand)
        
        elif ctx.mul_operators():
            op = self.visit(ctx.mul_operators())
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return BinaryOp(op,left,right)
        
        elif ctx.add_operators():
            op = self.visit(ctx.add_operators())
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return BinaryOp(op,left,right)
        
        elif ctx.logic_operators():
            op = self.visit(ctx.logic_operators())
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return BinaryOp(op,left,right)
        
        elif ctx.rel_operators():
            op = self.visit(ctx.rel_operators())
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return BinaryOp(op,left,right)

        elif ctx.str_operators():
            op = self.visit(ctx.str_operators())
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            return BinaryOp(op,left,right)
        
        elif ctx.param_list():
            name = Id(ctx.IDENTIFIER().getText())
            args = self.visit(ctx.param_list())
            return CallExpr(name,args)
        
        elif ctx.literal():
            return self.visit(ctx.literal())
        
        elif ctx.array_literal():
            # print("array literal is called")
            return self.visit(ctx.array_literal())
        
        else: return None

    #sign_operands: literal | SUB_OPERATOR ;
    def visitSign_operands(self,ctx:ZCodeParser.Sign_operandsContext):
        if ctx.SUB_OPERATOR():
            return ctx.SUB_OPERATOR().getText()
        else: return self.visit(ctx.literal())

    #not_operands: literal | NOT_OPERATOR;
    def visitNot_operands(self, ctx:ZCodeParser.Not_operandsContext):
        if ctx.NOT_OPERATOR():
            return ctx.NOT_OPERATOR().getText()
        else: return self.visit(ctx.literal())

    #index_operators: expression | expression COMMA index_operators;
    def visitIndex_operators(self,ctx:ZCodeParser.Index_operatorsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        else:
            return [self.visit(ctx.expression())] + self.visit(ctx.index_operators())

    #func_call: IDENTIFIER OPEN_PARENTHESIS  param_list CLOSE_PARENTHESIS;
    def visitFunc_call(self,ctx: ZCodeParser.Func_callContext):
        name = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.param_list())
        return CallStmt(name,args)

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
        return None

    #THIS IS OBSOLETE
    def visitNon_str_operators(self,ctx: ZCodeParser.Non_str_operatorsContext):
        return None

    #THIS IS OBSOLETE
    def visitNon_associative_operands(self,ctx: ZCodeParser.Non_associative_operandsContext):
        return None

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
        param = self.visit(ctx.param_decl_list())
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

