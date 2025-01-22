from collections import deque
from itertools import combinations
import sys 

n,m = map(int,sys.stdin.readline().split())
graph = []
empty = []
vrs = deque()
safe = 0

def bfs(vgraph,vrs):
    copy_vrs = deque(vrs)
    visited = [[False]*m for _ in range(n)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for x,y in copy_vrs:
        visited[x][y] = True

    while copy_vrs:
        x,y = copy_vrs.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == False and vgraph[nx][ny] == 0:
                    vgraph[nx][ny] = 2
                    visited[nx][ny] = True
                    copy_vrs.append((nx,ny))
    return vgraph


for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if arr[j] == 2: 
            vrs.append((i,j))
        if arr[j] == 0:
            empty.append((i,j))

    graph.append(arr)


for a,b,c in combinations(empty, 3):
    vgraph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            vgraph[i][j] = graph[i][j]
    for x,y in [a,b,c]:
        vgraph[x][y] = 1

    vgraph = bfs(vgraph,vrs)
    zero = 0
    for i in vgraph:
        for j in i:
            if j==0:
                zero += 1
    safe = max(safe, zero)
    
print(safe)