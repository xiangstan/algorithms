def Knapsack(capacity, values, weights) :
    # create a multidimensional array to store total count of carried items
    v = len(values)
    w = len(weights)
    # initialize a capacity * weights array
    Count = [[0 for x in range(capacity + 1)] for x in range(w + 1)]

    print(0, Count[0])

    for i in range (1, w + 1) :
        for j in range (capacity + 1) :
            if weights[i - 1] > j :
                Count[i][j] = Count[i - 1][j]
            else :
                Count[i][j] = max(Count[i - 1][j], (values[i - 1] + Count[i - 1][j - weights[i - 1]]))
        print(i, Count[i])
    return Count[w][capacity]

def main() :
    values = [42, 12, 40, 25]
    weights = [7, 3, 4, 5]
    print(f"\nMaximum weight can be carried: {Knapsack(10, values, weights)}\n")

if __name__ == "__main__":
    main()

