import sys

input = sys.stdin.readline

N = int(input())
dims = []

for _ in range(N):
    r, c = map(int, input().split())
    dims.append((r, c))

p = [dims[0][0]]
for i in range(N):
    p.append(dims[i][1])

dp = [[0] * N for _ in range(N)]

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][N - 1])
