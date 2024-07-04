grammar Slang;
options {
    language = Python3;
}

prog:   block EOF;

closedBlock: '{' newline? ws? block ws? newline? '}';

block: newline? (line newline)* line? newline?;

functionDecl: 'def' ws? ident ws? identList ws? closedBlock;
identList: '(' ws? (ident ws? ',' ws?)* ident? ws? ')';

line: ws? assignment ws? comment?
    | ws? comment
    | ws? functionDecl ws? comment?
    | ws? whileLoop ws? comment?
    | ws? ifStatement ws? comment?
    | ws? returnStatement ws? comment?
    | ws? functionCall ws? comment?
    | ws? byteArray ws? comment?
    ;

whileLoop: 'while' ws? '(' ws? boolExpression ws? ')' ws? closedBlock;
ifStatement: 'if' ws? '(' ws? boolExpression ws? ')' ws? closedBlock newline? ws? elseStatement?;
elseStatement: 'else' ws? closedBlock;
returnStatement: 'return(' ws? expression? ws? ')';

assignment:   ident ws? '=' ws? expression;

expression
    : arithmeticExpression
    | boolExpression
    | value
    | functionCall
    ;

boolExpression
    : s_bool
    | ident
    | equals_op
    | notEquals_op
    | and_op
    | xor_op
    | or_op
    ;

arithmeticExpression
    : addition
    | subtraction
    | multiplication
    | division
    ;

brackets    :   '(' ws? expression ws? ')';

equals_op   :   value ws? '==' ws? value;
notEquals_op:   value ws? '!=' ws? value;
and_op      :   value ws? '&' ws? value;
xor_op      :   value ws? '^' ws? value;
or_op       :   value ws? '|' ws? value;

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
    
byteArray: 'bytes' ws? ident newline? ws? '[' newline? ws? byteList newline? ws? ']';
byteList:  (ws? s_int ',' newline?)+ ws? s_int;

s_int   : INT;
INT     : [0-9]+
        | '0x'[0-9a-e]+
        | '0b'[01]+
        ;
s_bool  : BOOL;
BOOL    : 'True'|'False';
ident   : GLOBAL? IDENT;
GLOBAL  : 'global';
IDENT   : [a-zA-Z][a-zA-Z_0-9]*|'_';
comment : COMM;
COMM    : '#'[_.,#a-zA-Z0-9 +\-*^/=%&<>:;"()]+;
newline : NEWLINE;
NEWLINE : [\r\n]+;
ws      : WS;
WS      : (' ')+ -> channel (HIDDEN);