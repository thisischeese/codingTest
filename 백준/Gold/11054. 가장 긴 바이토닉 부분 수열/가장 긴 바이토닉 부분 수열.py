import sys 
import bisect 

input = sys.stdin.readline 

N = int(input())
arr = list(map(int, input().split()))

def get_lis(seq):
    
    tails = []
    dp = []

    for s in seq:
        if not tails or tails[-1]<s:
            tails.append(s)
            dp.append(len(tails))
        else: 
            idx = bisect.bisect_left(tails,s)
            tails[idx] = s 
            dp.append(idx+1)
    return dp
            
dp_asc = get_lis(arr)
dp_desc = get_lis(arr[::-1])[::-1]

answer = 0
for i in range(N):
    answer = max(answer, dp_asc[i] + dp_desc[i] - 1)

print(answer)
