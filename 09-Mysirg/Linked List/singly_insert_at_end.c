#include<stdio.h>
struct node
{
    int info;
    struct node *link;
};
struct node *START=NULL;

struct node* createNode()
{
    struct node *n;
    n=(struct node *)malloc(sizeof(struct node));
    return n;
}
void insertNode()
{
    struct node *temp,*t;
    temp=createNode();
    printf("Enter a number");
    scanf("%d",&temp->info);
    temp->link=NULL;
    if(START==NULL)
        START=temp;
    else
    {
        t=START;
        while(t->link!=NULL)
            t=t->link;
        t->link=temp;
    }
}

void print()
{
    struct node *t=START;
    int i;
    while(t!=NULL)
    {
        printf("%d ",t);
        t = t->link;
    }
}
void insertEnd()
{
    struct node *t=START,*p;
    p=createNode();
    if(START==NULL)
        START=temp;
    else
    {
        t=START;
        while(t->link!=NULL)
            t=t->link;
        t->link=temp;
    }
}
int main()
{
    insertNode();
    insertNode();
    insertNode();
    insertNode();
    print();
    insertEnd();
    
}