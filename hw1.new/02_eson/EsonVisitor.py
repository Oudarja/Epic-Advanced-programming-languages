# Generated from Eson.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EsonParser import EsonParser
else:
    from EsonParser import EsonParser

# This class defines a complete generic visitor for a parse tree produced by EsonParser.

class EsonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EsonParser#esonDocument.
    def visitEsonDocument(self, ctx:EsonParser.EsonDocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#esonValue.
    def visitEsonValue(self, ctx:EsonParser.EsonValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#list.
    def visitList(self, ctx:EsonParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#dictionary.
    def visitDictionary(self, ctx:EsonParser.DictionaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#dictEntry.
    def visitDictEntry(self, ctx:EsonParser.DictEntryContext):
        return self.visitChildren(ctx)



del EsonParser