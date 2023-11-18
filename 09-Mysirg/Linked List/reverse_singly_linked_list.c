#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *head = NULL;
struct node *createnode()
{
    struct node *p = head;
    p = (struct node *)malloc(sizeof(struct node));
    return p;
}
void create()
{
    struct node *p = createnode(), *t = head;
    printf("\nEnter your number:");
    scanf("%d", &p->data);
    p->next = NULL;
    if (head == NULL)
    {
        head = p;
    }
    else
    {
        while (t->next != NULL)
        {
            t = t->next;
        }
        t->next = p;
    }
    print(head);
}

void reverse()
{
    struct node *t1 = NULL, *t2 = NULL;
    while (head != NULL)
    {
        t2 = head->next;
        head->next = t1;
        t1 = head;
        head = t2;
    }
    print(t1);
}
void print(struct node *t1)
{
    struct node *t = t1;
    while (t != NULL)
    {
        printf("%d ", t->data);
        t = t->next;
    }
}

int main()
{
    int n, flag = 1;
    printf("1-Craete linked list\n2-Reverse linked list\n3-End the program");
    while (flag)
    {
        printf("\nEnter choice:");
        scanf("%d", &n);
        switch (n)
        {
        case 1:
            create();
            break;
        case 2:
            reverse();
            break;
        case 3:
            flag = 0;
            break;
        }
    }
    return 0;
}