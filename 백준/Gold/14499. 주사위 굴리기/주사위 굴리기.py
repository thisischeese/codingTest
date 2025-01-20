import sys 

direction = [[0,1],[0,-1],[-1,0],[1,0]]
dice = [0,0,0,0,0,0]
floor = 5
ceil = 0

n,m,y,x,k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
commands = list(map(int,sys.stdin.readline().split()))

def move(c):
    if c == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif c ==3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif c ==2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif c ==4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
       


for c in commands:
    dx,dy = direction[c-1][0],direction[c-1][1]
    if (0<=y+dx<n and 0<=x+dy<m):
        y+=dx
        x+=dy
        
        move(c)
        
        if board[y][x]==0:
            board[y][x] = dice[floor]
        else:
            dice[floor] = board[y][x]
            board[y][x] = 0 
            
        print(dice[ceil])



