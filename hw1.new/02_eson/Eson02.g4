grammar Eson;

esonDocument: esonValue EOF;

esonValue:
    | INTEGER
    | FLOAT
    | CHAR
    | STRING
    | DATE
    | TIME
    | DATETIME
    | DURATION
    | BOOL
    | NULL
    | SYMBOL
    | list
    | dictionary
    ;

list: '[' (esonValue (',' esonValue)*)? ']';

dictionary: '{' (dictEntry (',' dictEntry)*)? '}';
dictEntry: (STRING | SYMBOL) '=' esonValue;

INTEGER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+ ([eE] [+\-]? [0-9]+)?;
CHAR: '\'' ~('\'' | '\\') '\'';
STRING: '"' ~('"')* '"';
DATE: [0-9]{4} '-' [0-9]{2} '-' [0-9]{2};
TIME: [0-9]{2} ':' [0-9]{2} ':' [0-9]{2} ('.' [0-9]+)?;
DATETIME: DATE 'T' TIME;
DURATION: [0-9]+ ('.' [0-9]+)? ('ns' | 'us' | 'ms' | 's' | 'm' | 'h');
BOOL: 'true' | 'false';
NULL: 'null';
SYMBOL: [a-zA-Z_] [a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]*;