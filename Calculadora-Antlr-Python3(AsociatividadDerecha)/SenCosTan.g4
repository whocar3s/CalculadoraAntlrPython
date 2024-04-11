grammar SenCosTan;

//grammar
prog: stat+;

stat: expr NEWLINE                #print
    | ID '=' expr NEWLINE         #assign
    | NEWLINE                     #blank
    ;

expr: expr op=(' * ' |' / ') expr      #MulDiv
    | expr op=(' + '|' - ') expr      #AddSub
    | SIN '(' expr ')'            #Sin
    | COS '(' expr ')'            #Cos
    | TAN '(' expr ')'            #Tan
    | INT                         #int
    | 'pi'                        #pi
    | FLOAT                       #float
    | BOOLEAN                   #Boolean
    | BOOL_NEG expr                 #BoolNegacion
    | ID                          #id
    | '(' expr ')'                #parens
    | expr '++'                    #Incremento
    | expr '--'                    #Decremento
    | '-' expr                    #Negativo
    | '+' expr                    #Positivo
    ;
  
  
//lex
MUL    :  ' * ';
ADD    :  ' + ';
DIV    :  ' / ';
SUB    :  ' - ';
BOOLEAN : 'true' | 'false';
SIN: 'Sin';
COS: 'Cos';
TAN: 'Tan';
BOOL_NEG : '!';
ID     :  [a-zA-Z]+;
INT    :  ('-' | '+')? [0-9]+;
FLOAT  :  ('-' | '+')? [0-9]+ '.'[0-9]+;
NEWLINE:  '\r'?'\n';
WS     :  [\t]+ -> skip;
