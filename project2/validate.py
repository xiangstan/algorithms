"""
Project 2 Hybrid Sorting Algorithm
This program validates the designed hybrid sorting algorithm against Python build-in sorting function

Author: Xiang Shan Tan

run:
python ./validate.py
"""

import random
from insertionsort import InsertionSort
from mergesort2 import Merge2

def HybridSort(Array) :
    length = len(Array)
    if length > 2 :
        size = length // 2
        return Merge2(HybridSort(Array[0 : size]), HybridSort(Array[size : length]))
    else :
        return InsertionSort(Array)

def main() :
    max = 1000
    i = 10
    while i <= 100 :
        print(f"New Iteration: array size {i}\n")
        a = []
        for j in range(i) :
            a.append(random.randint(1, max))
        print("Array:\n", a)
        hybrid = HybridSort(a)
        a.sort()
        print("hybrid:\n", hybrid)
        print("builtin:\n", a)
        if hybrid == a :
            print("Hybrid sorting provides the same result as Python the built-in sorting function\n")
        else :
            print("Hybrid sorting gives different result than the Python Built-in sorting function\n")
        i = i + 10

if __name__ == "__main__":
    main()

