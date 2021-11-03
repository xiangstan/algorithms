Count = []
values = [42, 12, 40, 25]
weights = [7, 3, 4, 5]
capacity = 10
w = len(weights)
Count = [[-1 for x in range(capacity + 1)] for x in range(w + 1)]

def Knapsack(i, j) :
    if Count[i][j] < 0 :
        if weights[i - 1] > j :
            val = Count[i][j]
        else :
            #print("i and j: ", i, j)
            #print("Values: ", values[i - 1])
            #print(f"Recursive call: Knapsack({i - 1}, j - weights[{i - 1}])")
            #print("Knapsak: ", Knapsack(i - 1, j - weights[i - 1]))
            #print("Value sum: ", values[i - 1] + Knapsack(i - 1, j - weights[i - 1]))
            print("Val is: ", max(Knapsack(i - 1, j), values[i - 1] + Knapsack(i - 1, j - weights[i - 1])))
            val = max(Knapsack(i - 1, j), values[i - 1] + Knapsack(i - 1, j - weights[i - 1]))

        Count[i][j] = val

    return Count[i][j]


def main() :
    for i in range(len(Count[0])) :
        Count[0][i] = 0
    for i in range(len(Count)) :
        print(i, Count[i])
    

    result = Knapsack(w, capacity)
    for i in range(len(Count)) :
        print(i, Count[i])

    print(f"\nMaximum weight can be carried: {result}\n")

if __name__ == "__main__":
    main()

