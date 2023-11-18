#include<stdio.h>
int Sum(int n);
int Sum(int n);
int main()
{
    int n;
    printf("Enter last number: ");
    scanf("%d",&n);
    printf("Sum of the first %d numbers: %d",n,Sum(n));
    return 0;
}
int Sum(int n)
{
    if(n>0)
    {
        return (n+Sum(n-1));
    }
    return 0;
}