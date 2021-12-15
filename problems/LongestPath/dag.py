# Python3 program to find the
# longest path in the DAG
   
# function to add an edge
def addEdge(adj, u, v):
  adj[u].append(v)
   
# function to traverse the DAG and apply dynamic programming to find the longest path
def dfs(node, adj, dp, vis):
  # Mark as visited
  vis[node] = True
  # Traverse for all its children
  for i in range(0, len(adj[node])): 
    # if not visited
    if not vis[adj[node][i]]:
      dfs(adj[node][i], adj, dp, vis)

    # Store the max of the paths
    dp[node] = max(dp[node], 1 + dp[adj[node][i]])
    print(f"dp[node]: {node} -> {dp[node]}")
   
# function that returns the longest path
def findLongestPath(adj, n):
  # dp array
  dp = [0] * (n + 1)
  # visited array to know if the node has been visited previously or not
  vis = [False] * (n + 1)
  # call DFS for every unvisited vertex
  for i in range(1, n + 1): 
    if not vis[i]:
      dfs(i, adj, dp, vis)

  ans = 0
  
  print(f"DP: {dp}")
  # traverse and find the maximum of all dp[i]
  for i in range(1, n + 1): 
    ans = max(ans, dp[i])
  
  #print(f"Visited nodes: {vis}")
  return ans
  
if __name__ == "__main__":
  n = 5
  adj = [[] for i in range(n + 1)]
  
  # Example-1
  addEdge(adj, 1, 2)
  addEdge(adj, 1, 3)
  addEdge(adj, 3, 2)
  addEdge(adj, 2, 4)
  addEdge(adj, 3, 4)
  print(f"ADJ: {adj}")
  
  print(findLongestPath(adj, n))