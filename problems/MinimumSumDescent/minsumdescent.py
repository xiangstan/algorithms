def MinSumDescent(data) :
  memo = []
  n = len(data) - 1

  # string the bottom row
  for i in range(len(data[n])) :
    memo.append(data[n][i])
  
  # memo = [8, 6, 9, 6]


  # skipping the bottom row, loop through the rest of triangle
  for i in range(n - 1, -1, -1) :
    #print(f"Iteration: {i}")
    for j in range( len(data[i])):
      #print(f"data[i][j]: {data[i][j]}, memo[j]: {memo[j]}, meno[j+1]: {memo[j + 1]}")
      # find the minimum value between the current position and the one to the right, 
      # then add the minimum value with the value directly above.
      # update the j position of memo array.
      memo[j] = data[i][j] + min(memo[j], memo[j + 1])
      #print(f"min memo[j]: {memo[j]}")
    #print(f"{memo} \n")
  return memo[0]


def main() :
    data = [
      [2],
      [5, 4],
      [1, 4, 7],
      [8, 6, 9, 6]
    ]
    result = MinSumDescent(data)
    print(result)

if __name__ == "__main__":
    main()
