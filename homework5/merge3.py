# append all element of selected array "rest" and appened to Array[]
def appendRest(rest, Array) :
    while rest :
        Array.append(rest.pop(0))

# compare two arrays and sorts all possible elements to array Array[]
# a and b are both arrays
# loop through both arrays until one array is empty
# find the smaller value between both arrays at their current index, pop the value
def merge2(a, b, Array) :
    while a and b :
        Array.append((a if a[0] <= b[0] else b).pop(0))

# parsing three arrays: a, b, and c
def merge3(a, b, c) :
    Array = []
    #print("Merge 3: ", a, b, c)

    while a and b and c :
        smallest = min(a[0], b[0], c[0])
        Array.append(smallest)
        if smallest == a[0] :
            a.pop(0)
        elif smallest == b[0] :
            b.pop(0)
        elif smallest == c[0] :
            c.pop(0)
    
    while a and b :
        merge2(a, b, Array)

    while b and c :
        merge2(b, c, Array)

    while a and c :
        merge2(a, c, Array)

    if a :
        appendRest(a, Array)

    elif b :
        appendRest(b, Array)

    else :
        appendRest(c, Array)
    
    return Array

def main() :
    a = [2, 9, 49, 53, 84]
    b = [3, 7, 41, 50, 83]
    c = [1, 10, 31, 51, 66, 85]
    #d = [2, 9, 49, 53, 84, 3, 7, 41, 50, 83, 1, 10, 31, 51, 66, 85]
    #test = mergesort(d)
    print("Only Merge3:", merge3(a, b, c))
    #print("MergeSort:  ", test)

if __name__ == "__main__":
    main()
