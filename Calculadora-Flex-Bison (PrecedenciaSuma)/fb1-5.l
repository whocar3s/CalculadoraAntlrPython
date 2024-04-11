%{
# include "CalculadoraFB.tab.h"
%}

%%
"/" { return DIV; }
"*" { return MUL; }
"-" { return SUB; }
"+" { return ADD; }
"|" { return ABS; }
"(" { return OP; }
")" { return CP; }
"++" { return INC; }  
"--" { return DEC; }  
"!"  { return NOT; } 

"//".* /* ignore comments*/
[0-9]+(\.[0-9]+)? { yylval.dval = atof(yytext); return NUMBER; }
"-"[0-9]+(\.[0-9]+)? { yylval.dval = - atof(yytext+1); return NUMBER; } /* Signo negativo unario */
"+"[0-9]+(\.[0-9]+)? { yylval.dval = atof(yytext); return NUMBER; } /* Signo positivo unario */
"true" { yylval.dval = 1; return BOOL; } 
"false" { yylval.dval = 0; return BOOL; }
\n { return EOL; }
[ \t] { /* ignore whitespace */ }
. { printf("Mystery character %c\n", *yytext); }
%%

