# Generated from SenCosTan.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,71,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,66,8,2,10,2,12,2,69,9,2,1,2,0,1,4,3,
        0,2,4,0,2,2,0,9,9,11,11,2,0,10,10,12,12,85,0,7,1,0,0,0,2,20,1,0,
        0,0,4,53,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,
        9,10,1,0,0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,21,0,0,13,21,1,0,
        0,0,14,15,5,18,0,0,15,16,5,1,0,0,16,17,3,4,2,0,17,18,5,21,0,0,18,
        21,1,0,0,0,19,21,5,21,0,0,20,11,1,0,0,0,20,14,1,0,0,0,20,19,1,0,
        0,0,21,3,1,0,0,0,22,23,6,2,-1,0,23,24,5,14,0,0,24,25,5,2,0,0,25,
        26,3,4,2,0,26,27,5,3,0,0,27,54,1,0,0,0,28,29,5,15,0,0,29,30,5,2,
        0,0,30,31,3,4,2,0,31,32,5,3,0,0,32,54,1,0,0,0,33,34,5,16,0,0,34,
        35,5,2,0,0,35,36,3,4,2,0,36,37,5,3,0,0,37,54,1,0,0,0,38,54,5,19,
        0,0,39,54,5,4,0,0,40,54,5,20,0,0,41,54,5,13,0,0,42,43,5,17,0,0,43,
        54,3,4,2,7,44,54,5,18,0,0,45,46,5,2,0,0,46,47,3,4,2,0,47,48,5,3,
        0,0,48,54,1,0,0,0,49,50,5,7,0,0,50,54,3,4,2,2,51,52,5,8,0,0,52,54,
        3,4,2,1,53,22,1,0,0,0,53,28,1,0,0,0,53,33,1,0,0,0,53,38,1,0,0,0,
        53,39,1,0,0,0,53,40,1,0,0,0,53,41,1,0,0,0,53,42,1,0,0,0,53,44,1,
        0,0,0,53,45,1,0,0,0,53,49,1,0,0,0,53,51,1,0,0,0,54,67,1,0,0,0,55,
        56,10,16,0,0,56,57,7,0,0,0,57,66,3,4,2,17,58,59,10,15,0,0,59,60,
        7,1,0,0,60,66,3,4,2,16,61,62,10,4,0,0,62,66,5,5,0,0,63,64,10,3,0,
        0,64,66,5,6,0,0,65,55,1,0,0,0,65,58,1,0,0,0,65,61,1,0,0,0,65,63,
        1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,5,1,0,0,0,69,
        67,1,0,0,0,5,9,20,53,65,67
    ]

