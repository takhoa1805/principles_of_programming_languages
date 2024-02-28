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

    def visitStatement(self,ctx:ZCodeParser.StatementContext):
        pass

    def visitRet(self,ctx:ZCodeParser.RetContext):
        pass

    def visitReturn_statement(self,ctx:ZCodeParser.Return_statementContext):
        pass

    def visitFunc_call_statement(self,ctx:ZCodeParser.Func_call_statementContext):
        pass

    def visitAssignment_statement(self,ctx: ZCodeParser.Assignment_statementContext):
        pass

    def visitLhs(self,ctx:ZCodeParser.LhsContext):
        pass

    def visitRhs(self,ctx:ZCodeParser.RhsContext):
        pass

    def visitIf_statement(self,ctx:ZCodeParser.If_statementContext):
        pass

    def visitIf_body(self,ctx:ZCodeParser.If_bodyContext):
        pass

    def visitElif_statement_list(self,ctx:ZCodeParser.Elif_statement_listContext):
        pass

    def visitElif_statement(self,ctx:ZCodeParser.Elif_statementContext):
        pass

    def visitElse_statement(self,ctx:ZCodeParser.Else_statementContext):
        pass

    def visitFor_statement(self,ctx:ZCodeParser.For_statementContext):
        pass

    def visitFor_body(self,ctx:ZCodeParser.For_bodyContext):
        pass

    def visitBreak_statement(self,ctx:ZCodeParser.Break_statementContext):
        pass

    def visitContinue_statement(self,ctx:ZCodeParser.Continue_statementContext):
        pass

