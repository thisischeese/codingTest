import sys
sys.setrecursionlimit(10000)

def dfs(board, visited, x, y, M, N):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[y][x] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < M and 0 <= ny < N and visited[ny][nx]==False and board[ny][nx] == 1):
            dfs(board, visited, nx, ny, M, N)


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    board = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1  
    
    answer = 0
    
    for row in range(N):
        for col in range(M):
            if (board[row][col] == 1 and visited[row][col] == False):
                dfs(board, visited, col, row, M, N)
                answer += 1
    
    print(answer)

    