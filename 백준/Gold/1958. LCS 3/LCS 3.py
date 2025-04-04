import sys

strs = [sys.stdin.readline().strip() for _ in range(3)]

dp = [[[0] * (len(strs[2]) + 1) for _ in range(len(strs[1]) + 1)] for _ in range(len(strs[0]) + 1)]


for i in range(1, len(strs[0]) + 1):
    for j in range(1, len(strs[1]) + 1):
        for k in range(1, len(strs[2]) + 1):
            if strs[0][i - 1] == strs[1][j - 1] == strs[2][k - 1]: 
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])


print(dp[len(strs[0])][len(strs[1])][len(strs[2])])
