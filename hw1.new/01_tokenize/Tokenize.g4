lexer grammar Tokenize;

// Keywords and literals
TRUE    : 'true';
FALSE   : 'false';
NULL    : 'null';

// Date and time formats
DATE    : '2022-05-28' | '2023-12-32' | '2022-05-28T01:02:03.135164' | '2022-05-28T01:02:03' | '2022-13-01T10""20:30:40';

// Numbers (integers, decimals, scientific notation)
NUMBER  : [0-9]+ ('.' [0-9]+)? (('e' | 'E') ('+' | '-')? [0-9]+)?;

// Hexadecimal numbers
HEX     : '0x' [0-9a-fA-F]+;

// IP address
IP      : [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+;

// Strings (single and double-quoted)
STRING  : '\'' ~('\'' | '\\')* '\'' | '"' ~('"' | '\\')* '"';

// Symbols and identifiers
SYMBOL  : [a-zA-Z_] [a-zA-Z0-9_]*;

// Operators and special characters
PLUS    : '+';
MINUS   : '-';
DIVIDE  : '/';
TIMES   : '*';
DOT     : '.';
COLON   : ':';
COMMA   : ',';
UNDERSCORE: '_';

// Whitespace
WS      : [ \t\r\n]+ -> skip;

// Catch-all for any unrecognized characters
UNKNOWN : .;