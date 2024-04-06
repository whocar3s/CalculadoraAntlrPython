%{

#include <stdio.h>

int div_zero = 0;

int yylex(void);
int yyerror(char* s);   

%}

%union{
    double dval;
}
%token <dval>  NUMBER
%token <dval> BOOL
%token ADD SUB MUL DIV ABS
%token INC DEC NOT
%token EOL
%token OP CP
%left ADD SUB
%left MUL DIV
%right UMINUS
%token UMINUS

%type <dval> exp
%type <dval> factor
%type <dval> term
%type <dval> primary
%type <dval> bool_exp

%%

calclist:
    | calclist EOL { printf("=0 \n");  }
    | calclist exp EOL { if (!div_zero) printf("= %.3f\n", $2); else div_zero = 0; }
    | calclist bool_exp EOL { printf("= %s\n", $2 ? "true" : "false"); }
    ;
    

exp: term
    | exp ADD term { $$ = $1 + $3; }
    | exp SUB term { $$ = $1 - $3; }
    | ABS term { $$ = $2 >= 0 ? $2 : - $2; }
    ;

term: factor
    | term MUL factor { $$ = $1 * $3; }
    | term DIV factor { $$ = ($3 != 0) ? $1 / $3 : (printf("No se puede dividir por 0\n"), div_zero = 1, 0); }
    ;

factor: primary
    | primary INC { $$ = $1 + 1; }
    | primary DEC { $$ = $1 - 1; }
    | NOT primary { $$ = ($2 == 0) ? 1 : 0; }
    ;

primary: NUMBER
    | OP exp CP { $$ = $2; } 
    ;
    
bool_exp: BOOL
    | NOT bool_exp { $$ = !$2;}
    ;

%%

int main(double argc, char **argv)
{
    yyparse();
    return 0;
}

int yyerror(char* s) 
{
    fprintf(stderr, "error: %s\n", s);
}
