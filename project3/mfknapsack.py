"""
Project 3: Dynamic Programming Knapsack Problem
This program is the implementation of Memoization aproach of Knapsack problem.

Author: Xiang Shan Tan

run:
python ./mfknapsack.py
"""

Count = []
values = [42, 12, 40, 25]
weights = [7, 3, 4, 5]
capacity = 10
w = len(weights)
Count = [[-1 for x in range(capacity + 1)] for x in range(w + 1)]

def MFKnapsack(i, j, wt, val) :
    if Count[i][j] < 0 :
        if wt[i - 1] > j :
            val = MFKnapsack(i - 1, j, wt, val)
        else :
            print("Val is: ", max(MFKnapsack(i - 1, j, wt, val), values[i - 1] + MFKnapsack(i - 1, j - wt[i - 1], wt, val)))
            val = max(MFKnapsack(i - 1, j, wt, val), values[i - 1] + MFKnapsack(i - 1, j - wt[i - 1], wt, val))

        Count[i][j] = val

    return Count[i][j]


def main() :
    for i in range(len(Count[0])) :
        Count[0][i] = 0
    for i in range(len(Count)) :
        print(i, Count[i])

    result = MFKnapsack(w, capacity, weights, len(values))
    for i in range(len(Count)) :
        print(i, Count[i])

    print(f"\nMaximum weight can be carried: {result}\n")

if __name__ == "__main__":
    main()

