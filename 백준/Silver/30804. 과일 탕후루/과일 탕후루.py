import sys 
from collections import defaultdict 

input = sys.stdin.readline 

N = int(input())
fruits = list(map(int,input().split()))
mydict = defaultdict(int)

answer = 0 
left = 0
for right in range(N):
    mydict[fruits[right]] += 1 
    while(len(mydict)>2):
        mydict[fruits[left]]-=1 
        if(mydict[fruits[left]]==0): del mydict[fruits[left]]
        left += 1 
    answer = max(answer,right-left+1)
print(answer)