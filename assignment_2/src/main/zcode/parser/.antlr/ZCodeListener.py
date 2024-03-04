# Generated from c://Users//takho//Desktop//principles_of_programming_languages//assignment_2//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decllist.
    def enterDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decllist.
    def exitDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl.
    def enterDecl(self, ctx:ZCodeParser.DeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl.
    def exitDecl(self, ctx:ZCodeParser.DeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl.
    def enterVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl.
    def exitVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl_only.
    def enterVardecl_only(self, ctx:ZCodeParser.Vardecl_onlyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl_only.
    def exitVardecl_only(self, ctx:ZCodeParser.Vardecl_onlyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl_init.
    def enterVardecl_init(self, ctx:ZCodeParser.Vardecl_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl_init.
    def exitVardecl_init(self, ctx:ZCodeParser.Vardecl_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrlist.
    def enterArrlist(self, ctx:ZCodeParser.ArrlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrlist.
    def exitArrlist(self, ctx:ZCodeParser.ArrlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_expression.
    def enterArray_expression(self, ctx:ZCodeParser.Array_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_expression.
    def exitArray_expression(self, ctx:ZCodeParser.Array_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrlist_expression.
    def enterArrlist_expression(self, ctx:ZCodeParser.Arrlist_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrlist_expression.
    def exitArrlist_expression(self, ctx:ZCodeParser.Arrlist_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_literal.
    def enterArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_literal.
    def exitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_literal_prime.
    def enterArray_literal_prime(self, ctx:ZCodeParser.Array_literal_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_literal_prime.
    def exitArray_literal_prime(self, ctx:ZCodeParser.Array_literal_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sign_operands.
    def enterSign_operands(self, ctx:ZCodeParser.Sign_operandsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sign_operands.
    def exitSign_operands(self, ctx:ZCodeParser.Sign_operandsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#not_operands.
    def enterNot_operands(self, ctx:ZCodeParser.Not_operandsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#not_operands.
    def exitNot_operands(self, ctx:ZCodeParser.Not_operandsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#index_operators.
    def enterIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_operators.
    def exitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_call.
    def enterFunc_call(self, ctx:ZCodeParser.Func_callContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_call.
    def exitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_list.
    def enterParam_list(self, ctx:ZCodeParser.Param_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_list.
    def exitParam_list(self, ctx:ZCodeParser.Param_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_prime.
    def enterParam_prime(self, ctx:ZCodeParser.Param_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_prime.
    def exitParam_prime(self, ctx:ZCodeParser.Param_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#non_rel_operators.
    def enterNon_rel_operators(self, ctx:ZCodeParser.Non_rel_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#non_rel_operators.
    def exitNon_rel_operators(self, ctx:ZCodeParser.Non_rel_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#non_str_operators.
    def enterNon_str_operators(self, ctx:ZCodeParser.Non_str_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#non_str_operators.
    def exitNon_str_operators(self, ctx:ZCodeParser.Non_str_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#non_associative_operands.
    def enterNon_associative_operands(self, ctx:ZCodeParser.Non_associative_operandsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#non_associative_operands.
    def exitNon_associative_operands(self, ctx:ZCodeParser.Non_associative_operandsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typ.
    def enterTyp(self, ctx:ZCodeParser.TypContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typ.
    def exitTyp(self, ctx:ZCodeParser.TypContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#mul_operators.
    def enterMul_operators(self, ctx:ZCodeParser.Mul_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#mul_operators.
    def exitMul_operators(self, ctx:ZCodeParser.Mul_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#add_operators.
    def enterAdd_operators(self, ctx:ZCodeParser.Add_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#add_operators.
    def exitAdd_operators(self, ctx:ZCodeParser.Add_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logic_operators.
    def enterLogic_operators(self, ctx:ZCodeParser.Logic_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logic_operators.
    def exitLogic_operators(self, ctx:ZCodeParser.Logic_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#rel_operators.
    def enterRel_operators(self, ctx:ZCodeParser.Rel_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#rel_operators.
    def exitRel_operators(self, ctx:ZCodeParser.Rel_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#str_operators.
    def enterStr_operators(self, ctx:ZCodeParser.Str_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#str_operators.
    def exitStr_operators(self, ctx:ZCodeParser.Str_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl_list.
    def enterParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl_list.
    def exitParam_decl_list(self, ctx:ZCodeParser.Param_decl_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl_prime.
    def enterParam_decl_prime(self, ctx:ZCodeParser.Param_decl_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl_prime.
    def exitParam_decl_prime(self, ctx:ZCodeParser.Param_decl_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_single_decl.
    def enterParam_single_decl(self, ctx:ZCodeParser.Param_single_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_single_decl.
    def exitParam_single_decl(self, ctx:ZCodeParser.Param_single_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newline_list.
    def enterNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newline_list.
    def exitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#body.
    def enterBody(self, ctx:ZCodeParser.BodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#body.
    def exitBody(self, ctx:ZCodeParser.BodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_block.
    def enterStatement_block(self, ctx:ZCodeParser.Statement_blockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_block.
    def exitStatement_block(self, ctx:ZCodeParser.Statement_blockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_list.
    def enterStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_list.
    def exitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ret.
    def enterRet(self, ctx:ZCodeParser.RetContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ret.
    def exitRet(self, ctx:ZCodeParser.RetContext):
        pass


    # Enter a parse tree produced by ZCodeParser#return_statement.
    def enterReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#return_statement.
    def exitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_call_statement.
    def enterFunc_call_statement(self, ctx:ZCodeParser.Func_call_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_call_statement.
    def exitFunc_call_statement(self, ctx:ZCodeParser.Func_call_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignment_statement.
    def enterAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignment_statement.
    def exitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#lhs.
    def enterLhs(self, ctx:ZCodeParser.LhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#lhs.
    def exitLhs(self, ctx:ZCodeParser.LhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#rhs.
    def enterRhs(self, ctx:ZCodeParser.RhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#rhs.
    def exitRhs(self, ctx:ZCodeParser.RhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_statement.
    def enterIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_statement.
    def exitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_body.
    def enterIf_body(self, ctx:ZCodeParser.If_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_body.
    def exitIf_body(self, ctx:ZCodeParser.If_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_statement_list.
    def enterElif_statement_list(self, ctx:ZCodeParser.Elif_statement_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_statement_list.
    def exitElif_statement_list(self, ctx:ZCodeParser.Elif_statement_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_statement.
    def enterElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_statement.
    def exitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#else_statement.
    def enterElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#else_statement.
    def exitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_statement.
    def enterFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_statement.
    def exitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_body.
    def enterFor_body(self, ctx:ZCodeParser.For_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_body.
    def exitFor_body(self, ctx:ZCodeParser.For_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_statement.
    def enterBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_statement.
    def exitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continue_statement.
    def enterContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continue_statement.
    def exitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass



del ZCodeParser