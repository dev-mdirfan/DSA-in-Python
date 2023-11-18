#include<stdio.h>
#include<malloc.h>
struct node
{
    int data;
    struct node *next;
};
struct node *head=NULL;
struct node* newnode()
{
    struct node *p;
    p = (struct node *)malloc(sizeof(struct node));
    return p;
}
void insertB()
{
    struct node *p;
    p=newnode();
    printf("Enter number :");
    scanf("%d",&p->data);
    if(head==NULL)
    {
        p->next = NULL;
        head = p;
    }
    p->next = head;
    head = p;
}
void create()
{
    struct node *t=head,*p;
    p = newnode();
    printf("Enter a number :");
    scanf("%d",&p->data);
    p->next = NULL;
    if(head==NULL)
    {
        head = p;
        return;
    }
    while(t->next!=NULL)
    {
        t = t->next;
    }
    t->next = p;
}
void display()
{
    struct node *t=head;
    while(t!=NULL)
    {
        printf("%d  ",t->data);
        t = t->next;
    }
}
int main()
{
    int n,flag=1;
    printf("\nTo create list : 1\nTo insert a node at begining : 2\nTo display : 3\nTo End program : 4\n");
    while(flag)
    {
        printf("\nEnter Choice :");
        scanf("%d",&n);
        switch(n)
        {
            case 1: 
                create();
                break;
            case 2: 
                insertB();
                break;
            case 3: 
                display();
                break;
            case 4: 
                flag = 0;
                break;
            default : printf("\nEnter again!");
                
        }
    }
    
}