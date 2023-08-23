#  DFS
from collections import deque
class DFS:
    def __init__(self, v, edges, source):
        self.v = v
        self.edges = edges
        self.source = source
        self.dfsAns = self.depthFirstSearch(v, edges, source)
    
    def buildGraph(self, v, edges):
        graph = dict()
        for node in range(v):
            graph[node] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    def bfs(self, v , m, edges, source):
        graph = self.buildGraph(v, edges)
        queue = deque()
        
        visited = [False] * (v + 1)
        distance = [-1] * (v + 1)
        
        queue.append(source)
        distance[source] = 0
        visited[source] = True
        
        while queue:
            currNode = queue.pop()

            for nbr in graph[currNode]:
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr] = True
                    distance[nbr] = distance[currNode] + 6
        return distance
    
    def dfs(self, node, visited, graph, dfsAns):
        visited[node] = True
        dfsAns.append(node)
        
        for nbr in graph[node]:
            if not visited[nbr]:
                self.dfs(nbr, visited, graph, dfsAns)
    
    def depthFirstSearch(self, v, edges, source):
        graph = self.buildGraph(v, edges)
        visited = [False] * v
        dfsAns = []
        self.dfs(source, visited, graph, dfsAns)
        return dfsAns

if __name__ == '__main__':
    v = 6
    edges = [[0, 1], [0, 2], [0, 5], [1, 3], [1, 5], [2, 3], [3, 4], [4, 5]]
    dfs = DFS(v, edges, 0)
    
    for node in dfs.dfsAns:
        print(node, end=' ')