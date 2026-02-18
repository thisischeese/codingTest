import sys 
from collections import deque 

input = sys.stdin.readline 

def ts():
    queue = deque() 
    
    for node in range(1,N+1):
        if(indegree[node]==0):
            queue.append(node)
            
    while(queue):
        curr = queue.pop()
        print(curr,end=' ')
        for next in adj[curr]:
            indegree[next] -= 1 
            if(indegree[next]==0):
                queue.append(next)
        
    


N,M = map(int,input().split())
adj = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    indegree[b] += 1 
    adj[a].append(b)

ts() 
'''
위상정렬 
indegree의 개념을 아는가? 
'''