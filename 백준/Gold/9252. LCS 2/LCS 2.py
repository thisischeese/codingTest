import sys 

input = sys.stdin.readline 

mystr1 = input().strip() 
mystr2 = input().strip() 
dp = [['' for _ in range(len(mystr2)+1)] for _ in range(len(mystr1)+1)]

for i in range(len(mystr1)):
    for j in range(len(mystr2)):
        if mystr1[i]==mystr2[j]:
            dp[i+1][j+1] += dp[i][j] + mystr1[i]
        else: 
            dp[i+1][j+1] = dp[i+1][j] if len(dp[i+1][j])>len(dp[i][j+1]) else dp[i][j+1]

print(len(dp[-1][-1]))
if(len(dp[-1][-1])!=0):
    print(dp[-1][-1])
