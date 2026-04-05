import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
visited = [False]*N

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(curr,depth):
    if depth==4:
        print(1)
        sys.exit() 
    for next in graph[curr]:
        if not visited[next]:
            visited[next] = True 
            dfs(next,depth+1)
            visited[next] = False 
for i in range(N):
    visited[i] = True 
    dfs(i,0)
    visited[i] = False 
    
print(0)

'''
그냥 DFS로 5개 노드가 일렬로 연결되었는지 탐색
-> 간선의 개수는 4!!
'''