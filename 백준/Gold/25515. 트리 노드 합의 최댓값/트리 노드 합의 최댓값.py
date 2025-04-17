import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]
num = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n)]
for p, c in tree:
    graph[p].append(c)
    graph[c].append(p)

visited = [False] * n
dp = [0] * n  # dp[i]: 

def dfs(node):
    visited[node] = True
    dp[node] = num[node] 
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            dp[node] += max(0, dp[neighbor]) 
    return dp[node]

dfs(0)
print(dp[0])
