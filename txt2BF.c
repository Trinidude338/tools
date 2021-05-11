#define arrSize 4096
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv){
        char file[32]={'\0'};
        char input[arrSize]={'\0'};
        if(argc>1) strcpy(file, argv[1]);
        fflush(stdin);
        if(file[0]!='\0') {
                FILE* inp=fopen(file, "r");
                fgets(input, arrSize, inp);
        } else {
                fgets(input, arrSize, stdin);
        } input[strlen(input)-1]='\0';
        int bf[arrSize]={0};
        for(int i=0;i<strlen(input);i++) bf[i]=input[i];
        for(int i=0;i<strlen(input);i++) {
                int n=bf[i];
                if(n>=65&&n<=90) {
                        printf(">");
                        for (int x=0;x<13;x++) printf("+");
                        printf("[");
                        printf("<");
                        for (int x=0;x<5;x++) printf("+");
                        printf(">");
                        printf("-");
                        printf("]");
                        printf("<");
                        for (int x=0;x<(n-65);x++) printf("+");
                } else if(n>=97&&n<=122) {
                        printf(">");
                        for (int x=0;x<10;x++) printf("+");
                        printf("[");
                        printf("<");
                        for (int x=0;x<10;x++) printf("+");
                        printf(">");
                        printf("-");
                        printf("]");
                        printf("<");
                        printf("-");
                        printf("-");
                        printf("-");
                        for (int x=0;x<(n-97);x++) printf("+");
                } else {
                        for(int x=0;x<n;x++) printf("+");
                } printf(".>");
        } printf("\n");
        return 0;
}
