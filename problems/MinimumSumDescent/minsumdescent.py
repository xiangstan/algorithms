def MinSumDescent(data) :
  dept = len(data)
  memo = [None] * dept
  n = dept - 1

  # string the bottom row
  for i in range(len(data[n])) :
    memo[i] = data[n][i]


  # skipping the bottom row, loop through the rest of triangle
  for i in range(n - 1, -1, -1) :
    for j in range( len(data[i])):
      #print(f"data[i][j]: {data[i][j]}, memo[j]: {memo[j]}, meno[j+1]: {memo[j + 1]}")
      memo[j] = data[i][j] + min(memo[j], memo[j + 1])
      #print(f"min memo[j]: {memo[j]}")
      #print(f"{memo} \n")
  return memo[0]


def main() :
    data = [
      [2],
      [5, 4],
      [4, 1, 7],
      [8, 6, 9, 6]
    ]
    result = MinSumDescent(data)
    print(result)

if __name__ == "__main__":
    main()
