"""
Project 5: Dynamic Programming Knapsack Problem

This program is the implementation of greedy Knapsack algorithm. It is an updated version of greedy algorithm from project 1.

Author: Xiang Shan Tan

run:
python ./greedy.py
"""

import numpy as np

def Greedy(n, values, weights, capacity) :
    # get the index by sorting values from highest to lowest
    sort = np.argsort(values)[::-1]
    print(f"Sorted Array: {sort}")

    curvalue = 0
    curweight = 0
    valueset = []
    weightset = []
    #print("Sorted dataset: ", sort)
    for i in (sort):
        valueset.append(values[i])
        weightset.append(weights[i])

        temp = curweight + weights[i]
        if temp <= capacity :
            curvalue += values[i]
            curweight = temp
    #print("Sorted Values: ", valueset)
    #print("Sorted Weight: ", weightset)
    #print(curvalue)
    #print(curweight)
    return curvalue

def main() :
    # total capacity
    capacity = 10
    # highest value
    val = 10
    # total items
    items = 5

    count = 1
    #count = 10
    for i in range(count) :
        weights = np.random.randint(1, capacity + 1, size = items)
        values = np.random.randint(1, val + 1, size = items)
        print(f"Weights: {weights}")
        print(f"Values: {values}")
        
        g1 = Greedy(items, values, weights, capacity)
        print(g1)

if __name__ == "__main__":
    main()

