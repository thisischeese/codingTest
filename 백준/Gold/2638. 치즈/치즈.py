import sys
from collections import deque

sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt_cheese():
    visited = [[False] * M for _ in range(N)]
    air = deque()
    air.append((0, 0))
    visited[0][0] = True

    contact = [[0] * M for _ in range(N)]

    while air:
        x, y = air.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    air.append((nx, ny))
                elif arr[nx][ny] == 1:
                    contact[nx][ny] += 1 

    melted = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and contact[i][j] >= 2:
                arr[i][j] = 0  
                melted = True

    return melted

time = 0
while True:
    if not melt_cheese():
        break
    time += 1

print(time)
