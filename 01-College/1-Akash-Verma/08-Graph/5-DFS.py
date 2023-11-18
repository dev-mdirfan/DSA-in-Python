# DFS Traversal

class DFS:
    def __init__(self, v, edges, source):
        self.v = v
        self.edges = edges
        self.source = source
        self.graph = self.adjacencyList()
        self.dfsAnswer = self.dfs()
        self.graphAnswer = self.printGraph()
        
    def adjacencyList(self):
        graph = dict()
        for node in range(self.v):
            graph[node] = []
        for edge in self.edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    def printGraph(self):
        for node in range(self.v):
            print(node, ':', end='')
            for neighbors in self.graph[node]:
                print('  ->' ,neighbors, end='')
            print()
    
    def traversal(self, edges):
        graph = self.adjacencyList(v, edges)
        for node in graph:
            pass
        return
    
    def dfs(self):
        graph = self.adjacencyList()
        visited = [False] * v
        self.dfsAnswer = []
        self.dfsRecursion(self.source, visited)
        for node in range(self.v):
            pass
        return self.dfsAnswer
    
    def dfsRecursion(self, source, visited):
        visited[source] = True
        self.dfsAnswer.append(source)
        
        for neighbors in self.graph[source]:
            if not visited[neighbors]:
                self.dfsRecursion(neighbors, visited)
    
    def bfs(self):
        return
    
    

if __name__ == '__main__':
    v = 6
    edges = [[0, 1], [0, 2], [0, 5], [1, 3], [1, 5], [2, 3], [3, 4], [4, 5]]
    dfs = DFS(v, edges, 0)
    
    for node in dfs.dfsAnswer:
        print(node, end=' ')
    
    dfs.graphAnswer