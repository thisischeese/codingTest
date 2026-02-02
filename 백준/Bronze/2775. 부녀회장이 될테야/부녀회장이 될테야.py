import sys 

input = sys.stdin.readline 

T = int(input())

arr = [(int(input()),int(input())) for _ in range(T)]
max_k = max(arr,key=lambda x : x[0])[0]
max_n = max(arr,key=lambda x : x[1])[1]

dp= [[0]*(max_n+1) for _ in range(max_k+1)]
dp[0] = [i for i in range(max_n+1)]

for i in range(1,max_n+1):
    for j in range(1,max_k+1):
        dp[j][i] += dp[j-1][i]+dp[j][i-1]
for r,c in arr:
    print(dp[r][c])

'''
(a,b) = (a-1,1) + (a-1,2) + (a-1,3) + (a-1,4) + ... + (a-1,b)
(a,2) = (a-1,1) + (a-1,2)
(1,b) = (0,1) + (0,2) + ... (0,b)
'''