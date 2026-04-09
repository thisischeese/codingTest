import sys 
from itertools import permutations 

input = sys.stdin.readline 

N,M = map(int,input().split())
arr = sorted(map(int,input().split()))

for comb in sorted(set(permutations(arr,M))):
    print(*comb)
