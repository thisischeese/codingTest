import sys 

input = sys.stdin.readline 

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1, N+1): 
    weight, value = items[i-1]
    for w in range(K+1):
        if w < weight:
            dp[w][i] = dp[w][i-1] 
        else:
            dp[w][i] = max(dp[w][i-1], dp[w - weight][i-1] + value)

print(dp[K][N])
