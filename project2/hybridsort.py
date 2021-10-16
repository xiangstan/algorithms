"""
Project 2 Hybrid Sorting Methods
This program is an implementation of the hybrid sorting algorithem

Author: Xiang Shan Tan

run:
python ./hybridsort.py [k value] [n value]
"""

import matplotlib.pyplot as plt
import random
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
max = 1000
# array to store all randomized arrays
d = []
# preset all different sizes, each element is the percentage of the given array size n.
size = [20, 40, 60, 80, 100]


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
    # declare array of best times
    BestKs = []
    # open file input.txt
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

    fig, (ax1, ax2) = plt.subplots(2, 1)

    # call HybridSort function
    for s in size :
        # declare x, y values for plot
        x = []
        y = []
        # declare best time and best k value.
        bestT = -1
        bestK = 0
        # calculate partial size of array.
        partial = int(n * s / 100)
        print(f"Array size: {partial}")
        for i in range (1, k + 1) :
            timeSum = 0
            for j in range(len(d)) :
                #print(f"HybridSort k = {i}, interation {j+1} and n = {len(d[j])}")
                start = time.perf_counter()
                Array = HybridSort(d[j][0 : partial], i)
                end = time.perf_counter()
                timecount = end - start
                timeSum = timeSum + timecount
                #print(Array)
            timer = timeSum / len(d)
            x.append(i)
            y.append(timer)
            print(f"K: {i}, Hybrid Timer Average: {timer}")
            if bestT == -1 or timer < bestT :
                bestT = timer
                bestK = i
            print("Best Record: ", bestT, bestK)
        BestKs.append(bestK)
        ax1.plot(x, y, label=f"n = {partial}")
    ax1.set_ylabel("Timer (second)")
    ax1.set_xlabel(f"K Value with 5 different Array Sizes")
    ax1.set_title("Average Run Time")
    ax1.legend()

    ax2.scatter([int(s * n /100) for s in size], BestKs)
    ax2.set_xlabel("Size of n")
    ax2.set_ylabel(f"K Value with the Shortest Time")
    ax2.set_title("Optimal K Value of Array Length n")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

