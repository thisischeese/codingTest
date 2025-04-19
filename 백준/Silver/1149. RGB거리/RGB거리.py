import sys 
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
colors = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
# 말단 노드 값 == 말단 노드의 최소합  
dp[0][0], dp[0][1], dp[0][2] = colors[0][0],colors[0][1],colors[0][2]

for i in range(1,N):
    dp[i][0] = colors[i][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = colors[i][1] + min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = colors[i][2] + min(dp[i-1][0],dp[i-1][1])
    

print(min(dp[N-1]))
    
