import itertools
import matplotlib.pyplot as plt
import numpy as np
import platform
import random
import sys
import time
from matplotlib.gridspec import  GridSpec
from greedy import Greedy

if len(sys.argv) < 2 :
    print("\nUsage: python knapsack.py [number of total items]\n")
    sys.exit()

input = sys.argv

try:
    n = int(input[1])
except ValueError:
    print("\nThe number of total items must be an integer\n")
    sys.exit()

if n < 1 :
    print("The number of total items need to be more than 0\n")


limit = 10000   # Weight limit: W
values = []     # array of values in corresponding to items
weights = []    # array of weights in corresponding to items 

class BestSet :
    def __init__(self):
        self.value = 0
        self.weight = 0
        self.combo = ""

# random generate an array of values
def numGen(max) :
    temp = []
    for x in range(n):
        temp.append(random.randint(1, max))
    return temp

data = ""

# exhaustive search
def exhaustive(n, values, weights) :
    best = BestSet()
    for i in range(n):
        combi = [",".join(map(str, c)) for c in itertools.combinations(range(0, n), i+1)]
        for j in combi:
            curvalue = 0
            curweight = 0
            dataset = j.split(",")
            for k in dataset:
                curvalue += int(values[int(k)])
                curweight += int(weights[int(k)])
            if curweight < limit:
                #print("Possible Exhaustive Search Solution: ", j, " Total Value: ", curvalue, " Total Weight: ", curweight)
                if curvalue > best.value:
                    best.combo = j
                    best.value = curvalue
                    best.weight = curweight
    return best

# greedy search
"""
def greedy(n, values, weights) :
    best = BestSet()
    sort = np.argsort(values)[::-1] # get the index by sorting values from highest to lowest

    curvalue = 0
    curweight = 0
    dataset = []
    valueset = []
    weightset = []
    #print("Sorted dataset: ", sort)
    for i in (sort):
        valueset.append(values[i])
        weightset.append(weights[i])

        temp = curweight + weights[i]
        if temp < limit :
            curvalue += values[i]
            curweight += weights[i]
            dataset.append(i)
    #print("Sorted Values: ", valueset)
    #print("Sorted Weight: ", weightset)
    #print(dataset)
    #print(curvalue)
    #print(curweight)
    best.combo = dataset
    best.value = curvalue
    best.weight = curweight
    return best
"""

def main() :
    x = []
    # timer records for exhaustive search 
    yte = []
    # timer records for greedy search
    ytg = []
    # value records for exhaustive search
    yve = []
    # value records for gready search
    yvg = []
    # weight records for exhaustive search
    ywe = []
    # weight records for gready search
    ywg = []
    # best value by exhaustive algo / greedy algo
    ratio = []

    print("CS 5720 Design and Analysis of Algorithms")
    print("Project #1")
    print("Python Version: %s\n\n" % (platform.python_version()))

    file = open("Input.txt", "w")

    for i in range(3, n+1):
        #run same n five times
        for j in range(5):
            # print iteration number
            print(f"\nIteration {i}:")
            # random assign values to array values
            values = numGen(1000)
            # random assign values to array weights
            weights = numGen(10000)
            # print values and weights
            print("Values: ", values)
            print("Weights", weights)
            file.write(f"Iteration {i}, dataset {j+1}:\n")
            file.write(f"Values: {values}\n")
            file.write(f"Weights: {weights}\n")

            # exhaustive search
            # start timer
            estart = time.time()
            # calculate possible combinations with number n
            bestex = exhaustive(n, values, weights)
            # calculate possibility with greedy search
            # stop timer
            estop = time.time()
            extimer = estop - estart

            # greedy search
            # start timer
            gstart = time.time()
            bestgr = Greedy(n, values, weights)
            # stop timer
            gstop = time.time()
            grtimer = gstop - gstart


            #print("\nBest Value: ", best.value, " Best Combo: ", best.combo)
            #print(f"Run Time: {extimer}.\n")
            yte.append(extimer)
            yve.append(bestex.value)
            ywe.append(bestex.weight)
            ytg.append(grtimer)
            yvg.append(bestgr.value)
            ywg.append(bestgr.weight)
            ratio.append(bestex.value / bestgr.value)
            x.append(i)
        file.write("\n")

    file.close()

    grid = plt.GridSpec(2, 2, left = 0.1, bottom = .15, right = .94, top = .94, wspace = .25, hspace = .25)
    fig = plt.figure()
    fig.clf()
    fig.suptitle("Figures for Project 1\nExchaustive: blue, Greedy: green")

    ax1 = fig.add_subplot(grid[0, 0])
    ax1.scatter(x, yte, c = "blue")
    ax1.scatter(x, ytg, c = "green")
    ax1.set_title("Execute Timer")

    ax2 = fig.add_subplot(grid[0, 1])
    ax2.scatter(x, ywe, c = "blue")
    ax2.scatter(x, ywg, c = "green")
    ax2.set_title("Weight")

    ax5 = fig.add_subplot(grid[1, :])
    ax5.scatter(x, ratio)
    ax5.set_title("Best Value by Exhaustive Algo / Greedy Algo")

    plt.subplots_adjust(left = 0.1,
                    bottom = 0.1, 
                    right = 0.9, 
                    top = 0.9, 
                    wspace = 0.4, 
                    hspace = 0.4)

    plt.show()

if __name__ == "__main__":
    main()