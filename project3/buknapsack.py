"""
Project 3: Dynamic Programming Knapsack Problem
This program is the implementation of Bottom Up aproach of Knapsack problem.

Author: Xiang Shan Tan

run:
python ./buknapsack.py
"""

def BUKnapsack(capacity, values, weights) :
    # create a multidimensional array to store total count of carried items
    v = len(values)
    w = len(weights)
    # initialize a capacity * weights array
    Count = [[0 for x in range(capacity + 1)] for x in range(w + 1)]

    #print(0, Count[0])

    for i in range (1, w + 1) :
        for j in range (capacity + 1) :
            if weights[i - 1] > j :
                Count[i][j] = Count[i - 1][j]
            else :
                Count[i][j] = max(Count[i - 1][j], (values[i - 1] + Count[i - 1][j - weights[i - 1]]))
        #print(i, Count[i])
    return Count[w][capacity]

def main() :
    values = [50, 47, 13, 7, 9, 17, 46, 47, 7, 49]
    weights = [15, 17, 5, 12, 16, 4, 2, 12, 19, 20]
    print(f"\nMaximum weight can be carried: {BUKnapsack(10, values, weights)}\n")

if __name__ == "__main__":
    main()

