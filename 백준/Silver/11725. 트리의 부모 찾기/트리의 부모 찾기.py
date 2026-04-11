import sys 
from collections import deque 

input = sys.stdin.readline 

N = int(input())
adj = [[] for _ in range(N+1)]
parents = [0 for i in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    adj[e].append(s)
    adj[s].append(e) 

def bfs(start):
    parents[start] = start 
    queue = deque([start])
    
    while(queue):
        curr = queue.popleft() 
        for next in adj[curr]:
            if parents[next]==0:
                parents[next] = curr 
                queue.append(next)
                
bfs(1) 
print(*parents[2:],sep='\n')
    