class SenCosTanParser ( Parser ):

    grammarFileName = "SenCosTan.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'pi'", "'++'", "'--'", 
                     "'-'", "'+'", "' * '", "' + '", "' / '", "' - '", "<INVALID>", 
                     "'Sin'", "'Cos'", "'Tan'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MUL", "ADD", "DIV", "SUB", "BOOLEAN", 
                      "SIN", "COS", "TAN", "BOOL_NEG", "ID", "INT", "FLOAT", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    MUL=9
    ADD=10
    DIV=11
    SUB=12
    BOOLEAN=13
    SIN=14
    COS=15
    TAN=16
    BOOL_NEG=17
    ID=18
    INT=19
    FLOAT=20
    NEWLINE=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SenCosTanParser.StatContext)
            else:
                return self.getTypedRuleContext(SenCosTanParser.StatContext,i)


        def getRuleIndex(self):
            return SenCosTanParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SenCosTanParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4186516) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SenCosTanParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(SenCosTanParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(SenCosTanParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SenCosTanParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(SenCosTanParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = SenCosTanParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = SenCosTanParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(SenCosTanParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = SenCosTanParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(SenCosTanParser.ID)
                self.state = 15
                self.match(SenCosTanParser.T__0)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(SenCosTanParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = SenCosTanParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(SenCosTanParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SenCosTanParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(SenCosTanParser.TAN, 0)
        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTan" ):
                listener.enterTan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTan" ):
                listener.exitTan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTan" ):
                return visitor.visitTan(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SenCosTanParser.ExprContext)
            else:
                return self.getTypedRuleContext(SenCosTanParser.ExprContext,i)

        def MUL(self):
            return self.getToken(SenCosTanParser.MUL, 0)
        def DIV(self):
            return self.getToken(SenCosTanParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SenCosTanParser.ExprContext)
            else:
                return self.getTypedRuleContext(SenCosTanParser.ExprContext,i)

        def ADD(self):
            return self.getToken(SenCosTanParser.ADD, 0)
        def SUB(self):
            return self.getToken(SenCosTanParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class CosContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(SenCosTanParser.COS, 0)
        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCos" ):
                listener.enterCos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCos" ):
                listener.exitCos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCos" ):
                return visitor.visitCos(self)
            else:
                return visitor.visitChildren(self)


    class BoolNegacionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_NEG(self):
            return self.getToken(SenCosTanParser.BOOL_NEG, 0)
        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolNegacion" ):
                listener.enterBoolNegacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolNegacion" ):
                listener.exitBoolNegacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolNegacion" ):
                return visitor.visitBoolNegacion(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(SenCosTanParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SenCosTanParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class PositivoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositivo" ):
                listener.enterPositivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositivo" ):
                listener.exitPositivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositivo" ):
                return visitor.visitPositivo(self)
            else:
                return visitor.visitChildren(self)


    class SinContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(SenCosTanParser.SIN, 0)
        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin" ):
                listener.enterSin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin" ):
                listener.exitSin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSin" ):
                return visitor.visitSin(self)
            else:
                return visitor.visitChildren(self)


    class PiContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPi" ):
                listener.enterPi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPi" ):
                listener.exitPi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPi" ):
                return visitor.visitPi(self)
            else:
                return visitor.visitChildren(self)


    class DecrementoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecremento" ):
                listener.enterDecremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecremento" ):
                listener.exitDecremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecremento" ):
                return visitor.visitDecremento(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SenCosTanParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(SenCosTanParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class IncrementoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncremento" ):
                listener.enterIncremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncremento" ):
                listener.exitIncremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncremento" ):
                return visitor.visitIncremento(self)
            else:
                return visitor.visitChildren(self)


    class NegativoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SenCosTanParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SenCosTanParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativo" ):
                listener.enterNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativo" ):
                listener.exitNegativo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegativo" ):
                return visitor.visitNegativo(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SenCosTanParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = SenCosTanParser.SinContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(SenCosTanParser.SIN)
                self.state = 24
                self.match(SenCosTanParser.T__1)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(SenCosTanParser.T__2)
                pass
            elif token in [15]:
                localctx = SenCosTanParser.CosContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(SenCosTanParser.COS)
                self.state = 29
                self.match(SenCosTanParser.T__1)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(SenCosTanParser.T__2)
                pass
            elif token in [16]:
                localctx = SenCosTanParser.TanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(SenCosTanParser.TAN)
                self.state = 34
                self.match(SenCosTanParser.T__1)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(SenCosTanParser.T__2)
                pass
            elif token in [19]:
                localctx = SenCosTanParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(SenCosTanParser.INT)
                pass
            elif token in [4]:
                localctx = SenCosTanParser.PiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(SenCosTanParser.T__3)
                pass
            elif token in [20]:
                localctx = SenCosTanParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(SenCosTanParser.FLOAT)
                pass
            elif token in [13]:
                localctx = SenCosTanParser.BooleanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(SenCosTanParser.BOOLEAN)
                pass
            elif token in [17]:
                localctx = SenCosTanParser.BoolNegacionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(SenCosTanParser.BOOL_NEG)
                self.state = 43
                self.expr(7)
                pass
            elif token in [18]:
                localctx = SenCosTanParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(SenCosTanParser.ID)
                pass
            elif token in [2]:
                localctx = SenCosTanParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(SenCosTanParser.T__1)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(SenCosTanParser.T__2)
                pass
            elif token in [7]:
                localctx = SenCosTanParser.NegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(SenCosTanParser.T__6)
                self.state = 50
                self.expr(2)
                pass
            elif token in [8]:
                localctx = SenCosTanParser.PositivoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(SenCosTanParser.T__7)
                self.state = 52
                self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 65
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SenCosTanParser.MulDivContext(self, SenCosTanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = SenCosTanParser.AddSubContext(self, SenCosTanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = SenCosTanParser.IncrementoContext(self, SenCosTanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 62
                        self.match(SenCosTanParser.T__4)
                        pass

                    elif la_ == 4:
                        localctx = SenCosTanParser.DecrementoContext(self, SenCosTanParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        self.match(SenCosTanParser.T__5)
                        pass

             
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




