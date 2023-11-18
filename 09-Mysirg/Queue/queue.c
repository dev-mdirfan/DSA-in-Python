#include<stdio.h>
#include<malloc.h>
struct arqueue
{
    int front,rear,capacity,*a;

};
struct arqueue* queue(int size)
{
    struct arqueue *q =malloc(sizeof(struct arqueue));
    if(!q)
        return NULL;
    q->capacity = size;
    q->front = q->rear = -1;
    q->a=malloc(q->capacity*sizeof(int));
    if(!q->a)
        return NULL;
    return q;
}
int isEmpty(struct arqueue *q)
{
    return (q->front==-1);

}
int isFull(struct arqueue *q)
{
    return ((q->rear +1)%q->capacity==q->front);
}
int qsize(struct arqueue *q)
{
    return q->capacity - q->front +q->rear+1;
}
void enqueue(struct arqueue *q,int data)
{
    if(isFull(q))
        printf("Overflow");
    else
    {
        q->rear = (q->rear + 1) % q->capacity;
        q->a[q->rear]= data;
        if(q->front == -1)
            q->front= q->rear;
    }
}
int dequeue(struct arqueue *q)
{
    int data =0;
    if(isEmpty(q))
        printf("Underflow");
    else
    {
        data = q->a[q->front];
        if(q->front == q->rear)
        {
            q->front = q->rear =-1;
        }
        else
        {
            q->front = (q->front +1) % q->capacity;
        }

    }
    return data;
}
void print(struct arqueue *q)
{
    struct arqueue *t = q;
    while(t->front!=t->rear)
    {
        printf("%d ",t->a[t->front]);
            t->front++;
    }

}

int main()
{
    int size;
    scanf("%d",&size);
    struct arqueue *p=queue(size);
    enqueue(p,1);
    enqueue(p,2);
    enqueue(p,3);
    enqueue(p,4);
    enqueue(p,5);
    print(p);
    printf("\n%d",dequeue(p));
    printf("%d",dequeue(p));
    printf("%d",dequeue(p));
    printf("%d",dequeue(p));
    printf("%d",dequeue(p));
    return 0;
}
