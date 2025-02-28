import sys
input = sys.stdin.readline
 
INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    
    dist = [[ graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


v,e = map(int, input().split())
graph = [[INF for _ in range(v+1)] for _ in range(v+1)]

for i in range(e) :
    a,b,c = map(int, input().split())
    
    graph[a][a] = 0
    graph[b][b] = 0
    graph[a][b] = c

shortest_paths = floyd_warshall(graph)

path = []

for row in shortest_paths[1:]:
    path.append(row[1:])
    
result = INF

for i in range(v) :
    
    if path[i][i] == INF :
        continue
    result = min(result,path[i][i])

if result == INF : 
    print(-1)
else :
    print(result)