# Generated from Eson.g4 by ANTLR 4.13.1
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
        4,1,22,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,2,42,9,2,
        3,2,44,8,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,52,8,3,10,3,12,3,55,9,3,3,
        3,57,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,
        72,8,6,10,6,12,6,75,9,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,2,0,12,12,
        19,19,88,0,14,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,47,1,0,0,0,8,60,
        1,0,0,0,10,64,1,0,0,0,12,68,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,
        16,1,1,0,0,0,17,33,1,0,0,0,18,33,5,9,0,0,19,33,5,10,0,0,20,33,5,
        11,0,0,21,33,5,12,0,0,22,33,5,13,0,0,23,33,5,14,0,0,24,33,5,15,0,
        0,25,33,5,16,0,0,26,33,5,17,0,0,27,33,5,18,0,0,28,33,5,19,0,0,29,
        33,3,4,2,0,30,33,3,6,3,0,31,33,3,10,5,0,32,17,1,0,0,0,32,18,1,0,
        0,0,32,19,1,0,0,0,32,20,1,0,0,0,32,21,1,0,0,0,32,22,1,0,0,0,32,23,
        1,0,0,0,32,24,1,0,0,0,32,25,1,0,0,0,32,26,1,0,0,0,32,27,1,0,0,0,
        32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,
        0,0,34,43,5,1,0,0,35,40,3,2,1,0,36,37,5,2,0,0,37,39,3,2,1,0,38,36,
        1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,44,1,0,0,0,
        42,40,1,0,0,0,43,35,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,
        3,0,0,46,5,1,0,0,0,47,56,5,4,0,0,48,53,3,8,4,0,49,50,5,2,0,0,50,
        52,3,8,4,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,
        0,54,57,1,0,0,0,55,53,1,0,0,0,56,48,1,0,0,0,56,57,1,0,0,0,57,58,
        1,0,0,0,58,59,5,5,0,0,59,7,1,0,0,0,60,61,7,0,0,0,61,62,5,6,0,0,62,
        63,3,2,1,0,63,9,1,0,0,0,64,65,5,7,0,0,65,66,3,12,6,0,66,67,5,8,0,
        0,67,11,1,0,0,0,68,73,3,2,1,0,69,70,5,20,0,0,70,72,3,2,1,0,71,69,
        1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,13,1,0,0,0,
        75,73,1,0,0,0,6,32,40,43,53,56,73
    ]

