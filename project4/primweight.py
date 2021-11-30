"""
Project 4: Minimum Spanning Tree algorithm
This program is the implemetation of Prim algorithm using weight matrix

Author: Xiang Shan Tan

run:
python ./primweight.py
"""

from importcsv import ImportCsv
from count import CountNodes
from pathlib import Path

# e edges and v vertices
def PrimWeight(graph) :
    # initial empty minimum spanning tree array
    mst = []
    # calculate the total number of nodes
    nodes = CountNodes(graph)
    # initial empty edge array
    edges = nodes - 1
    # initialize visited nodes, and the value of its first node visited[0]
    visited = []
    for i in range(nodes) :
        visited.append(0)
    visited[0] = 1
    total = 0

    #print(visited)
    while edges > 0 :
        min = float("inf")
        x = 0
        y = 0
        weight = 0
        for i in range(nodes) :
            if visited[i] == 1 :
                for j in range(nodes) :
                    weight = float(graph[i][j])
                    if visited[j] == 0 and weight > 0:
                        #print(f"Weight: {weight}")
                        if min > weight :
                            min = weight
                            x = i
                            y = j
                            #print(f"I am here {x, y, weight}")
        #print(f"{x} - {y} : {str(graph[x][y])}")
        visited[y] = 1
        #print(f"Visited: {visited}")
        edges -= 1
        #print(f"Weight: {min}")
        total += min
        mst.append([x, y, min])

    return mst, total

def main() :
    file = Path(__file__).parent / "graphs" / "type_1" / "t1_graph_0.csv"
    graph = [
        [-1, 5, -1, 3, 4, -1],
        [5, -1, 3, -1, 4, -1],
        [-1, 3, -1, -1, 2, 3],
        [3, -1, -1, -1, 1, -1],
        [4, 4, 2, 1, -1, 3],
        [-1, -1, 3, -1, 3, -1]
    ]
    data = ImportCsv(file)
    #print(PrimWeight(graph))
    result, weight = PrimWeight(data)
    print(result)
    print(weight)
    

if __name__ == "__main__":
    main()
