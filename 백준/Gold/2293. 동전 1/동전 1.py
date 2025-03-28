import sys 

n,k = map(int,sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(n))
dp = [1]+[0 for _ in range(k)]

for coin in coins:
    for i in range(coin,k+1):
        dp[i] += dp[i-coin]
            
print(dp[-1])