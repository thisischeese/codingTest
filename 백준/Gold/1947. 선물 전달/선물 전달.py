import sys 

N = int(sys.stdin.readline())

if N <= 2:
    print(N-1)
    sys.exit()

dp = [0,1]

for i in range(3,N+1):
    prev0,prev1 = dp[0],dp[1]
    dp[0] = prev1 
    dp[1] = (i-1)*(prev0+prev1)%1000000000

print(dp[1])    