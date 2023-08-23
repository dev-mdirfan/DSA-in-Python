There are two ways to store a graph:

1. Adjacency Matrix
2. Adjacency List

## 1. Adjacency Matrix

In this method, the graph is stored in the form of the 2D matrix where rows and columns denote vertices. Each entry in the matrix represents the weight of the edge between those vertices.

![Adjacency Matrix](media/adjacency_mat1.jpg)

## 2. Adjacency List

  

This graph is represented as a collection of linked lists. There is an array of pointer which points to the edges connected to that vertex.

  

![Adjacency List](media/adjacency_list.jpg)

### Comparison between Adjacency Matrix and Adjacency List

When the graph contains a large number of edges then it is good to store it as a matrix because only some entries in the matrix will be empty. An algorithm such as Prim’s and Dijkstra adjacency matrix is used to have less complexity.

|Action |Adjacency Matrix|Adjacency List|
|---|---|---|
|Adding Edge |$O(1)$|$O(1)$|
|Removing an Edge |$O(1)$|$O(N)$|
|Initializing|$O(N*N)$|$O(N)$|



