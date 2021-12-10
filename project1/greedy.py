import numpy as np

limit = 10000   # Weight limit: W

class BestSet :
    def __init__(self):
        self.value = 0
        self.weight = 0
        self.combo = ""

def Greedy(n, values, weights) :
    best = BestSet()
    sort = np.argsort(values)[::-1] # get the index by sorting values from highest to lowest

    curvalue = 0
    curweight = 0
    dataset = []
    valueset = []
    weightset = []
    #print("Sorted dataset: ", sort)
    for i in (sort):
        valueset.append(values[i])
        weightset.append(weights[i])

        temp = curweight + weights[i]
        if temp < limit :
            curvalue += values[i]
            curweight += weights[i]
            dataset.append(i)
    #print("Sorted Values: ", valueset)
    #print("Sorted Weight: ", weightset)
    #print(dataset)
    #print(curvalue)
    #print(curweight)
    best.combo = dataset
    best.value = curvalue
    best.weight = curweight
    return best
