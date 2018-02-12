# dijkstra_python
Lazy implementation of dijkstra using python3

## Input Format
Each line contains 3 integers separated by a space (sourceNodeId destinationNodeId edgeWeight)
The very last line represents the start node and the goal node, to calculate the shortest path

## Sample Input:
```
13 1 12
8 13 13
5 3 6
5 8 5
3 1 10
1 8 20
2 8 16
2 13 3
13 2 5
13 5 4
2 8 
```


## Sample Output:
```
Starting vertex: 2
Ending vertex: 8
The shortest path is:

Vertex 2 to vertex 13 (edge weight of 3)
Vertex 13 to vertex 5 (edge weight of 4)
Vertex 5 to vertex 8 (edge weight of 5)
```
