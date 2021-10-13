# Project 2 Hybrid Sorting Methods
# This program is an implementation of insertion sort
# 
# Author: Xiang Shan Tan

def InsertionSort(Array) :
    # loop through entire array. idx is the index position and value is the value of Array[i]
    # keep a copy of the value of Array[i] for swaping later
    for i, val in enumerate(Array) :
        # duplicate a copy of the current index
        idx = i
        # while loop to find the left most index postion which has the value greater than the stored value "val"
        while i > 0 and Array[i - 1] > val :
            Array[i] = Array[i - 1]
            i = i - 1
        # assign the value to the index position, which was the last value that was greater than the stored value "val"
        Array[i] = val
    return Array

def main() :
    d = [2, 9, 49, 53, 84, 3, 7, 41, 50, 83, 1, 10, 31, 51, 66, 85]
    Array = InsertionSort(d)
    #print(Array)

if __name__ == "__main__":
    main()