class EsonParser ( Parser ):

    grammarFileName = "Eson.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "'{'", "'}'", "'='", 
                     "'('", "')'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTEGER", "FLOAT", "CHAR", "STRING", 
                      "DATE", "TIME", "DATETIME", "DURATION", "BOOL", "NULL", 
                      "SYMBOL", "MATH_OPERATOR", "WS", "COMMENT" ]

    RULE_esonDocument = 0
    RULE_esonValue = 1
    RULE_list = 2
    RULE_dictionary = 3
    RULE_dictEntry = 4
    RULE_mathExpression = 5
    RULE_mathOperation = 6

    ruleNames =  [ "esonDocument", "esonValue", "list", "dictionary", "dictEntry", 
                   "mathExpression", "mathOperation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INTEGER=9
    FLOAT=10
    CHAR=11
    STRING=12
    DATE=13
    TIME=14
    DATETIME=15
    DURATION=16
    BOOL=17
    NULL=18
    SYMBOL=19
    MATH_OPERATOR=20
    WS=21
    COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EsonDocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def esonValue(self):
            return self.getTypedRuleContext(EsonParser.EsonValueContext,0)


        def EOF(self):
            return self.getToken(EsonParser.EOF, 0)

        def getRuleIndex(self):
            return EsonParser.RULE_esonDocument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEsonDocument" ):
                listener.enterEsonDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEsonDocument" ):
                listener.exitEsonDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEsonDocument" ):
                return visitor.visitEsonDocument(self)
            else:
                return visitor.visitChildren(self)




    def esonDocument(self):

        localctx = EsonParser.EsonDocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_esonDocument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.esonValue()
            self.state = 15
            self.match(EsonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EsonValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(EsonParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(EsonParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(EsonParser.CHAR, 0)

        def STRING(self):
            return self.getToken(EsonParser.STRING, 0)

        def DATE(self):
            return self.getToken(EsonParser.DATE, 0)

        def TIME(self):
            return self.getToken(EsonParser.TIME, 0)

        def DATETIME(self):
            return self.getToken(EsonParser.DATETIME, 0)

        def DURATION(self):
            return self.getToken(EsonParser.DURATION, 0)

        def BOOL(self):
            return self.getToken(EsonParser.BOOL, 0)

        def NULL(self):
            return self.getToken(EsonParser.NULL, 0)

        def SYMBOL(self):
            return self.getToken(EsonParser.SYMBOL, 0)

        def list_(self):
            return self.getTypedRuleContext(EsonParser.ListContext,0)


        def dictionary(self):
            return self.getTypedRuleContext(EsonParser.DictionaryContext,0)


        def mathExpression(self):
            return self.getTypedRuleContext(EsonParser.MathExpressionContext,0)


        def getRuleIndex(self):
            return EsonParser.RULE_esonValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEsonValue" ):
                listener.enterEsonValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEsonValue" ):
                listener.exitEsonValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEsonValue" ):
                return visitor.visitEsonValue(self)
            else:
                return visitor.visitChildren(self)




    def esonValue(self):

        localctx = EsonParser.EsonValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_esonValue)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 2, 3, 5, 8, 20]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(EsonParser.INTEGER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(EsonParser.FLOAT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(EsonParser.CHAR)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 21
                self.match(EsonParser.STRING)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 22
                self.match(EsonParser.DATE)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 23
                self.match(EsonParser.TIME)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 8)
                self.state = 24
                self.match(EsonParser.DATETIME)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 9)
                self.state = 25
                self.match(EsonParser.DURATION)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 10)
                self.state = 26
                self.match(EsonParser.BOOL)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 11)
                self.state = 27
                self.match(EsonParser.NULL)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 12)
                self.state = 28
                self.match(EsonParser.SYMBOL)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 13)
                self.state = 29
                self.list_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 14)
                self.state = 30
                self.dictionary()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 15)
                self.state = 31
                self.mathExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def esonValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsonParser.EsonValueContext)
            else:
                return self.getTypedRuleContext(EsonParser.EsonValueContext,i)


        def getRuleIndex(self):
            return EsonParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = EsonParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(EsonParser.T__0)
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 35
                self.esonValue()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 36
                    self.match(EsonParser.T__1)
                    self.state = 37
                    self.esonValue()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 45
            self.match(EsonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictionaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dictEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsonParser.DictEntryContext)
            else:
                return self.getTypedRuleContext(EsonParser.DictEntryContext,i)


        def getRuleIndex(self):
            return EsonParser.RULE_dictionary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary" ):
                listener.enterDictionary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary" ):
                listener.exitDictionary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionary" ):
                return visitor.visitDictionary(self)
            else:
                return visitor.visitChildren(self)




    def dictionary(self):

        localctx = EsonParser.DictionaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dictionary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(EsonParser.T__3)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==19:
                self.state = 48
                self.dictEntry()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 49
                    self.match(EsonParser.T__1)
                    self.state = 50
                    self.dictEntry()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 58
            self.match(EsonParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def esonValue(self):
            return self.getTypedRuleContext(EsonParser.EsonValueContext,0)


        def STRING(self):
            return self.getToken(EsonParser.STRING, 0)

        def SYMBOL(self):
            return self.getToken(EsonParser.SYMBOL, 0)

        def getRuleIndex(self):
            return EsonParser.RULE_dictEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictEntry" ):
                listener.enterDictEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictEntry" ):
                listener.exitDictEntry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictEntry" ):
                return visitor.visitDictEntry(self)
            else:
                return visitor.visitChildren(self)




    def dictEntry(self):

        localctx = EsonParser.DictEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dictEntry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==12 or _la==19):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 61
            self.match(EsonParser.T__5)
            self.state = 62
            self.esonValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mathOperation(self):
            return self.getTypedRuleContext(EsonParser.MathOperationContext,0)


        def getRuleIndex(self):
            return EsonParser.RULE_mathExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathExpression" ):
                listener.enterMathExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathExpression" ):
                listener.exitMathExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathExpression" ):
                return visitor.visitMathExpression(self)
            else:
                return visitor.visitChildren(self)




    def mathExpression(self):

        localctx = EsonParser.MathExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mathExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(EsonParser.T__6)
            self.state = 65
            self.mathOperation()
            self.state = 66
            self.match(EsonParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def esonValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsonParser.EsonValueContext)
            else:
                return self.getTypedRuleContext(EsonParser.EsonValueContext,i)


        def MATH_OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(EsonParser.MATH_OPERATOR)
            else:
                return self.getToken(EsonParser.MATH_OPERATOR, i)

        def getRuleIndex(self):
            return EsonParser.RULE_mathOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathOperation" ):
                listener.enterMathOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathOperation" ):
                listener.exitMathOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOperation" ):
                return visitor.visitMathOperation(self)
            else:
                return visitor.visitChildren(self)




    def mathOperation(self):

        localctx = EsonParser.MathOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mathOperation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.esonValue()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 69
                self.match(EsonParser.MATH_OPERATOR)
                self.state = 70
                self.esonValue()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





