# Homework 6 Edit Distance Problem
# 
# Author: Xiang Shan Tan
#
# This implementation is specifically for the edit distance problem (question 2) of homework 6.
# Find nimimum steps to nutate one word to another.
# The program shall be able to change aletter,
# insert a letter, or
# delete a letter
#
# This is a for loop implementation of the problem
#

import sys
import time

if len(sys.argv) < 3 :
    print("\nUsage: python editdistance.py [starting word] [ending word]\n")
    sys.exit()

input = sys.argv

start = input[1]
end = input[2]

distance = []

def EditDistance(a, b, m, n) :
    # if string a and string b is exact the same
    if a == b :
        return 0
    #print(a, b)
    # this program restrict the use of empty string
    # otherwise, if one string is empty, the distance is inserting whatever left of the other string
    #if a == "" :
    #    return n
    #if b == "" :
    #    return m
    print(distance[0])

    for i in range (1, m + 1) :
        for j in range(1, n + 1) :
            # when nothing changes
            cost = 0
            # when add/delete/update is required
            if a[i - 1] != b[j - 1] :
                cost = 1
            # find the minimum mutations occurs at the selected cell block
            distance[i][j] = min(distance[i - 1][j] + 1, distance[i][j - 1] + 1, distance[i - 1][j - 1] + cost)
        print(distance[i])

    return distance[m][n]

def main() :
    (m, n) = (len(start), len(end))
    # intialize m*n multidementional array
    for i in range (m + 1) :
        temp = []
        for j in range (n + 1) :
            temp.append(0)
        distance.append(temp)
    # initialize first row and column
    for i in range(1, m + 1) :
        distance[i][0] = i
    for j in range(1, n + 1) :
        distance[0][j] = j
    print("Initial distance: ", distance)

    timerstart = time.perf_counter()
    print("\nThe minimum mutation count is: ", EditDistance(start, end, m, n))
    timerend = time.perf_counter()
    print(f"Program execution time: {timerend - timerstart} second(s).\n")

if __name__ == "__main__":
    main()
