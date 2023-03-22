from collections import deque

class AdjacencyList:
    def buildGraph(v, edges):
        graph = [[] for i in range(v + 1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])    # remove if directed
        return graph
    
    def printGraph(v, edges):
        graph = AdjacencyList.buildGraph(v, edges)
        for i in range(1, v + 1):
            print(i, ':', end='')
            for nbr in graph[i]:
                print('  ->', nbr, end='')
            print()
    
    def BFS(v, edges, src):
        graph = AdjacencyList.buildGraph(v, edges)
        visited = [False] * (v + 1)
        queue = deque()
        queue.append(1)
        visited[src] = True
        
        bfsTraversal = []
        
        while queue:
            node = queue.pop()
            bfsTraversal.append(node)
            for nbr in graph[node]:
                if visited[nbr] == False:
                    queue.append(nbr)
                    visited[nbr] = True
        return bfsTraversal

if __name__ == '__main__':
    v = 6
    edges = [[1, 2], [1, 4], [1, 5], [2, 3], [2, 4], [3, 4], [3, 6], [4, 5], [5, 3], [5, 6]]
    AdjacencyList.buildGraph(v, edges)
    print(AdjacencyList.BFS(v, edges, 1))
    print(AdjacencyList.printGraph(v, edges))
