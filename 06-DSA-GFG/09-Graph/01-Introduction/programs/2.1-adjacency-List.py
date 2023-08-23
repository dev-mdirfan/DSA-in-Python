# Adjacency List
class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class graph:
    def __init__(self, v) -> None:
        self.vertices = v
        self.graph = [None] * self.vertices
    
    def add_edge(self, source, destination):
        # Adding Source
        node = Node(destination)
        node.next = self.graph[source]
        self.graph[source] = node
        
        # Adding destination
        node = Node(source)
        node.next = self.graph[destination]
        self.graph[destination] = node
    
    def printGraph(self):
        for i in range(self.vertices):
            print(i, end='')
            temp = self.graph[i]
            while temp:
                print(' ->', temp.vertex, end='')
                temp = temp.next
            print()

if __name__ == '__main__':
    v = 5
    G = graph(v)
    G.add_edge(0, 1)
    G.add_edge(0, 4)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.printGraph()