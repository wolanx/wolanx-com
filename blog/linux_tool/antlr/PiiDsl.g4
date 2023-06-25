grammar PiiDsl;

// antlr -Dlanguage=Python3 PiiDsl.g4 -visitor -o PiiDsl

/*
 * parser rules
 */

program
    : statement+
    ;

statement
    : expr                                  # LineExpr
    | identifier '=' expr                   # AssignExpr
    ;

expr
    : expr arguments                                                    # FuncExpr
    | expr '.' expr                                                     # MemberDotExpr
    // | '-' expr                                                          # UnaryMinusExpr
    | left=expr op=('*'|'/'|'%') right=expr                             # OpExpr
    | left=expr op=('+'|'-') right=expr                                 # OpExpr
    | left=expr op=('<<' | '>>') right=expr                             # BitShiftExpr
    | left=expr op=('<' | '>' | '<=' | '>=' | '==' | '!=') right=expr   # EqualityExpr
    | left=expr op=('&' | '^' | '|') right=expr                         # BitOpExpr
    | left=expr op=('and' | 'or' | '&&' | '||') right=expr              # LogicalExpr
    | obj                                                               # ObjectExpr
    | identifier                                                        # IdExpr
    | literal                                                           # LitExpr
    | '(' expr ')'                                                      # ParenExpr
    ;

arguments
    : '(' (expr (',' expr)*)? ')'
    ;

obj
   : '{' pair (',' pair)* '}'
   | '{' '}'
   ;

pair
   : mapk=NAME ':' mapv=expr
   ;

identifier
    : NAME
    ;

literal
    : NUMBER
    ;

/*
 * lexer rules
 */

NAME  : [a-zA-Z$][a-zA-Z0-9$_]* ;

NUMBER
   : '-'? INT ('.' [0-9] +)?
   ;

D : ',' ;
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
LP : '(' ;
RP : ')' ;
PCT : '%' ;
WS  : [ \t\r\n]+ -> skip ;    // toss out whitespace

fragment INT
   : '0' | [1-9] [0-9]*
   ;
