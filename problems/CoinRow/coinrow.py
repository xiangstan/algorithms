"""
Algorithm: Coin Row

Applies bottom up to find the maximum amount of money
that can be picked up from a coin row without picking two adjacent coins
Input: Array C[1..n] of positive integers indicating the coin values
Output: The maximum amount of money that can be picked up
"""

def CoinRow(array) :
    n = len(array)
    coin = [0, array[0]]
    for i in range (2, n + 1) :
        coin.append(max(array[i - 1] + coin[i - 2], coin[i - 1]))
        #print(coin)
    return coin[n]

def main() :
    c = [5, 1, 2, 10, 6, 2]
    result = CoinRow(c)
    print(result)

if __name__ == "__main__":
    main()
