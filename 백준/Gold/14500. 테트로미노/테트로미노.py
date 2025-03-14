import sys

answer = 0 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 차례로 ㅗ,ㅜ,ㅏ,ㅓ
exceptions = [
    [(0, -1), (0, 1), (1, 0)], 
    [(0, -1), (0, 1), (-1, 0)],
    [(-1, 0), (1, 0), (0, 1)],
    [(-1, 0), (1, 0), (0, -1)]
]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(x, y, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False  

def check_exception(x, y):
    global answer
    for shape in exceptions:
        total = board[x][y]
        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                total += board[nx][ny]
            else:
                break
        else:
            answer = max(answer, total)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])  
        visited[i][j] = False
        check_exception(i, j) 

print(answer)
