grammar EpicLang;

// Lexer rules
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
INT: '-'? [0-9]+;
BOOLEAN: 'true' | 'false';
NONE: 'none';
LBRACKET: '[';
RBRACKET: ']';
COMMA: ',';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
EQ: '==';
NEQ: '!=';
NOT: '!';
AND: '&';
OR: '|';
LEN: 'len';
PRINT: 'print';
IF: 'if';
THEN: 'then';
ELSE: 'else';
FOR: 'for';
DO: 'do';
WHILE: 'while';
FUNC: 'func';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
COMMENT: '//' ~[\r\n]* -> skip; // Single-line comment

// Parser rules
program: functionDeclaration+;

functionDeclaration: FUNC ID parameters? block;

parameters: LPAREN parameterList? RPAREN;

parameterList: ID (COMMA ID)*;

block: LBRACE statement* RBRACE;

statement: 
    | emptyStatement
    | expressionStatement
    | block
    | ifStatement
    | forStatement
    | whileStatement
    | assignmentStatement
    | loopControlStatement
    | returnStatement
    | printStatement;

emptyStatement: SEMICOLON;

expressionStatement: expression SEMICOLON;

ifStatement: IF expression THEN statement (ELSE statement)?;

forStatement: FOR ID IN expression DO block;

whileStatement: WHILE expression DO block;

assignmentStatement: variable '=' expression SEMICOLON;

loopControlStatement: (BREAK | CONTINUE) SEMICOLON;

returnStatement: RETURN expression? SEMICOLON;

printStatement: PRINT expression SEMICOLON;

expression: 
    | literal
    | ID
    | functionCall
    | listLiteral
    | expression indexing
    | expression (MULTIPLY | DIVIDE | MODULO) expression
    | expression (PLUS | MINUS) expression
    | expression (LT | LE | GT | GE | EQ | NEQ) expression
    | expression (AND | OR) expression
    | NOT expression
    | LEN LPAREN expression RPAREN;

literal: INT | BOOLEAN | NONE;

listLiteral: LBRACKET (expression (COMMA expression)*)? RBRACKET;

functionCall: ID LPAREN (expression (COMMA expression)*)? RPAREN;

indexing: LBRACKET expression RBRACKET;

// Variable rule to support variable declarations
variable: ID;