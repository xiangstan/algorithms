# Homework 6 Edit Distance Problem
# 
# Author: Xiang Shan Tan
#
# This implementation is specifically for the edit distance problem (question 2) of homework 6.
# Find nimimum steps to nutate one word to another.
# The program shall be able to change aletter,
# insert a letter, or
# delete a letter

import sys
import time

if len(sys.argv) < 3 :
    print("\nUsage: python editdistance.py [starting word] [ending word]\n")
    sys.exit()

input = sys.argv

start = input[1]
end = input[2]

def EditDistance(a, b) :
    # if string a and string b is exact the same
    if a == b :
        return 0
    #print(a, b)
    # if one string is empty, the distance is inserting whatever left of the other string
    if a == "" :
        return len(b)
    if b == "" :
        return len(a)
    # initialize the cost counter
    cost = 0
    # if the last character of two strings are different, insert/delete/swap need to be performed
    # insertion cost: 1
    # deletion cost: 1
    # swaping cost: 1
    # this logic will not work if the cost of swaping is not 1
    if a[-1] != b[-1] :
        cost = 1
    #print(a[:-1])
    # take whatever the shorted distance plus the cost of current step
    distance = min([EditDistance(a[:-1], b),
               EditDistance(a, b[:-1]), 
               EditDistance(a[:-1], b[:-1])]) + cost

    return distance

def main() :
    timerstart = time.perf_counter()
    print("\nThe minimum mutation count is: ", EditDistance(start, end))
    timerend = time.perf_counter()
    print(f"Program execution time: {timerend - timerstart} second(s).\n")

if __name__ == "__main__":
    main()
