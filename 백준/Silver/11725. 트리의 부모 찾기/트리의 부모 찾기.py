import sys 
from collections import deque 

input = sys.stdin.readline 

N = int(input())
adj = [[] for _ in range(N+1)]
parents = [i for i in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    adj[e].append(s)
    adj[s].append(e) 

def bfs(start):
    visited = [False]*(N+1)
    visited[start] = True 
    queue = deque([start])
    
    while(queue):
        curr = queue.popleft() 
        for next in adj[curr]:
            if not visited[next]:
                visited[next] = True 
                queue.append(next)
                parents[next] = curr 
bfs(1) 
print(*parents[2:],sep='\n')
    
