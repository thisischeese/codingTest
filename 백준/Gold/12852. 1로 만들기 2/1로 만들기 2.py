import sys 

input = sys.stdin.readline 

N = int(input())
dp = [0]*(N+1)
path = [0]*(N+1)

for i in range(2,N+1):
    dp[i] = dp[i-1]+1 
    path[i] = i-1

    if(i%2==0 and dp[i]>dp[i//2]+1):
        dp[i]=min(dp[i],dp[i//2]+1)
        path[i] = i//2
    if(i%3==0 and dp[i]>dp[i//3]+1):
        dp[i] = min(dp[i],dp[i//3]+1)
        path[i] = i//3 
        
print(dp[N])
curr = N 
while(True):
    print(curr,end=' ')
    if(curr==1):
        break 
    curr = path[curr]