import sys 
from collections import deque 

INF = 1e8
input = sys.stdin.readline 

def bfs(start):
    distance = [-1]*(V+1)
    queue = deque([start])
    distance[start]=0

    max_idx = start 
    max_dist = 0
    
    while(queue):
        curr = queue.pop() 
        for next,cost in adj[curr]:
            if(distance[next]==-1):
                distance[next] = distance[curr]+cost 
                queue.append(next)

                if(distance[next]>max_dist):
                    max_dist = distance[next]
                    max_idx = next 
    return max_dist, max_idx
                    
    

V = int(input())
adj = [[] for _ in range(V+1)]
leaves = [False for _ in range(V+1)]

for i in range(1,V+1):
    temp = list(map(int,input().split()))
    idx = temp[0]
    for i in range(1,len(temp)-1,2):
        adj[idx].append((temp[i],temp[i+1])) # 연결된 idx, 가중치 

max_dist,max_idx = bfs(1)
max_dist,max_idx = bfs(max_idx)
print(max_dist)