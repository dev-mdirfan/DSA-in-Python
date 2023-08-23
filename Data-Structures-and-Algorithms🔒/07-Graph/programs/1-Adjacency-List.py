from collections import deque

class AdjacencyList:
    def __init__(self, vertices, edges, source):
        self.v = vertices
        self.edges = edges
        self.s = source
    
    def buildGraph(self):
        graph = [[] for i in range(self.v + 1)]
        for edge in self.edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])      # Remove in case of directed graph
        return graph
    
    def printGraph(self):
        print("Adjacency List:- ")
        graph = self.buildGraph()
        for node in range(1, self.v + 1):
            print(node, ':', end='')
            for nbr in graph[node]:
                print(' ->', nbr, end='')
            print()

if __name__ == '__main__':
    vertices = 6
    edges = [[1, 2], [1, 4], [1, 5], [2, 3], [2, 4], [3, 4], [3, 6], [4, 5], [5, 6]]
    source = 1      # Node start from 1
    graph = AdjacencyList(vertices, edges, source)
    graph.printGraph()