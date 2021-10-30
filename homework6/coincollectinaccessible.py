# Homework 6 Robot Coin Collection
# 
# Author: Xiang Shan Tan
#
# This implementation uses the idea in homework 6.
# Find maximum number of coins, which can be collected by robots.
# Robot can only move to the right or down.
# -1 means the cell is inaccessible for the robot.

# initialize a global multidementional array to store all steps of collected coins
f = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
# result of test array supposed to get

# check if the selected cell is inaccessible.
# paramters:
#   check: the value of top/left cell of the selected cell
#   add: the pre-defined value of selected cell in Array
# return -1 if either check or add has a value of -1
# otherwise return the cell value + the add value
def CheckInacc(check, add) :
    if add < 0 or check < 0 :
        if add > 0 :
            return -1
        else :
            return -9
    else :
        return check + add

def CoinCollection(Array) :
    # measure/store size of rows and columns
    rowsize = len(f)
    colsize = len(f[0])

    # initialize the value of [0, 0] point.
    f[0][0] = Array[0][0]

    # fill first row
    for i in range(colsize) :
        f[0][i] = CheckInacc(f[0][i - 1], Array[0][i])
    # print the first row of collected coins
    print(f[0])
    
    for i in range(1, rowsize) :
        #print(Array[i][0])
        f[i][0] = CheckInacc(f[i - 1][0], Array[i][0])
        #print(f[i])
        for j in range(1, colsize) :
            #print(f"Array[{i}][{j}]: {Array[i][j]}")
            f[i][j] = CheckInacc(max(f[i - 1][j], f[i][j - 1]), Array[i][j])
        # print the current row of collected coins
        print(f[i])

    return f[rowsize - 1][colsize - 1]

def main() :
    ## Sample Test Arrays
    c = [
        [0, -9, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, -9],
        [-9, 0, -9, 1, 0, 1],
        [0, 1, 0, 0, -9, 0],
        [1, 0, 0, 0, -9, 0],
    ]
    collected = CoinCollection(c)
    if (collected < 0) :
        result = "End cell block inaccessible"
    else :
        result = str(collected)
    print("\n-9 represents inaccessible cell; -1 represents inaccessible cell with a coin in it.")
    print(f"Total coin collected: {result}.\n")

if __name__ == "__main__":
    main()
