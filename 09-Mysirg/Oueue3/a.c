// write an algorithm for finding armstrong number from 1 to 5
// write an algo queue using stack
// write an algo for converting infix to postfix expression using stack 
// write an algo for searching an element in b.s.t.
#include<stdio.h>
#include<math.h>

int main()
{
    int r,n,s=0;
    scanf("%d",&n);
    int a=n;
    while(n)
    {
        r = n%10;
        s = s+r*r*r;
        n = n/10;
    }
    if(a==s)
        printf("armg");
    else
        printf("no");
    return 0;
}
