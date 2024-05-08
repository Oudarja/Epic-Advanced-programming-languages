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
        4,1,19,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,28,8,1,
        1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,3,2,39,8,2,1,2,1,2,1,
        3,1,3,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,3,3,52,8,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,1,2,0,10,10,17,17,71,0,10,1,0,
        0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,42,1,0,0,0,8,55,1,0,0,0,10,11,3,
        2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,28,1,0,0,0,14,28,5,7,0,0,15,
        28,5,8,0,0,16,28,5,9,0,0,17,28,5,10,0,0,18,28,5,11,0,0,19,28,5,12,
        0,0,20,28,5,13,0,0,21,28,5,14,0,0,22,28,5,15,0,0,23,28,5,16,0,0,
        24,28,5,17,0,0,25,28,3,4,2,0,26,28,3,6,3,0,27,13,1,0,0,0,27,14,1,
        0,0,0,27,15,1,0,0,0,27,16,1,0,0,0,27,17,1,0,0,0,27,18,1,0,0,0,27,
        19,1,0,0,0,27,20,1,0,0,0,27,21,1,0,0,0,27,22,1,0,0,0,27,23,1,0,0,
        0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,38,5,
        1,0,0,30,35,3,2,1,0,31,32,5,2,0,0,32,34,3,2,1,0,33,31,1,0,0,0,34,
        37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,
        0,38,30,1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,41,5,3,0,0,41,5,1,
        0,0,0,42,51,5,4,0,0,43,48,3,8,4,0,44,45,5,2,0,0,45,47,3,8,4,0,46,
        44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,52,1,0,0,
        0,50,48,1,0,0,0,51,43,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,
        5,5,0,0,54,7,1,0,0,0,55,56,7,0,0,0,56,57,5,6,0,0,57,58,3,2,1,0,58,
        9,1,0,0,0,5,27,35,38,48,51
    ]

class EsonParser ( Parser ):

    grammarFileName = "Eson.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "'{'", "'}'", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INTEGER", 
                      "FLOAT", "CHAR", "STRING", "DATE", "TIME", "DATETIME", 
                      "DURATION", "BOOL", "NULL", "SYMBOL", "WS", "COMMENT" ]

    RULE_esonDocument = 0
    RULE_esonValue = 1
    RULE_list = 2
    RULE_dictionary = 3
    RULE_dictEntry = 4

    ruleNames =  [ "esonDocument", "esonValue", "list", "dictionary", "dictEntry" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INTEGER=7
    FLOAT=8
    CHAR=9
    STRING=10
    DATE=11
    TIME=12
    DATETIME=13
    DURATION=14
    BOOL=15
    NULL=16
    SYMBOL=17
    WS=18
    COMMENT=19

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
            self.state = 10
            self.esonValue()
            self.state = 11
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
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 2, 3, 5]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(EsonParser.INTEGER)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(EsonParser.FLOAT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 16
                self.match(EsonParser.CHAR)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 17
                self.match(EsonParser.STRING)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 18
                self.match(EsonParser.DATE)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 7)
                self.state = 19
                self.match(EsonParser.TIME)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 8)
                self.state = 20
                self.match(EsonParser.DATETIME)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 9)
                self.state = 21
                self.match(EsonParser.DURATION)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 10)
                self.state = 22
                self.match(EsonParser.BOOL)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 11)
                self.state = 23
                self.match(EsonParser.NULL)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 12)
                self.state = 24
                self.match(EsonParser.SYMBOL)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 13)
                self.state = 25
                self.list_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 14)
                self.state = 26
                self.dictionary()
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
            self.state = 29
            self.match(EsonParser.T__0)
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 30
                self.esonValue()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 31
                    self.match(EsonParser.T__1)
                    self.state = 32
                    self.esonValue()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 40
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
            self.state = 42
            self.match(EsonParser.T__3)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==17:
                self.state = 43
                self.dictEntry()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 44
                    self.match(EsonParser.T__1)
                    self.state = 45
                    self.dictEntry()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 53
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
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==10 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.match(EsonParser.T__5)
            self.state = 57
            self.esonValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





