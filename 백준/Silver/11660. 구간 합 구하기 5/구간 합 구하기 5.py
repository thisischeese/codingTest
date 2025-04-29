import sys 
import copy

N,M = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
target = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
prefix = [[0 for _ in range(N+2)] for _ in range(N+2)]

for i in range(1,N+1):
    for j in range(1,N+1):
        prefix[i][j] = board[i-1][j-1]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==1 and j ==1:
            continue
        elif i==1:
            prefix[i][j] += prefix[i][j-1]
        elif j ==1:
            prefix[i][j] += prefix[i-1][j]
        else:
            prefix[i][j] += prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for x1,y1,x2,y2 in target:
    if x1==x2 and y1==y2:
        print(board[x1-1][y1-1])
    else:
        total = prefix[x2][y2] + prefix[x1-1][y1-1] - prefix[x1-1][y2] - prefix[x2][y1-1]
        print(total)

            

