"""
Project 2 Hybrid Sorting Methods
This program is an implementation of the hybrid sorting algorithem

Author: Xiang Shan Tan

run:
python ./hybridsort.py [k value] [n value]
"""

import matplotlib.pyplot as plt
import random
import statistics
import sys
import time
from insertionsort import InsertionSort
from mergesort2 import Merge2

if len(sys.argv) < 3 :
    print("\nUsage: python hybridsort.py [k value] [n value]\n")
    sys.exit()

input = sys.argv

# get k value store in k
try:
    k = int(input[1])
except ValueError:
    print("\nThe k value must be an integer\n")
    sys.exit()

try:
    n = int(input[2])
except ValueError:
    print("\nThe n value must be an integer\n")
    sys.exit()

# k value cannot be negative or over 100
if k < 1 or k > 100:
    print("\nPlease try to give k value between 1 and 100\n")
    sys.exit()

# n value must be greater than or equal to k value
if n < k :
    print("\nFor the purpose of this project, please provide a n value, which is greater than k\n")
    sys.exit()

# max size of the random numbers can be generated
max = 100000
# array to store all randomized arrays
d = []


# random generate an array of values
# max: maximum value, n: length of the array
def numGen(size) :
    temp = []
    for x in range(size):
        temp.append(random.randint(1, max))
    return temp

# hybrid sorting algorithm.
# when n > k merge sort with 2 recursive call hybridsort function return as paramters
# until n <= k, then insertion sort.
def HybridSort(Array, k) :
    length = len(Array)
    if length > k :
        size = length // 2
        return Merge2(HybridSort(Array[0 : size], k), HybridSort(Array[size : length], k))
    else :
        return InsertionSort(Array)

def main() :
    # declare x, y values for plot
    x = []
    y = []
    # declare best time and best k value.
    bestT = -1
    bestK = 0
    file = open("Input.txt", "w")
    ## test arrays
    print("The system will generate 6 different sets of arrays!!")
    # generate 6 different array sets
    for i in range (6) :
        temp = numGen(n)
        file.write(f"Iteration {i+1}:\n")
        file.write(f"{temp}\n\n")
        #print(temp)
        d.append(temp)

    file.close()
    print("All data saved to a file: input.txt")

    # call HybridSort function
    for i in range (1, k + 1) :
        timeList = []
        for j in range(len(d)) :
            print(f"HybridSort k = {i}, interation {j+1} and n = {len(d[j])}")
            start = time.perf_counter()
            Array = HybridSort(d[j], i)
            end = time.perf_counter()
            timecount = end - start
            timeList.append(timecount)
            #print(Array)
            x.append(i)
            y.append(timecount)
        timer = statistics.mean(timeList)
        print(f"Hybrid Timer Median {timer}")
        if bestT == -1 or timer < bestT :
            bestT = timer
            bestK = i
    
    print("Best Record: ", bestT, bestK)
    plt.scatter(x, y)
    plt.ylabel("Timer (second)")
    plt.xlabel(f"K Value with Array Size: {n}")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
