import sys 
from collections import deque 

input = sys.stdin.readline 

N,K = map(int,input().split())

def find(curr):
    visited = [False]*(100001)
    visited[curr] = True
    
    queue = deque()
    queue.append((curr,0))
    
    while(queue):
        curr,time = queue.popleft() 
        if(curr==K):
            return time
        nexts = [curr*2,curr-1,curr+1]
        diff = [0,1,1]
        for i in range(len(nexts)):
            if(0<=nexts[i]<=100000 and not visited[nexts[i]]):
                visited[nexts[i]] = True 
                if(diff[i]==0):
                    queue.appendleft((nexts[i],time+diff[i]))
                else:
                    queue.append((nexts[i],time+diff[i]))

print(find(N))