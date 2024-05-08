grammar Calc;

// <expr> ::= <sum>
// <sum> ::= <mul> | <sum> "+" <mul> | <sum> "-" <mul>
// <mul> ::= <last> | <mul> "*" <last> | <mul> "/" <last>
// <last> ::= <number> | "+" <last> | "-" <last> | "(" <expr> ")"
// <number> ::= <digit> | <digit> <number>
// <digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

// Lexer rules
NUMBER: [0-9]+;
SPACE: (' ' | '\t') -> skip;

// Parser rules
exprs: expr* EOF;
expr: sum '\n';
sum: mul | sum op=('+' | '-') mul;
mul: last | mul op=('*' | '/') last;
last: num=NUMBER | op=('+' | '-') last | '(' sum ')';
