from heapq import heappop, heappush, heapify
from math import inf
edges = [[1, 2, 5], [1, 3, 7], [1, 4, 8], [2, 3, 1], [2, 4, 2], [3, 4, 3]]
source = 1

graph = dict()
for i in range(len(edges)):
    if edges[i][0] in graph:
        graph[edges[i][0]].append((edges[i][1], edges[i][2]))
    else:
        graph[edges[i][0]] = [(edges[i][1], edges[i][2])]
    if edges[i][1] in graph:
        graph[edges[i][1]].append((edges[i][0], edges[i][2]))
    else:
        graph[edges[i][1]] = [(edges[i][0], edges[i][2])]

print(graph)

distance = [inf] * (len(graph) + 1)
visited = [False] * (len(graph) + 1)

heap = []
distance[source] = 0
heappush(heap, [distance[source], source])

# print(heap)

while heap:
    currDistance, currNode = heappop(heap)
    
    if visited[currNode]:
        continue
    visited[currNode] = True
    for pair in graph[currNode]:
        print(pair)
        if visited[pair[0]]:
            continue
        newDistance = currDistance + pair[1]
        if newDistance < distance[pair[0]]:
            distance[pair[0]] = newDistance
            heappush(heap, [newDistance, pair[0]])

print(distance)



# Network Delay