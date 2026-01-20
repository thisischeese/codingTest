import sys 
import math
from collections import Counter 

input = sys.stdin.readline 

N = int(input())
arr = []
cnt = 0 

for _ in range(N):
    arr.append(int(input()))
arr.sort()
count = Counter(arr).most_common()

print(round(sum(arr)/N))
print(arr[N//2])
if(len(count)>1):
    if(count[0][1]==count[1][1]):
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(arr[-1]-arr[0])