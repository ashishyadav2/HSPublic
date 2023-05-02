function ("printf"|"main")
identifier [a-zA-Z][a-zA-Z0-9]*
%%
#.* {printf("Header File: %s\n",yytext);}
int |
void {printf("Keyword: %s\n",yytext);}
{function} {printf("Function: %s\n",yytext);}
{identifier} {printf("Identifier: %s\n",yytext);}
\{ {printf("Blocks Begins\n");}
\} {printf("Blocks Ends\n");}
\".*\" {printf("String: %s\n",yytext);}
[0-9]+ {printf("Number: %s\n",yytext);}
= {printf("Assignment Operator: %s\n",yytext);}
%%
int main(int argc, char **argv) {
    FILE *file;
    file = fopen("input.c","r");
    if (!file) {
        printf("File not found");
    }
    yyin = file;
    yylex();
    printf("\n");
    return(0);
}
int yywrap(){
    return(1);
}