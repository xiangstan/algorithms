"""
Write a divide-and-conquer algorithm for finding both the largest and the smallest elements in an array
break the array into 2 subarrays
"""

def MinMax (Array) :
    # declare 2 empty arrays
    left = right = []
    minmax = [0, 0]

    length = len(Array)

    if length < 2 :
        minmax[0] = Array[0]
        minmax[1] = Array[0]
        #print("Only 1 element: ", minmax)
        return minmax
    else :
        # split array in the middle
        mid = length // 2
        left = MinMax(Array[0 : mid])
        right = MinMax(Array[mid : length])
        #print("Left:", left)
        #print("Right:", right)
    
        # compare the minimum value
        if left[0] <= right[0] :
            minmax[0] = left[0]
        else :
            minmax[0] = right[0]

        # compare the maximum value
        if left[1] >= right[1] :
            minmax[1] = left[1]
        else :
            minmax[1] = right[1]

        return minmax


def main() :
    d = [2, 7, 5, 34, 84, 125, 19, 27, 6, 42]
    minmax = MinMax(d)
    print("Maximum Value:", minmax[0], " Minimum Value: ", minmax[1])

if __name__ == "__main__":
    main()
