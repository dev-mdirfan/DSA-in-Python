class graph:
    def __init__(self, vertices, edges, source):
        self.v = vertices
        self.e = edges
        self.s = source
    
    def adjacencyList(self):
        graph = [[] for i in range(self.v + 1)]
        for edge in self.e:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])      # Remove if directed graph
        return graph
    
    def BFS(self):
        graph = self.adjacencyList()
        visited = [False] * (self.v + 1)
        queue = []
        queue.append(self.s)
        visited[self.s] = True
        bfsTraversal = []
        print("BFS Traversal:-")
        while queue:
            node = queue.pop(0)
            bfsTraversal.append(node)
            for nbr in graph[node]:
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr] = True
        return bfsTraversal

if __name__ == '__main__':
    vertices = 6
    edges = [[1, 2], [1, 4], [1, 5], [2, 3], [2, 4], [3, 4], [3, 6], [4, 5], [5, 6]]
    source = 1
    graph = graph(vertices, edges, source)
    print(graph.BFS())
