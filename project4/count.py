"""
Project 4: Minimum Spanning Tree algorithm
This program counts the number of nodes and edges of a given graph.

Author: Xiang Shan Tan

run:
python ./count.py
"""

from importcsv import ImportCsv
from pathlib import Path
import pandas as pd

def CountNodes(graph) :
    node = len(graph)
    return node

def CountNodesEdges(graph) :
    edge = 0
    for i in range(len(graph)) :
        for j in range(len(graph[i])) :
            if i > j :
                if float(graph[i][j]) > 0 :
                    edge += 1
            else :
                break
    return CountNodes(graph), edge


def main() :
    path = Path(__file__).parent / "graphs" / "type_1" / "t1_graph_0.csv"
    data = ImportCsv(path)
    print(pd.DataFrame(data))
    nodes, edges = CountNodesEdges(data)
    print(nodes, edges)

if __name__ == "__main__":
    main()
