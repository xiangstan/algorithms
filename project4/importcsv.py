"""
Project 4: Minimum Spanning Tree algorithm
This program imports data from CSV files

Author: Xiang Shan Tan

run:
python ./importcsv.py
"""

from pathlib import Path
import csv

# function to load and return file content 
def ImportCsv(file) :
    dataset = []
    with open(file, newline="") as csvfile :
        reader = csv.reader(csvfile)
        for row in reader :
            dataset.append(row)
    return dataset

def main() :
    file = Path(__file__).parent / "graphs" / "type_1" / "t1_graph_0.csv"
    print(ImportCsv(file))

if __name__ == "__main__":
    main()

