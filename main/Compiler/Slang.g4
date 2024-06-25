grammar Slang;
options {
    language = Python3;
}

prog:   context EOF;

block: '{' NEWLINE? WS? context WS? NEWLINE? '}';

context: (line NEWLINE)* line? NEWLINE?;

functionDecl: IDENT WS? '(' WS? ')' WS? block;

line: WS? assignment WS? COMM?
    | WS? COMM
    | WS? functionDecl
    ;

assignment  :   IDENT WS? '=' WS? expression;

expression: 
    |   addition
    |   subtraction
    |   multiplication
    |   division
    |   value
    |   functionCall
    ;

brackets    :   '(' WS? expression WS? ')';

addition    :   value WS? '+' WS? value;
subtraction :   value WS? '-' WS? value;
multiplication: value WS? '*' WS? value;
division    :   value WS? '/' WS? value;

value : IDENT
    |   INT
    |   brackets
    ;

functionCall:   IDENT WS? '(' WS? (value','WS?)* value WS? ')'
    |   IDENT WS? '(' WS? (value','WS?)* WS? ')'
    ;

INT     : [0-9]+ ;
IDENT   : [a-zA-Z]+|'_';
COMM    : '#'[#a-zA-Z0-9 +\-*/=%&"()]+;
NEWLINE : [\r\n]+;
WS      : (' ')+ {self.skip();};