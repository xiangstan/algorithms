from buknapsack import BUKnapsack
import math
import matplotlib.pyplot as plt
import random
import time

maxValue = 500
avg = 5

def main() :
    capacity = []
    values = []
    weights = []
    x = []
    y = []

    for i in range(1, 10) :
        capacity = i * 100
        # append value of x axis
        x.append(math.floor(math.log2(i * 100)) + 1)

        print(f"Capacity = {capacity}:")

        # generate weights and values array on the fly
        weights.append(random.randint(1, capacity))
        values.append(random.randint(1, maxValue))
        # generate Count array
        Count = [[-1 for x in range(capacity + 1)] for x in range(capacity + 1)]

        # initialize timer counter.
        timerB = 0
        for j in range(avg) :
            start = time.perf_counter()
            result = BUKnapsack(capacity, values, weights, Count)
            end = time.perf_counter()
            timerB = timerB + (end - start)
        # compute average timer
        avgB = timerB / avg
        print(f"Average Timer: {timerB}")
        # append value of y axis
        y.append(avgB)
    plt.scatter(x, y)
    plt.ylabel("Timer (second)")
    plt.xlabel("Size of W")
    plt.title("Size of W vs Execution Time")
    plt.show()


if __name__ == "__main__":
    main()

