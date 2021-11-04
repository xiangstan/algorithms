"""
Project 3: Dynamic Programming Knapsack Problem
This program is the implementation of Memoization aproach of Knapsack problem.

Author: Xiang Shan Tan

run:
python ./mfknapsack.py
"""

Count = []
#values = [42, 12, 40, 25]
#weights = [7, 3, 4, 5]
values = [22, 8, 47, 28, 7, 34, 19, 17, 5, 23]
weights = [3, 17, 17, 14, 2, 9, 3, 19, 20, 20]
capacity = 10
w = len(weights)

def MFKnapsack(i, j, wt, values, Count) :
    #print("MFKnapsack: ", i, j)
    if Count[i][j] < 0 :
        if wt[i - 1] > j :
            val = MFKnapsack(i - 1, j, wt, values, Count)
        else :
            #print("Val is: ", max(MFKnapsack(i - 1, j, wt, val), values[i - 1] + MFKnapsack(i - 1, j - wt[i - 1], wt, val)))
            val = max(MFKnapsack(i - 1, j, wt, values, Count), values[i - 1] + MFKnapsack(i - 1, j - wt[i - 1], wt, values, Count))

        Count[i][j] = val
    #print(i, Count[i])
    return Count[i][j]


def main() :
    Count = [[-1 for x in range(capacity + 1)] for x in range(w + 1)]
    for i in range(len(Count[0])) :
        Count[0][i] = 0
    for i in range(len(Count)) :
        print(i, Count[i])
    result = MFKnapsack(w, capacity, weights, values, Count)
    #for i in range(len(Count)) :
    #    print(i, Count[i])

    print(f"\nMaximum weight can be carried: {result}\n")

if __name__ == "__main__":
    main()

