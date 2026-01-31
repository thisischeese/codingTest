import sys 

N = int(input())
arr = list(map(int,input().split()))

dp_asc = [1]*N
dp_desc = [1]*N

for i in range(N):
    for j in range(i+1,N):
        if(arr[i]<arr[j]):
            dp_asc[j] = max(dp_asc[i]+1,dp_asc[j])

for i in range(N-1,-1,-1):
    for j in range(i-1,-1,-1):
        if(arr[i]<arr[j]):
            dp_desc[j] = max(dp_desc[i]+1,dp_desc[j])

answer = 0
for i in range(N):
    answer = max(dp_asc[i]+dp_desc[i],answer)

print(answer-1)
