import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 

N = int(input())
adj = [[] for _ in range(N+1)]
parents = [i for i in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    adj[e].append(s)
    adj[s].append(e) 
visited = [True]*2+[False]*(N-1) 

def dfs(curr):
    if len(adj[curr])==0:
        return 
    
    for next in adj[curr]:
        if not visited[next]:
            parents[next] = curr 
            visited[next] = True 
            dfs(next)
dfs(1)
print(*parents[2:],sep='\n')
    
