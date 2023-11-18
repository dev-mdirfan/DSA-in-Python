struct ArayQueue
{
    int front,rear;
    int capacity;
    int *array;
};
struct ArrayQueue* createQueue(int capacity)
{
    struct ArrayQueue* Q= malloc(sizeof(struct ArrayQueue));
    if(!Q)
        return(NULL);
    Q->capacity=capacity;
    Q->front=Q->rear=-1
    Q->array=malloc(Q->capacity*sizeof(int));
    if(!Q->array)
        return(NULL);
    return Q;
}