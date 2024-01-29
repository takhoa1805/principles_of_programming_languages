# Generated from c://Users//takho//Desktop//principles_of_programming_languages//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ZCodeParser#arrlist.
    def enterArrlist(self, ctx:ZCodeParser.ArrlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrlist.
    def exitArrlist(self, ctx:ZCodeParser.ArrlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrexp.
    def enterArrexp(self, ctx:ZCodeParser.ArrexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrexp.
    def exitArrexp(self, ctx:ZCodeParser.ArrexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exp.
    def enterExp(self, ctx:ZCodeParser.ExpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exp.
    def exitExp(self, ctx:ZCodeParser.ExpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typ.
    def enterTyp(self, ctx:ZCodeParser.TypContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typ.
    def exitTyp(self, ctx:ZCodeParser.TypContext):
        pass



del ZCodeParser