# array of all solutions
count = []

def BottomUp (n, coins) :
    # solution 0 is always 0
    count.append(0)
    for i in range (1, n) :
        # make the temperory highest count to be higher than the total amount of coin counts.
        temp = len(count) + 1
        m = len(coins)
        j = 1
        while  j < m and i >= coins[j]  :
            temp = min(temp, count[i - coins[j]])
            j += 1
        count.append(temp + 1)
    return count[n - 1]

def main() :
    coins = [1, 3, 4]
    total = 10
    print("Total number of coins: ", BottomUp(total, coins))

if __name__ == "__main__":
    main()
