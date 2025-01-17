import sys 
from collections import deque

d = {1:[(0, 1), (0, -1), (-1, 0)], 
     2:[(1, 0), (-1, 0), (0, 1)],
     3:[(0, -1), (0, 1), (1, 0)], 
     0:[(-1, 0), (1, 0), (0, -1)]}  

N = int(sys.stdin.readline()) 
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(sys.stdin.readline()) 
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1 

L = int(sys.stdin.readline()) 
move = {}
for i in range(L):
    time, direction = sys.stdin.readline().split()
    move[int(time)] = direction
  

def bfs(x, y, dir, now):
    queue = deque()
    snake = deque()
    
    queue.append((x, y))
    snake.append((x, y))

    while queue:
        tmp_x, tmp_y = queue.popleft()
        if now in move.keys():         
            if move[now] == "D":      
                nx = tmp_x + d[dir][0][0]
                ny = tmp_y + d[dir][0][1]
                dir = (dir + 1) % 4
            else:                           
                nx = tmp_x + d[dir][1][0]
                ny = tmp_y + d[dir][1][1]
                dir = (dir + 3) % 4
        else:                               
            nx = tmp_x + d[dir][2][0]
            ny = tmp_y + d[dir][2][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake: 
            return now + 1
        
        queue.append((nx, ny))
        snake.append((nx, ny))
        now += 1
        
        if board[nx][ny] == 1:    
            board[nx][ny] = 0
        
        else:   
            snake.popleft()

    return now + 1

print(bfs(0, 0, 2, 0))
