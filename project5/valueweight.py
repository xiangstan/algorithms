"""
Project 5: Knapsack Approximation Algorithm
This program is the implemetation of Knapsack Approximation Algorithm (ordered items by value/weight). 

Author: Xiang Shan Tan

run:
python ./valueweight.py
"""

import numpy as np


# greedy algorithm
# pick the largest value per weight
def ValueWeight(n, values, weights, capacity) :
  # initialize a weight counter
  # this is be used against capacity
  curweight = 0
  curvalue = 0
  # initialize an array to store values of values/weights 
  ratios = []
  # initialize empty arrays to store picked values and weights
  valueset = []
  weightset = []

  for i in range(n) :
    if values[i] > 0 :
      ratios.append(values[i] / weights[i])
  #print(ratios)
  # get the index by sorting values from highest to lowest
  sorted = np.array(np.argsort(ratios))[::-1]
  print(f"Sorted Array: {sorted}")

  for i in (sorted):
      temp = curweight + weights[i]
      if temp <= capacity :
          valueset.append(values[i])
          weightset.append(weights[i])
          curvalue += values[i]
          curweight = temp
  
  return curvalue, curweight, sorted

def main() :
    # total capacity
    capacity = 10
    # highest value
    val = 10
    # total items
    items = 5

    count = 1
    for i in range(count) :
        weights = np.random.randint(1, capacity + 1, size = items)
        values = np.random.randint(1, val + 1, size = items)
        print(f"Weights: {weights}")
        print(f"Values: {values}")

        value, weight, itemset = ValueWeight(items, values, weights, capacity)
        print(value, weight)


if __name__ == "__main__":
    main()



