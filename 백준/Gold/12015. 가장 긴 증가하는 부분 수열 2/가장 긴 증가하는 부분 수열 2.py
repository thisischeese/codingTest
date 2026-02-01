import sys 
import bisect

input = sys.stdin.readline 

N = int(input())
arr = list(map(int,input().split()))

dp = []
tails = []

for i in range(N):
    if not tails or tails[-1]<arr[i]:
        tails.append(arr[i])
        dp.append(len(tails))
    else:
        idx = bisect.bisect_left(tails,arr[i])
        tails[idx]=arr[i]
        dp.append(idx+1)

print(max(dp))

'''
N<=1e6
a_i<=1e6
'''