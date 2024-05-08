from antlr4 import FileStream, CommonTokenStream
from EsonLexer import EsonLexer
from EsonParser import EsonParser
from EsonVisitor import EsonVisitor
import datetime
import json
import sys
import math  # Don't forget to import the math module

class Visitor(EsonVisitor):
    def visitMathExpression(self, ctx):
        return self.visit(ctx.mathOperation())

    def visitMathOperation(self, ctx):
        left = self.visit(ctx.esonValue(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.esonValue(1))
        
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == 'sin':
            return math.sin(right)
        elif operator == 'cos':
            return math.cos(right)


in_stream = FileStream('input.eson')
lexer = EsonLexer(in_stream)
stream = CommonTokenStream(lexer)
parser = EsonParser(stream)
tree = parser.item()
visitor = Visitor()
result = visitor.visit(tree)
json.dump(result, sys.stdout, indent=2, sort_keys=True)  # Corrected the indent value
