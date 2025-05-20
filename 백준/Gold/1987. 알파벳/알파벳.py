import sys
sys.setrecursionlimit(10000) 

answer = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

def DFS(r, c, bitmask, cnt):
    global answer
    
    answer = max(answer, cnt)
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            next_char = ord(board[nr][nc]) - ord('A')
            if not (bitmask & (1 << next_char)):
                DFS(nr, nc, bitmask | (1 << next_char), cnt + 1)


start_char = ord(board[0][0]) - ord('A')
DFS(0, 0, 1 << start_char, 1)

print(answer)
