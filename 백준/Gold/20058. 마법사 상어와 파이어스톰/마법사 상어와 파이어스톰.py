import sys 
from collections import deque 

input = sys.stdin.readline

def move(length):
    queue = deque() 
    if(length!=1):
        for r in range(0,2**N,length):
            for c in range(0,2**N,length):
                for nr in range(r,r+length):
                    for nc in range(c,c+length):
                        queue.append((graph[nr][nc]))
                # c는 뒤에서부터
                # r은 작은것부터 큰 것으로
                for nc in range(c+length-1,c-1,-1):
                    for nr in range(r,r+length):
                        graph[nr][nc] = queue.popleft() 
    for i in range(2**N):
        for j in range(2**N):
            temp[i][j] = graph[i][j]
    for r in range(0,2**N):
        for c in range(0,2**N):
            cnt = 0 
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if(0<=nr<2**N and 0<=nc<2**N and graph[nr][nc]!=0):
                    cnt +=1 
            if(cnt<3 and graph[r][c]!=0):
                    temp[r][c] -=1
    for i in range(2**N):
        for j in range(2**N):
            graph[i][j] = temp[i][j]
            
def bfs(r,c):
    cnt = 0
    queue = deque() 
    queue.append((r,c))
    visited[r][c] = True 
    
    while(queue):
        cr, cc = queue.popleft() 
        cnt += 1
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if(0<=nr<2**N and 0<=nc<2**N and not visited[nr][nc]):
                visited[nr][nc] = True 
                queue.append((nr,nc))

    return cnt if cnt!=0 else 0 
        
N, Q = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(2**N)]
temp = [[0 for _ in range(2**N)] for _ in range(2**N)]
visited = [[False for _ in range(2**N)] for _ in range(2**N)]
magic_seq = list(map(int,input().split()))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

for L in magic_seq:
    move(2**L)

print(sum(map(sum,graph)))

for i in range(2**N):
    for j in range(2**N):
        if(graph[i][j]==0):
            visited[i][j]=True 

answer = 0
for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and graph[i][j]!=0:
            answer = max(answer,bfs(i,j))
print(answer)