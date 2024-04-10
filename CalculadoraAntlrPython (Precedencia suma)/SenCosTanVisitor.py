# Generated from SenCosTan.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SenCosTanParser import SenCosTanParser
else:
    from SenCosTanParser import SenCosTanParser

# This class defines a complete generic visitor for a parse tree produced by SenCosTanParser.

class SenCosTanVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SenCosTanParser#prog.
    def visitProg(self, ctx:SenCosTanParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#print.
    def visitPrint(self, ctx:SenCosTanParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#assign.
    def visitAssign(self, ctx:SenCosTanParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#blank.
    def visitBlank(self, ctx:SenCosTanParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Tan.
    def visitTan(self, ctx:SenCosTanParser.TanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#parens.
    def visitParens(self, ctx:SenCosTanParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#AddSub.
    def visitAddSub(self, ctx:SenCosTanParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#MulDiv.
    def visitMulDiv(self, ctx:SenCosTanParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Cos.
    def visitCos(self, ctx:SenCosTanParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#BoolNegacion.
    def visitBoolNegacion(self, ctx:SenCosTanParser.BoolNegacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#float.
    def visitFloat(self, ctx:SenCosTanParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#int.
    def visitInt(self, ctx:SenCosTanParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Positivo.
    def visitPositivo(self, ctx:SenCosTanParser.PositivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Sin.
    def visitSin(self, ctx:SenCosTanParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#pi.
    def visitPi(self, ctx:SenCosTanParser.PiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Decremento.
    def visitDecremento(self, ctx:SenCosTanParser.DecrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#id.
    def visitId(self, ctx:SenCosTanParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Boolean.
    def visitBoolean(self, ctx:SenCosTanParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Incremento.
    def visitIncremento(self, ctx:SenCosTanParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SenCosTanParser#Negativo.
    def visitNegativo(self, ctx:SenCosTanParser.NegativoContext):
        return self.visitChildren(ctx)



del SenCosTanParser