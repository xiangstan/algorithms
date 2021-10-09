# Project 2 Hybrid Sorting Methods
# This program is an implementation of 2 array sorting algorithm
# 
# Author: Xiang Shan Tan
#
# This implementation uses the idea in homework 5.

# append all element of selected array "rest" and appened to Array[]
def appendRest(rest, Array) :
    while rest :
        Array.append(rest.pop(0))

def Merge2(a: list, b: list) :
    Array = []
    while a and b :
        Array.append((a if a[0] <= b[0] else b).pop(0))
    
    if a :
        appendRest(a, Array)
    elif b :
        appendRest(b, Array)

    return Array

def MergeSort2(array) :
    length = len(array)
    #print("Array size:", length)
    if length > 1 :
        size = length // 2
        return Merge2(MergeSort2(array[0 : size]), MergeSort2(array[size : length]))
    else :
        return array

def main() :
    ## Test Arrays
    d = [2, 9, 49, 53, 84, 3, 7, 41, 50, 83, 1, 10, 31, 51, 66, 85]
    # call Merge2 function
    Array = MergeSort2(d)
    print(Array)

if __name__ == "__main__":
    main()

