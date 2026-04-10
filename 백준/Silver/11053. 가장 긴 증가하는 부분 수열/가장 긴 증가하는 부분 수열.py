import sys 
from bisect import bisect_left 

input = sys.stdin.readline 

N = int(input())
arr = list(map(int,input().split()))
seq = [] 

for i in range(N):
    if(len(seq)==0 or seq[-1]<arr[i]):
        seq.append(arr[i])
        continue 
    # lower bound 찾기 
    last_idx = bisect_left(seq,arr[i])
    seq[last_idx] = arr[i]

    

print(len(seq))
'''

3
3 2 3

3
2
2 3 

'''