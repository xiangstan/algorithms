import itertools
import matplotlib.pyplot as plt
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

# exhaustive research
def exhaustive(n) :
    best = BestSet()
    # random assign values to array values
    values = numGen(1000)
    # random assign values to array weights
    weights = numGen(10000)
    # print values and weights
    print("Values: ", values)
    print("Weights", weights, "\n")

    for i in range(n):
        combi = [",".join(map(str, c)) for c in itertools.combinations(range(0, n), i+1)]
        #print(combi)
        for j in combi:
            #print(j)
            curvalue = 0
            curweight = 0
            dataset = j.split(",")
            for k in dataset:
                #print(values[int(k)])
                curvalue += int(values[int(k)])
                curweight += int(weights[int(k)])
                #print(k)
            #print(j.split(","))
            #print(curvalue)
            #print(curweight)
            if curweight < limit:
                print("Possible Solution: ", j, " Total Value: ", curvalue, " Total Weight: ", curweight)
                if curvalue > best.value:
                    best.value = curvalue
                    best.combo = j
    return best


def main() :
    x = []
    y = []
    print("CS 5720 Design and Analysis of Algorithms")
    print("Project #1")
    print("Python Version: %s\n\n" % (platform.python_version()))

    for i in range(3, n+1):
        #run same n five times
        for j in range(5):
            # print iteration number
            print(f"Iteration {i+1}:")
            # start timer
            start = time.time()
            # calculate possible combinations with number n
            best = exhaustive(n)
            # stop timer
            stop = time.time()
            timer = stop - start
            #print("\nBest Value: ", best.value, " Best Combo: ", best.combo)
            #print(f"Run Time: {timer}.\n")
            y.append(timer)
            x.append(i)
    plt.scatter(x, y, c ="blue")
    plt.xlabel("n Times")
    plt.ylabel("Time (sec)")
    plt.show()

if __name__ == "__main__":
    main()