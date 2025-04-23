import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0],dp[1][0] = sticker[0][0], sticker[1][0]
    if n!=1:
        dp[0][1],dp[1][1] = sticker[0][1]+sticker[1][0], sticker[1][1]+sticker[0][0]
        for c in range(2,n):
            dp[0][c] = max(dp[1][c-1],dp[1][c-2])+sticker[0][c]
            dp[1][c] = max(dp[0][c-1],dp[0][c-2])+sticker[1][c]
    
    print(max(dp[0][-1],dp[1][-1]))