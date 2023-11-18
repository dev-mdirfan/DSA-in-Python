#include <stdio.h>
#include <stdlib.h>

struct ArrayQueue
{
    int front;
    int rare;
    int capacity;
    int *array;
};

struct ArrayQueue *queue(int size)
{
    struct ArrayQueue *Q = malloc(sizeof(struct ArrayQueue));

    if (!Q)
        return NULL;
    Q->capacity = size;
    Q->front = Q->rare = -1;
    Q->array = malloc(sizeof(int) * Q->capacity);
    if (!Q->array)
        return NULL;
    return Q;
}
int isEmptyQueue(struct ArrayQueue *Q )
{
    return Q->front==-1;
}
int isFullQueue(struct ArrayQueue *Q)
{
    return (Q->rare+1)%Q->capacity==Q->front;
}
void EnQueue(int data,struct ArrayQueue *Q)
{
    if(isFullQueue)
     print("Overflow!");
    else {
        Q->rare=(Q->rare+1)%(Q->capacity);
        Q->array[Q->rare]=value;
    } 

    if(Q->front==1)
    {
        Q->front==Q->rare;
        return ;
    }
   
}
void DeQueue(struct ArrayQueue *Q)
{
    int data=0;
    if(isEmptyQueue)
    {
        printf("underflow!");
        return 0;
    }
    else{
        data=Q->array[Q->front];
        if(Q->front==Q->rare)
        {
            Q->front=Q->rare=-1;
        }
        else
        {
            Q->front=(Q->front+1)%Q->capacity;
        }
    }
    print(Q);
}

void print(struct ArrayQueue *Q)
{
    struct ArrayQueue *t=Q;
    while(t->front!=t->rare)
    {
        print("%d",t->array[i]);
        t=t->front;
    }
}
int main(struct ArrayQueue *Q)
{
    int flag=1,n,a;
    while(flag)
    {
        printf("Enter choice: ");
        scanf("%d",&n);
        switch()
        {
            case 1: printf("Enter Number: ");
                scanf("%d",&a);
                EnQueue(a,Q);
                break;
        }

    }
    return 0;
}
