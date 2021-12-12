"""
Algorithm: Unbound Knapsack

Unbounded Knapsack: use of 1 or more instances of any resource. A simple 1D array, say dp[W+1] can be used such that dp[i] stores the maximum value which can achieved using all items and i capacity of knapsack.
"""

# n: size of itemset
# values: array of all values
# weights: array of all weights
# capacity: max capacity allowed to carry
def UnboundKnapsack (n, values, weights, capacity) :
  kpset = [0] * (capacity + 1)

  for i in range(capacity + 1) :
    curweight = 0
    for j in range(len(weights) - 1) :
      if weights[j] <= capacity :
        curweight = max(curweight, values[j] + kpset[capacity - weights[j]])
        #print(f"I: {i}, Curweight: {curweight}")
      kpset[i] = curweight
  
  #print(kpset)
  return kpset[capacity]

def main() :
    # total capacity
    capacity = 10
    # value array
    values = [10, 30, 20]
    # weight array
    weights = [5, 10, 15]
    # total items
    n = len(values)

    print(UnboundKnapsack(n, values, weights, capacity))


if __name__ == "__main__":
    main()
