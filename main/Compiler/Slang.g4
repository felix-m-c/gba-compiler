grammar Slang;
options {
    language = Python3;
}

prog:   context EOF;

block: '{' newline? ws? context ws? newline? '}';

context: newline? (line newline)* line? newline?;

functionDecl: ident ws? '(' ws? ')' ws? block;

line: ws? assignment ws? comment?
    | ws? comment
    | ws? functionDecl ws? comment?
    | ws? whileLoop ws? comment?
    | ws? ifStatement ws? comment?
    ;

whileLoop: 'while' ws? '(' ws? boolExpression ws? ')' ws? block;
ifStatement: 'if' ws? '(' ws? boolExpression ws? ')' ws? block;

assignment:   ident ws? '=' ws? expression;

expression
    : arithmeticExpression
    | boolExpression
    | value
    | functionCall
    ;

boolExpression
    : equals
    | notEquals
    | ident
    | s_bool
    ;

arithmeticExpression
    : addition
    | subtraction
    | multiplication
    | division
    ;

brackets    :   '(' ws? expression ws? ')';

equals      :   value ws? '==' ws? value;
notEquals   :   value ws? '!=' ws? value;
addition    :   value ws? '+' ws? value;
subtraction :   value ws? '-' ws? value;
multiplication: value ws? '*' ws? value;
division    :   value ws? '/' ws? value;

value 
    : ident
    | s_int
    | brackets
    | s_bool
    ;

functionCall
    :   ident ws? '(' ws? (value ',' ws?)* value ws? ')'
    |   ident ws? '(' ws? (value ',' ws?)* ws? ')'
    ;

s_int   : INT;
INT     : [0-9]+ ;
s_bool  : BOOL;
BOOL    : 'True'|'False';
ident   : GLOBAL? IDENT;
GLOBAL  : 'global';
IDENT   : [a-zA-Z]+|'_';
comment : COMM;
COMM    : '#'[_,#a-zA-Z0-9 +\-*/=%&"()]+;
newline : NEWLINE;
NEWLINE : [\r\n]+;
ws      : WS;
WS      : (' ')+ -> channel (HIDDEN);