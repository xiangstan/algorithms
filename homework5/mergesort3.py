from merge3 import merge3 

loopcount = 0

def mergesort(array) :
    global loopcount
    #print("Loop Count: ", loopcount, "Array: ", array)
    loopcount += 1
    length = len(array)
    #print("Array size:", length)
    if length > 2 :
        size = length // 3
        return merge3(mergesort(array[0 : size]), mergesort(array[size : size*2]), mergesort(array[size*2 : length]))
    else :
        return array


def main() :
    #a = [2, 9, 49, 53, 84]
    #b = [3, 7, 41, 50, 83]
    #c = [1, 10, 31, 51, 66, 85]
    d = [2, 9, 49, 53, 84, 3, 7, 41, 50, 83, 1, 10, 31, 51, 66, 85]
    test = mergesort(d)
    #print("Only Merge3:", merge3(a, b, c))
    print("MergeSort:  ", test)

if __name__ == "__main__":
    main()
