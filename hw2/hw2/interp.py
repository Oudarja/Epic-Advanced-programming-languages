import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener, ConsoleErrorListener
from EpicLangLexer import EpicLangLexer
from EpicLangParser import EpicLangParser
from EpicLangVisitor import EpicLangVisitor


# handler for syntax errors
class ErrorHandler(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print('syntax error')
        sys.exit(0)

class Interpreter(EpicLangVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        for func_decl in ctx.functionDeclaration():
            self.visitFunctionDeclaration(func_decl)

    def visitFunctionDeclaration(self, ctx):
        func_name = ctx.ID().getText()
        parameters = ctx.parameters().parameterList().ID() if ctx.parameters() else []
        self.variables[func_name] = {"parameters": parameters, "body": ctx.block()}

    def visitBlock(self, ctx):
        for statement in ctx.statement():
            self.visitStatement(statement)

    def visitExpressionStatement(self, ctx):
        return self.visitExpression(ctx.expression())

    def visitAssignmentStatement(self, ctx):
        variable_name = ctx.variable().getText()
        value = self.visitExpression(ctx.expression())
        self.variables[variable_name] = value

    def visitPrintStatement(self, ctx):
        value = self.visitExpression(ctx.expression())
        print(value)

    def visitReturnStatement(self, ctx):
        return self.visitExpression(ctx.expression()) if ctx.expression() else None

    def visitIfStatement(self, ctx):
        condition = self.visitExpression(ctx.expression())
        if condition:
            self.visitBlock(ctx.statement(0))
        elif ctx.ELSE():
            self.visitBlock(ctx.statement(1))

    def visitForStatement(self, ctx):
        variable_name = ctx.ID().getText()
        start = self.visitExpression(ctx.expression(0))
        end = self.visitExpression(ctx.expression(1))
        step = 1 if start < end else -1
        for value in range(start, end, step):
            self.variables[variable_name] = value
            self.visitBlock(ctx.block())

    def visitWhileStatement(self, ctx):
        while self.visitExpression(ctx.expression()):
            self.visitBlock(ctx.block())
    def visitExpression(self, ctx):
        if ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.variable():
            return self.visitVariable(ctx.variable())
        elif ctx.BIN_OP():
            left = self.visitExpression(ctx.expression(0))
            right = self.visitExpression(ctx.expression(1))
            return self.evaluateBinaryOperation(ctx.BIN_OP().getText(), left, right)
        elif ctx.UNARY_OP():
            operand = self.visitExpression(ctx.expression(0))
            return self.evaluateUnaryOperation(ctx.UNARY_OP().getText(), operand)
        elif ctx.listLiteral():
            return self.visitListLiteral(ctx.listLiteral())
        elif ctx.functionCall():
            return self.visitFunctionCall(ctx.functionCall())
        elif ctx.lenOperation():
            return self.visitLenOperation(ctx.lenOperation())
        elif ctx.indexOperation():
            return self.visitIndexOperation(ctx.indexOperation())

    def visitLiteral(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.BOOL():
            return ctx.BOOL().getText() == 'true'
        elif ctx.NONE():
            return None

    def visitVariable(self, ctx):
        variable_name = ctx.getText()
        return self.variables.get(variable_name)

    def evaluateBinaryOperation(self, operator, left, right):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right
        elif operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '==':
            return left == right
        # Add more operators as needed

    def evaluateUnaryOperation(self, operator, operand):
        if operator == '-':
            return -operand
        elif operator == '!':
            return not operand
        # Add more unary operators as needed

    def visitListLiteral(self, ctx):
        elements = [self.visitExpression(expr) for expr in ctx.expression()]
        return elements

    def visitFunctionCall(self, ctx):
        function_name = ctx.IDENTIFIER().getText()
        arguments = [self.visitExpression(expr) for expr in ctx.expression()]
        # Implement logic for calling functions
        pass

    def visitLenOperation(self, ctx):
        operand = self.visitExpression(ctx.expression())
        if isinstance(operand, list):
            return len(operand)
        else:
            print("runtime error: len() applied to non-list")
            sys.exit(0)

    def visitIndexOperation(self, ctx):
     variable_name = ctx.IDENTIFIER().getText()
     index = self.visitExpression(ctx.expression())
     if variable_name in self.variables and isinstance(self.variables[variable_name], list):
        lst = self.variables[variable_name]

        # Check if the index is within bounds
        if 0 <= index < len(lst):
            return lst[index]
        else:
            print(f"runtime error: Index out of bounds for variable '{variable_name}'")
            sys.exit(0)
     else:
        print(f"runtime error: '{variable_name}' is not a list or is not defined")
        sys.exit(0)
def main():
    # create input stream
    in_stream = FileStream(sys.argv[1])

    # create a lexer
    lexer = EpicLangLexer(in_stream)
    # add error handling for our lexer
    lexer.addErrorListener(ErrorHandler())
    lexer.removeErrorListener(ConsoleErrorListener.INSTANCE)

    # create a parser with the lexer as an input
    stream = CommonTokenStream(lexer)
    parser = EpicLangParser(stream)
    # add error handling for our parser
    parser.addErrorListener(ErrorHandler())
    parser.removeErrorListener(ConsoleErrorListener.INSTANCE)

    # use the parser to obtain an abstract syntax tree
    tree = parser.program()

    # TODO : traverse the tree and execute the program
     # create the interpreter and execute the program
    interpreter = Interpreter()
    interpreter.visitProgram(tree)


if __name__ == "__main__":
    main()
