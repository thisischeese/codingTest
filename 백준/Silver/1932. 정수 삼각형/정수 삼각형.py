import sys 

input = sys.stdin.readline

answer = 0 

n = int(input())
tri = [list(map(int,input().split())) for _ in range(n)]
dp = [[tri[i][j] for j in range(i+1)] for i in range(n)]


for i in range(n-1):
    for j in range(i+1):
        dp[i+1][j] = max(dp[i][j]+tri[i+1][j],dp[i+1][j])
        dp[i+1][j+1] = max(dp[i][j]+tri[i+1][j+1],dp[i+1][j+1])


print(max(dp[-1]))