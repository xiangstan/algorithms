"""
Riddle function fetches the smallest number in a given array

python riddle.py
Array:  [11, 4, 3, 4, 5, 3, 2, 3, 54]
Array:  [11, 4, 3, 4, 5, 3, 2, 3]
Array:  [11, 4, 3, 4, 5, 3, 2]
Array:  [11, 4, 3, 4, 5, 3]
Array:  [11, 4, 3, 4, 5]
Array:  [11, 4, 3, 4]
Array:  [11, 4, 3]
Array:  [11, 4]
Array:  [11]
Temp:  11
Temp:  4
Temp:  3
Temp:  3
Temp:  3
Temp:  3
Temp:  2
Temp:  2
2

"""

def Riddle(Array) :
    #print("Array: ", Array)
    length = len(Array)
    if length == 1 :
        return Array[0]
    else :
        temp = Riddle(Array[0 : length - 1])
        #print("Temp: ", temp)
        if temp <= Array[length - 1] :
            return temp
        else :
            return Array[length - 1]

print(Riddle([11,4,3,4,5,3,2,3,54]))