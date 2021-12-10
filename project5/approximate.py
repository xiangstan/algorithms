"""
Project 5: Dynamic Programming Knapsack Problem

This program is the main program of Project 5. It find the max value from two greedy Knapsack algorithm and calcualte the approximation ratio against an optimal dynamic programming Knapsack solution.

The optimal dynamic programming Knapsack solution is the button up Knapsack algorithm from Project 3.

Author: Xiang Shan Tan

run:
python ./approximate.py
"""

from buknapsack import BUKnapsack
from greedy import Greedy
from valueweight import ValueWeight
import matplotlib.pyplot as plt
import numpy as np


def main() :
    # total capacity
    capacity = 100
    # highest value
    val = 10
    # total items
    items = 50

    count = 100000
    #count = 1000

    # initialize empty arrays for plotting
    y = []
    y = []
    x = []

    # counter to calculate average approximation ratio
    sum = 0

    print("Program started...")

    for i in range(count) :
        weights = np.random.randint(1, capacity + 1, size = items)
        values = np.random.randint(1, val + 1, size = items)
        
        greedy1 = Greedy(items, values, weights, capacity)
        greedy2, weight2, sorted = ValueWeight(items, values, weights, capacity)
        approx = max(greedy1, greedy2)

        Count = [[0 for x in range(capacity + 1)] for x in range(items + 1)]
        bu = BUKnapsack(capacity, values, weights, Count)
        #print(approx, bu)

        temp = bu / approx
        sum += temp

        y.append(temp)
        x.append(i)
        if i > 0 and i % 1000 == 0 :
            print(f"Iteration {i}, {i * 100 / count}% completed...")

    y.sort(reverse = True)
    # initialize plot figure
    print(f"\nThe approximation ratio of this greedy algorithm acorss all trails is {sum / count}\n")
    print("Generate Plot...")
    plt.scatter(x, y)
    plt.ylabel("Ratio r(x)")
    plt.xlabel("Instance")
    plt.title("Approximation vs Optimal DP")
    plt.show()


if __name__ == "__main__":
    main()


