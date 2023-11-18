#include<stdio.h>
//-----------------------For create Linked List----------------------
struct node
{
    int data;
    struct node *next;
}*head=NULL;
void llist()
{
    struct node *t=head,*p = (struct node*)malloc(sizeof(struct node));
    printf("Enter a number: ");
    scanf("%d",&p->data);
    if(head == NULL)
    {
        p->next = NULL;
        head = p;
    }
    else
    {
        while(t->next!=NULL)
            t = t->next;
        t->next = p;
        p->next = NULL;
    }
    struct node *temp=head;
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
}
//-------------------For Count Length---------------------
void count()
{
    int count = 0;
    struct node *t=head;
    while(t!=NULL)
    {
        count++;
        t = t->next;
    }
    printf("\nLength of the Linked List: %d",count);
} 
//-------------------Main function------------------------
int main()
{
    int flag = 1,n;
    printf("1 - Create linked list\n2 - Count Length\n3 - End \n");
    while(flag)
    {
        printf("\n\nEnter your choice: ");
        scanf("%d",&n);
        switch(n)
        {
            case 1: llist();
                break; 
            case 2: count();
                break;
            case 3: flag = 0;
                break;
        }
    }
    return 0;
}