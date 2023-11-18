#include<stdio.h>
void TOH(int n, char BEG, char AUX, char END);
int main()
{
    int n;
    char a='A',b='B',c='C';
    printf("Enter Numbers of disk: ");
    scanf("%d",&n);
    TOH(n,a,b,c);
}

void TOH(int n, char BEG, char AUX, char END)
{
    if(n>=1)
    {
        TOH(n-1,BEG,END,AUX);
        static int i=1;
        printf("%d-%c to %c\n",i++,BEG,END);
        TOH(n-1,AUX,BEG,END);
    }
}