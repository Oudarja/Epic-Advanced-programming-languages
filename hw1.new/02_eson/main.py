from antlr4 import FileStream, CommonTokenStream
from EsonLexer import EsonLexer
from EsonParser import EsonParser
from EsonVisitor import EsonVisitor
import datetime
import json
import sys


def parse_time(time):
    return datetime.datetime.strptime(
        time,
        '%H:%M:%S.%f' if '.' in time[:15] else '%H:%M:%S')


def parse_date(date):
    return datetime.datetime.fromisoformat(date)


def parse_datetime(dt):
    d, t = dt.split('T')
    d = parse_date(d)
    t = parse_time(t)
    return datetime.datetime.combine(d.date(), t.time())


def format_time(time):
    return time.strftime('%Y-%m-%d')


def format_date(date):
    return date.strftime('%H:%M:%S.%f')


def format_datetime(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')


class Visitor(EsonVisitor):
    # TODO: write the visitor
    def visitList(self, ctx):
        return [self.visit(child) for child in ctx.esonValue()]

    def visitDictionary(self, ctx):
        dictionary = {}
        for entry in ctx.dictEntry():
            key = entry.STRING().getText() if entry.STRING() else entry.SYMBOL().getText()
            value = self.visit(entry.esonValue())
            dictionary[key] = value
        return dictionary

    def visitDictEntry(self, ctx):
        return self.visit(ctx.esonValue())

    def visitInteger(self, ctx):
        return int(ctx.getText())

    def visitFloat(self, ctx):
        return float(ctx.getText())

    def visitChar(self, ctx):
        return ctx.getText()[1]  # Extract the character from the single quotes

    def visitString(self, ctx):
        return ctx.getText()[1:-1]  # Remove double quotes from the string

    def visitDate(self, ctx):
        return parse_date(ctx.getText())

    def visitTime(self, ctx):
        return parse_time(ctx.getText())

    def visitDatetime(self, ctx):
        return parse_datetime(ctx.getText())

    def visitDuration(self, ctx):
        duration_text = ctx.getText()
        value = float(duration_text[:-1])  # Extract numerical value
        unit = duration_text[-1]  # Extract the unit
        if unit == 's':
            return value
        elif unit == 'ms':
            return value / 1000
        elif unit == 'us':
            return value / 1000000
        elif unit == 'ns':
            return value / 1000000000
        elif unit == 'm':
            return value * 60
        elif unit == 'h':
            return value * 3600

    def visitBool(self, ctx):
        return ctx.getText() == 'true'

    def visitNull(self, ctx):
        return None

    def visitSymbol(self, ctx):
        return ctx.getText()


in_stream = FileStream('input.eson')
lexer = EsonLexer(in_stream)
stream = CommonTokenStream(lexer)
parser = EsonParser(stream)
tree = parser.item()
visitor = Visitor()
result = visitor.visit(tree)
json.dump(result, sys.stdout, indent='  ', sort_keys=True)
