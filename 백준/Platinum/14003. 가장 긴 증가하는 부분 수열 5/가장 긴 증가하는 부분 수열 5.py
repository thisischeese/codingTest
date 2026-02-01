import sys 
import bisect

input = sys.stdin.readline 

N = int(input())
arr = list(map(int,input().split()))

dp = [0]*N
tails = []
result = []

if N==0:
    print(1)
    print(arr[0])
    sys.exit()

for i in range(N):
    if not tails or tails[-1][1]<arr[i]:
        tails.append((i,arr[i]))
        dp[i] = len(tails)
    else:
        idx = bisect.bisect_left(tails,arr[i],key=lambda x : x[1])
        tails[idx]=(i,arr[i])
        dp[i] = idx+1

max_len = len(tails)
print(max_len)

curr_len = max_len
for i in range(N-1,-1,-1):
    if(curr_len==dp[i]):
        result.append(arr[i])
        curr_len-=1
    if curr_len ==0:
        break 
        
        
print(*result[::-1])
        

        

'''
N<=1e6
|a_i|<=1e9

이분탐색 or 세그먼트 트리로 시간 복잡도 줄여야 함 
이분탐색 -> tails 배열 만들기 
tails 배열은 수열 가능성 있는 tail 값만 저장함 
실제로 수열 구할 때는 역추적해서 구해야 함 

'''