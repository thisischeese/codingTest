import sys 

input = sys.stdin.readline 

N = int(input())
nset = set(map(int,input().split()))

M = int(input())
marr = list(map(int,input().split()))
for m in marr: 
    if(m in nset): 
        print(1)
    else: 
        print(0)