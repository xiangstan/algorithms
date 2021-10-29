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
# return -1 if it is
# otherwise return the cell value + the add value
def CheckInacc(check, add) :
    if check == -1 :
        return -1
    else :
        return check + add

def CoinCollection(Array) :
    # measure/store size of rows and columns
    rowsize = len(f)
    colsize = len(f[0])

    #print(Array[rowsize - 2][colsize - 1], Array[rowsize - 1][colsize - 2])
    # check if the last cell is block by both upper and left inaccessible cells.
    if Array[rowsize - 2][colsize - 1] == -1 and Array[rowsize - 1][colsize - 2] == -1 :
        return 0 if Array[rowsize - 1][colsize - 1] <= 0 else Array[rowsize - 1][colsize - 1]

    else :
        # initialize the value of [0, 0] point.
        f[0][0] = Array[0][0]

        # fill first row
        for i in range(colsize) :
            f[0][i] = CheckInacc(f[0][i - 1], Array[0][i])
        # print the first row of collected coins
        print(f[0])
        
        for i in range(1, rowsize) :
            #print(Array[i][0])
            if Array[i][0] != -1 :
                f[i][0] = CheckInacc(f[i - 1][0], Array[i][0])
            else :
                f[i][0] = -1
            #print(f[i])
            for j in range(1, colsize) :
                #print(f"Array[{i}][{j}]: {Array[i][j]}")
                # check if Array[i][j] is inaccessible
                if Array[i][j] == -1 :
                    f[i][j] = -1
                else :
                    #print(max(f[i - 1][j], f[i][j - 1]))
                    f[i][j] = max(f[i - 1][j], f[i][j - 1]) + Array[i][j]
            # print the current row of collected coins
            print(f[i])

        return f[rowsize - 1][colsize - 1]

def main() :
    ## Sample Test Arrays
    c = [
        [0, -1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, -1],
        [-1, 0, -1, 1, 0, 1],
        [0, 1, 0, 0, -1, 0],
        [1, 0, 0, 0, -1, 0],
    ]
    collected = CoinCollection(c)
    print("Total coin collected: ", collected)

if __name__ == "__main__":
    main()

