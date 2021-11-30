from count import CountNodesEdges
from importcsv import ImportCsv
from pathlib import Path
from primweight import PrimWeight
import matplotlib.pyplot as plt
import os
import sys
import time

path = Path(__file__).parent / "graphs"

if not os.path.isdir(path) :
    print(f"\nDirectory '{path}' not found.\n")
    sys.exit()

def main() :
    dataset = []
    # array to store all edge counts
    counts = {
        "edge": {},
        "node": {}
    }
    timer = {
        "weightmatrix": {}
    }
    totalweight = {
        "weightmatrix": {}
    }
    print(f"\nReading files under directory {path} ...\n")
    # initialize plot figure
    fig, (ax1, ax2) = plt.subplots(2, 1)

    x = []

    # main loop
    for i in range(2) :
        counts["node"]["type" + str(i + 1)] = []
        counts["edge"]["type" + str(i + 1)] = []
        timer["weightmatrix"]["type" + str(i + 1)] = []
        totalweight["weightmatrix"]["type" + str(i + 1)] = []
        print(f"Type {i + 1}")
        for j in range(10) :
            # load data from csv file
            file = path / Path("type_" + str(i + 1)) / Path("t" + str(i + 1) + "_graph_" + str(j) + ".csv")
            data = ImportCsv(file)

            # calcualte node and edge
            nodes, edges = CountNodesEdges(data)
            # save node and edge into dictionary "counts"
            counts["node"]["type" + str(i + 1)].append(nodes)
            counts["edge"]["type" + str(i + 1)].append(edges)
            #print(f"File t{str(i + 1)}_graph_{str(j)}.csv => Node: {nodes}, Edge: {edges}")

            # total weight
            # per project requirement, data retrieve as result will not need to be stored
            start = time.perf_counter()
            result, weight = PrimWeight(data)
            end = time.perf_counter()
            timer["weightmatrix"]["type" + str(i + 1)].append(end - start)
            # save weight value into disctoary "totalweight"
            totalweight["weightmatrix"]["type" + str(i + 1)].append(weight)
            if j == 0 :
                print("{:<25} {:<10} {:<10} {:<10}".format("File", "Nodes", "Edges", "Weight"))
                print("{:<25} {:<10} {:<10} {:<10}".format("---------------", "-----", "-----", "-----"))
            print("{:<25} {:<10} {:<10} {:<10}".format(f"t{str(i + 1)}_graph_{str(j)}.csv", nodes, edges, weight))
            if i == 0 :
                x.append(nodes)
        print("\n")

    print(f"{totalweight}\n")
    print(f"{timer}\n")
    ax1.scatter(counts["node"]["type1"], counts["edge"]["type1"], label="Type 1", color="red")
    ax1.scatter(counts["node"]["type2"], counts["edge"]["type2"], label="Type 2", color="black")
    ax1.set_ylabel("Total Edges")
    ax1.set_xlabel("Total Nodes")
    ax1.set_title("Edge vs Node")
    ax1.legend()
    ax2.scatter(x, timer["weightmatrix"]["type1"], label="Type 1", color="red")
    ax2.scatter(x, timer["weightmatrix"]["type2"], label="Type 2", color="black")
    ax2.set_ylabel("Time Comsuming")
    ax2.set_xlabel("Total Nodes")
    ax2.set_title("Execution Time vs Node")
    ax2.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

