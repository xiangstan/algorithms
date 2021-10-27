# Homework 6 Robot Coin Collection
# 
# Author: Xiang Shan Tan
#
# This implementation uses the idea in homework 6.
# Find maximum number of coins, which can be collected by robots.
# Robot can only move to the right or down.

f = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
check = [
    [0, 0, 0, 0, 1, 1],
    [0, 1, 1, 2, 2, 2],
    [0, 1, 1, 3, 3, 4],
    [0, 1, 2, 3, 3, 5],
    [1, 1, 2, 3, 4, 5],
]


def CoinCollection(Array) :
    # measure/store size of rows and columns
    rowsize = len(f)
    colsize = len(f[0])

    # initialize the value of [0, 0] point.
    f[0][0] = Array[0][0]
    # fill first row
    for i in range(colsize) :
        f[0][i] = f[0][i - 1] + Array[0][i]
    
    for i in range(1, rowsize) :
        f[i][1] = f[i - 1][i] + Array[i][1]
        #print(f[i])
        for j in range(1, colsize) :
            #print(f[i - 1][j], f[i][j - 1])
            f[i][j] = max(f[i - 1][j], f[i][j - 1]) + Array[i][j]
    print(f)
    return f[rowsize - 1][colsize - 1]

def main() :
    ## Test Arrays
    c = [
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0],
    ]
    collected = CoinCollection(c)
    print("Total coin collected: ", collected)

if __name__ == "__main__":
    main()

