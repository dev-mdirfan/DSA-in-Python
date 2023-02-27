# For Undirected Graph
if __name__ == '__main__':
    # v is the number of vertices
    # edge is the edges
    vertices, edges = map(int, input().split())
    adjacencyMatrix = [[0 for i in range(vertices)] for j in range(vertices)]
    for i in range(vertices):
        u, v = map(int, input().split())
        adjacencyMatrix[u][v] = 1
        adjacencyMatrix[v][u] = 1
        # for a directed graph we only need to store from u to, we just assign
        # adjacency[u][v] = 1
