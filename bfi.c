#define bfplus "++*i;\n"
#define bfminus "--*i;\n"
#define bfnext "++i;\n"
#define bfprev "--i;\n"
#define bfbeg "while(*i!=0){\n"
#define bfend "}\n"
#define bfprint "putchar(*i);\n"
#define bfinp "*i=getchar();\n"
#include <stdio.h>

int main(int argc, char *argv[]){
    char inp[4096]={"\0"};
    FILE *infile, *outfile;
    if(argc==2){
            infile = fopen(argv[1], "r");
            outfile = fopen("a.c", "w");
    } else if(argc==3){
            infile = fopen(argv[1], "r");
            outfile = fopen(argv[2], "w");
    } else{
            printf("Usage: bfi [input file] <output file>");
            return 1;
    }fgets(inp, 4096, infile);
    fprintf(outfile, "#include <stdio.h>\nint main(){\nchar buf[4096]={0};\nchar *i;\ni=buf;\n");
    for (int i=0;(i<sizeof(inp));i++){
        if (inp[i]=='+')
            fprintf(outfile, bfplus);
        else if (inp[i]=='-')
            fprintf(outfile, bfminus);
        else if (inp[i]=='>')
            fprintf(outfile, bfnext);
        else if (inp[i]=='<')
            fprintf(outfile, bfprev);
        else if (inp[i]=='[')
            fprintf(outfile, bfbeg);
        else if (inp[i]==']')
            fprintf(outfile, bfend);
        else if (inp[i]=='.')
            fprintf(outfile, bfprint);
        else if (inp[i]==',')
            fprintf(outfile, bfinp);
    } fprintf(outfile, "return 0;\n}\n");
    fclose(infile);
    fclose(outfile);
    return 0;
}
