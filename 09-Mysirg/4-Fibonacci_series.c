#include<stdio.h>
int fib(int n);
int main()
{
    int n;
    printf("Enter place for get fibonacii no: ");
    scanf("%d",&n);
    printf("%dth term is %d",n,fib(n));
    return 0;

}

int fib(int n)
{
    if(n==1||n==2)
    {
        return 1;
    }
        return (fib(n-1)+fib(n-2));
}