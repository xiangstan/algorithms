import itertools
import matplotlib.pyplot as plt
import numpy as np
import platform
import random
import sys
import time

input = sys.argv

if len(sys.argv) < 2 :
    print("\nUsage: python exhaustive.py [number of total items]\n")
    sys.exit()

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
                    best.value = curvalue
                    best.combo = j
    return best

# greedy search
def greedy(n, values, weights) :
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
    return dataset

def main() :
    x = []
    # timer records for exhaustive search 
    ye = []
    # timer records for greedy search
    yg = []
    print("CS 5720 Design and Analysis of Algorithms")
    print("Project #1")
    print("Python Version: %s\n\n" % (platform.python_version()))

    for i in range(3, n+1):
        #run same n five times
        for j in range(5):
            # print iteration number
            print(f"\nIteration {i+1}:")
            # random assign values to array values
            values = numGen(1000)
            # random assign values to array weights
            weights = numGen(10000)
            # print values and weights
            print("Values: ", values)
            print("Weights", weights)

            # exhaustive search
            # start timer
            estart = time.time()
            # calculate possible combinations with number n
            best = exhaustive(n, values, weights)
            # calculate possibility with greedy search
            # stop timer
            estop = time.time()
            extimer = estop - estart

            # greedy search
            # start timer
            gstart = time.time()
            greedy(n, values, weights)
            # stop timer
            gstop = time.time()
            grtimer = gstop - gstart


            #print("\nBest Value: ", best.value, " Best Combo: ", best.combo)
            #print(f"Run Time: {extimer}.\n")
            ye.append(extimer)
            yg.append(grtimer)
            x.append(i)

    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)
    fig.tight_layout()
    ax1.scatter(x, ye)
    ax1.set_title("Exhaustive Search")
    ax2.scatter(x, yg)
    ax2.set_title("Greedy Search")
    plt.show()

if __name__ == "__main__":
    main()