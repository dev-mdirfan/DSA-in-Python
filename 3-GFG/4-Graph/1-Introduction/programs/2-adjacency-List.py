# A class represents the adjacency list of the node
class adjNode:
    def __init__(self, data) -> None:
        self.vertex = data
        self.next = None

# A class is represents a graph. A graph is the list of the adjacency lists.

class graph:
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = [None] * self.v
    
    def add_edge(self, src, dest):
        # Adding source node
        node = adjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        
        # Adding destination node
        node = adjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    
    def print_graph(self):
        for i in range(self.v):
            print('Adjacency List of vertex {}\n head'.format(i), end='')
            temp = self.graph[i]
            while temp:
                print(' -> {}'.format(temp.vertex), end='')
                temp = temp.next
            print('\n')

if __name__ == '__main__':
    v = 5
    Graph = graph(v)
    Graph.add_edge(0, 1)
    Graph.add_edge(0, 4)
    Graph.add_edge(1, 2)
    Graph.add_edge(1, 3)
    Graph.add_edge(1, 4)
    Graph.add_edge(2, 3)
    Graph.add_edge(3, 4)
    
    Graph.print_graph()
