from SenCosTanVisitor import SenCosTanVisitor
from SenCosTanParser import SenCosTanParser
import math

class SenCosTanVisitorTest(SenCosTanVisitor):

    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        id_ = ctx.ID().getText()
        value = int(self.visit(ctx.expr()))
        self.memory[id_] = value
        return float(value)

    def visitProg(self, ctx):
        return super().visitProg(ctx)

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        if isinstance(value, bool):
            print(value)
        else:
            print("{:.2f}".format(value))  # Imprime con 2 decimales si el valor no es booleano
        return value

    def visitBlank(self, ctx):
        return super().visitBlank(ctx)

    def visitId(self, ctx):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return float(self.memory[id_])
        return 0.0

    def visitInt(self, ctx):
        return float(ctx.INT().getText())

    def visitPi(self, ctx):
        return math.pi

    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SenCosTanParser.ADD:
            return right + left
        return right - left

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SenCosTanParser.MUL:
            return right * left
        return right / left

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitSin(self, ctx):
        n = self.visit(ctx.expr())
        return math.sin(n)

    def visitCos(self, ctx):
        n = self.visit(ctx.expr())
        return math.cos(n)

    def visitTan(self, ctx):
        n = self.visit(ctx.expr())
        return math.tan(n)
    
    def VisitNeg(self, ctx):
        n = self.visit(ctx.expr())
        return -n
    
    def VisitPos(self, ctx):
        n = self.visit(ctx.expr())
        return n
    
    def visitIncremento(self, ctx):
        n = self.visit(ctx.expr())
        return n + 1

    def visitDecremento(self, ctx):
        n = self.visit(ctx.expr())
        return n - 1
        
    def visitBoolean(self, ctx):
        value = ctx.BOOLEAN().getText()
        return value.lower() == "true"
    
    def visitBoolNegacion(self, ctx):
        value = self.visit(ctx.expr())
        return not bool(value)

