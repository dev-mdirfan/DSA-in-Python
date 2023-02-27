# For directed Graph
if __name__ == '__main__':
    vertices, edges = map(int, input().split())
    adjacencyMatrix = [[0 for i in range(vertices)] for j in range(vertices)]
    for i in range(vertices):
        u, v = map(int, input().split())
        adjacencyMatrix[u][v] = 1