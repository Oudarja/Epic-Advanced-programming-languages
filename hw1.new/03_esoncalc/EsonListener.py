# Generated from Eson.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EsonParser import EsonParser
else:
    from EsonParser import EsonParser

# This class defines a complete listener for a parse tree produced by EsonParser.
class EsonListener(ParseTreeListener):

    # Enter a parse tree produced by EsonParser#esonDocument.
    def enterEsonDocument(self, ctx:EsonParser.EsonDocumentContext):
        pass

    # Exit a parse tree produced by EsonParser#esonDocument.
    def exitEsonDocument(self, ctx:EsonParser.EsonDocumentContext):
        pass


    # Enter a parse tree produced by EsonParser#esonValue.
    def enterEsonValue(self, ctx:EsonParser.EsonValueContext):
        pass

    # Exit a parse tree produced by EsonParser#esonValue.
    def exitEsonValue(self, ctx:EsonParser.EsonValueContext):
        pass


    # Enter a parse tree produced by EsonParser#list.
    def enterList(self, ctx:EsonParser.ListContext):
        pass

    # Exit a parse tree produced by EsonParser#list.
    def exitList(self, ctx:EsonParser.ListContext):
        pass


    # Enter a parse tree produced by EsonParser#dictionary.
    def enterDictionary(self, ctx:EsonParser.DictionaryContext):
        pass

    # Exit a parse tree produced by EsonParser#dictionary.
    def exitDictionary(self, ctx:EsonParser.DictionaryContext):
        pass


    # Enter a parse tree produced by EsonParser#dictEntry.
    def enterDictEntry(self, ctx:EsonParser.DictEntryContext):
        pass

    # Exit a parse tree produced by EsonParser#dictEntry.
    def exitDictEntry(self, ctx:EsonParser.DictEntryContext):
        pass


    # Enter a parse tree produced by EsonParser#mathExpression.
    def enterMathExpression(self, ctx:EsonParser.MathExpressionContext):
        pass

    # Exit a parse tree produced by EsonParser#mathExpression.
    def exitMathExpression(self, ctx:EsonParser.MathExpressionContext):
        pass


    # Enter a parse tree produced by EsonParser#mathOperation.
    def enterMathOperation(self, ctx:EsonParser.MathOperationContext):
        pass

    # Exit a parse tree produced by EsonParser#mathOperation.
    def exitMathOperation(self, ctx:EsonParser.MathOperationContext):
        pass



del EsonParser