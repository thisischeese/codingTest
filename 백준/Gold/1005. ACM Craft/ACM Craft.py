import sys 
from collections import deque 

input = sys.stdin.readline 

def ts():
    queue = deque() 
    # indegree==0인 것을 queue에 삽입 
    
    for i in range(1,N+1):
        if indegree[i]==0:
            queue.append(i)  
            time[i] = dtime[i]

    # 인접 노드 방문하며 indegree 업데이트
    while(queue):
        curr = queue.pop()
        for next in adj[curr]:
            indegree[next] -= 1
            time[next] = max(time[curr]+dtime[next],time[next])
            if(indegree[next]==0):
                queue.append(next)
        
    


T = int(input())

for t in range(T):
    N,K = map(int,input().split())
    adj = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    
    dtime = [0]+list(map(int,input().split()))
    time = [0]*(N+1)

    for _ in range(K):
        x,y = map(int,input().split())
        adj[x].append(y)
        indegree[y] += 1
        
    W = int(input())
    ts()
    print(time[W])