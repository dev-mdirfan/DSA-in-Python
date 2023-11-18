#Disjoint set algorithm #Also the algo for krushkals algo


def find(graph,node):
    if(graph[node]<0):
        return node

    else:
        temp = find(graph,graph[node])
        graph[node]=temp
        return temp                         #reduces the complexity

def union(graph,u,v):
    parent_u=find(graph,u)
    parent_v=find(graph,v)
    
    if(parent_u==parent_v):
        print("Nodes of the same family")

    else:
        if(graph[parent_u]==graph[parent_v]):
            graph[parent_v]=graph[parent_u]+graph[parent_v]          #add the negative indices (which show the number of connected elements) of the smaller value (mag wise) to the larger one                            
            graph[parent_u]=parent_v                          #let the smaller one point the larger one
        elif(graph[parent_u]<graph[parent_v]):
            graph[parent_u]=graph[parent_u]+graph[parent_v]          
            graph[parent_v]=parent_u
        else:
            graph[parent_v]=graph[parent_u]+graph[parent_v]          
            graph[parent_u]=v


n=7
graph={}

for i in range(n):
    graph[i]=-1


ipt=[[0,1],[1,2],[2,3],[4,5],[3,5]]

for u,v in ipt:
    print(u,v)
    print(graph)
    union(graph,u,v)
print(graph)
