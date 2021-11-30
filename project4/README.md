# Minimum Spanning Tree Algorithm

This project is to implement a Minimum Spanning Tree (MST) algorithm.

Load the example graphs and programmatically count their nodes and edges.
Write code which reads the CSV files and loads the graphs into memory. You may use any
graph representation you wish. For each graph, your code should determine both the number
of nodes and the number of edges.
Deliverable 1: A table which reports the exact number of nodes and edges for each of
the 20 graphs. You will be graded in part on the correctness of these values; please clearly
state which graph yields which values. Note: the values in this table must be obtained using
code, not by counting by hand. If I can't verify that your code works, I may provide you
with additional graph examples and ask you to demonstrate that your code is computing the
values.

## Deliverables

### Deliverable 1

Display a table which reports the exact number of nodes and edges for each of the 20 graphs.

### Deliverable 2

For each of the 2 types, provide your conjecture about whether the type is sparse (that is, its graphs satisfy |E| in O(|V|)) or dense (that is, its graphs satisfy |E| in Theta (|V|^2)).

### Deliverable 3

Implement the algorithm to determine the MST of all imported graphs. Choose one of the MST algorithm below:

1. Prim's using weight matrix,
1. Prim's using adjacency list,
1. Kruskal's using adjacency list.

### Deliverable 4

An estimate of the time complexity of your algorithm for each of the two types of graph.


## Files

| Filename | Description |
|--- |--- |
| [count.py](count.py) | Count the number of nodes and edges of given graph from CSV file. |
| [importcsv.py](importcsv.py) | Function to import data from a selected CSV file. |
| [mst.py](compare.py) | Main program delivers all deliverables of this project. |
| [primweight.py](primweight.py) | Function to calculate the minimum weight with the Prim algorithm using weight matrix. |
