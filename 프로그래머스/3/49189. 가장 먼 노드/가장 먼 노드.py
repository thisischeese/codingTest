from collections import deque 

def solution(n, edge):
    INF = 1e9 
    
    dist = [INF for _ in range(n+1)]
    
    adj = [[] for _ in range(n+1)]
    for a,b in edge:
        adj[a].append(b)
        adj[b].append(a)
        
    def bfs(start):
        visited = [False for _ in range(n+1)]
        queue = deque() 
        queue.append((start,0))
        
        while(queue):
            curr_node,curr_total=queue.popleft()
            visited[curr_node] = True 
            
            for next_node in adj[curr_node]:
                if not visited[next_node] and dist[next_node]>dist[curr_node]+1:
                    dist[next_node] = dist[curr_node]+1
                    queue.append((next_node,curr_total+1))
    dist[1]=0
    bfs(1)    
    return len([d for d in dist[1:] if d==max(dist[1:])])