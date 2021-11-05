from buknapsack import BUKnapsack
from mfknapsack import MFKnapsack
import matplotlib.pyplot as plt
import random
import sys
import time

sys.setrecursionlimit(2000)

if len(sys.argv) < 2 :
    maxWeight = 100
else :
    input = sys.argv
    maxWeight = int(input[1])

maxValue = 500
items = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

print(maxWeight)
# random generate an array of values
def numGen(max, set) :
    temp = []
    for x in range(set[-1]):
        temp.append(random.randint(1, max))
    return temp


def main() :
    avg = 5
    ixb = []
    ixm = []
    wxb = []
    wxm = []
    y1 = []
    y2 = []
    values = numGen(maxValue, items)
    print("Number of items vs Time")
    for i in range(100, 1001, 5) :
        timerB = 0
        timerM = 0
        Count = [[-1 for x in range(i + 1)] for x in range(i + 1)]
        print(f"Item index: {i}")
        for j in range(avg) :
            weights = numGen(maxWeight, items)
            # Bottom Up
            start = time.perf_counter()
            result = BUKnapsack(maxWeight, values[0 : i], weights[0 : i], Count)
            end = time.perf_counter()
            timerB = timerB + (end - start)

            # Top Down / Memoization
            for k in range(len(Count[0])) :
                Count[0][k] = 0
            start = time.perf_counter()
            result = MFKnapsack(i, i, weights[0 : i], values[0 : i], Count)
            end = time.perf_counter()
            timerM = timerM + (end - start)

        avgB = timerB / avg
        avgM = timerM / avg

        print(f"Bottom-up result is {result}, execution time is {avgB}")
        print(f"Memoization result is {result}, execution time is {avgM} \n")
        ixb.append(avgB)
        ixm.append(avgM)
        y1.append(i)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.scatter(y1, ixb, label="Bottom Up", color="red")
    ax1.scatter(y1, ixm, label="Top Down/Memoization", color="black")
    ax1.set_ylabel("Timer (second)")
    ax1.set_xlabel("Size of Items")
    ax1.set_title("Items vs Execution Time")
    ax1.legend()
    print("Weights vs Time")
    for i in range(1, maxWeight) :
        weightB = 0
        weightM = 0
        print(f"Weight index: {i}")
        for j in range(avg) :
            # random generate weights array, if programming specific weight, the maximum value of randomly generate value 
            # is the specific weight.
            # otherwise default 100
            weights = numGen(i if maxWeight == 100 else maxWeight, items)
            # Bottom Up
            CountB = [[0 for x in range(500 + 1)] for x in range(500 + 1)]
            start = time.perf_counter()
            result = BUKnapsack(i, values[0 : 500], weights[0 : 500], CountB)
            end = time.perf_counter()
            weightB = weightB + (end - start)

            # Top Down / Memoization
            CountM = [[-1 for x in range(500 + 1)] for x in range(500 + 1)]
            for k in range(len(CountM[0])) :
                CountM[0][k] = 0
            start = time.perf_counter()
            result = MFKnapsack(i, i, values[0 : 500], weights[0 : 500], CountM)
            end = time.perf_counter()
            weightM = weightM + (end - start)

        avgB = weightB / avg
        avgM = weightM / avg

        print(f"Bottom-up result is {result}, execution time is {avgB}")
        print(f"Memoization result is {result}, execution time is {avgM} \n")
        wxb.append(avgB)
        wxm.append(avgM)
        y2.append(i)
    ax2.scatter(y2, wxb, label="Bottom Up", color="red")
    ax2.scatter(y2, wxm, label="Top Down/Memoization", color="black")
    ax2.set_ylabel("Timer (second)")
    ax2.set_xlabel(f"Size of Capacity: Maximum {maxWeight}")
    ax2.set_title("Capacity vs Execution Time")
    ax2.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
