import sys
sys.setrecursionlimit(10000)

def dfs(x, y, color, grid, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited[x][y] = True
    n = len(grid)
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and (grid[nx][ny] == color):
            dfs(nx, ny, color, grid, visited)


N = int(sys.stdin.readline().strip())
painting = [list(sys.stdin.readline().strip()) for _ in range(N)]

visited_rgb = [[False] * N for _ in range(N)]
visited_rb = [[False] * N for _ in range(N)]

# 적록색약 x
cnt_rgb = 0
for i in range(N):
    for j in range(N):
        if not visited_rgb[i][j]:
            dfs(i, j, painting[i][j], painting, visited_rgb)
            cnt_rgb += 1

# 적록색약 o 
cnt_rb = 0
painting_rb = [['R' if c == 'G' else c for c in row] for row in painting]
for i in range(N):
    for j in range(N):
        if not visited_rb[i][j]:
            dfs(i, j, painting_rb[i][j], painting_rb, visited_rb)
            cnt_rb += 1

print(cnt_rgb, cnt_rb)
