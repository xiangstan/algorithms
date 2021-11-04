from buknapsack import BUKnapsack
from mfknapsack import MFKnapsack
import matplotlib.pyplot as plt
import random
import sys
import time

maxValue = 500
inputs = [100, 200, 300, 400, 500, 600, 700, 800, 900]


# random generate an array of values
def numGen(max) :
    temp = []
    for x in range(inputs[-1]):
        temp.append(random.randint(1, max))
    return temp


def main() :
    avg = 5
    xb = []
    xm = []
    y = []
    values = numGen(maxValue)
    #print(values, "\n\n", weights)
    for i in range(100, 300, 10) :
        timerB = 0
        timerM = 0
        print(f"Input index: {i}, value: {i}")
        for j in range(avg) :
            weights = numGen(100)
            # Bottom Up
            start = time.perf_counter()
            result = BUKnapsack(i, values[0 : i], weights[0 : i])
            end = time.perf_counter()
            timerB = timerB + (end - start)

            # Top Down / Memoization
            Count = [[-1 for x in range(i + 1)] for x in range(i + 1)]
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
        xb.append(avgB)
        xm.append(avgM)
        y.append(i)
    print(xb)
    print(xm)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.scatter(y, xb, label="Bottom Up", color="red")
    ax1.scatter(y, xm, label="Top Down/Memoization", color="black")
    ax1.set_ylabel("Timer (second)")
    ax1.set_xlabel("Size of Capacity")
    ax1.set_title("Capacity vs Execution Time")
    ax1.legend()
    plt.show()

if __name__ == "__main__":
    main()
