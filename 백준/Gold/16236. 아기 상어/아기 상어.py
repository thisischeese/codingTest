import sys 
from collections import deque 

input = sys.stdin.readline 

def find_next(currr,currc,size):
    dr = [-1,0,0,1]
    dc = [0,-1,1,0]
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[currr][currc] = True 
    
    queue = deque() 
    queue.append((currr,currc,0))

    result = [] 
    
    while(queue):
        currr,currc,dist = queue.popleft()
        for i in range(4): 
            nr = currr + dr[i] 
            nc = currc + dc[i]
            if(0<=nr<N and 0<=nc<N and not visited[nr][nc]):
                if(0<graph[nr][nc]<size):
                    result.append((nr,nc,dist+1)) 
                elif(graph[nr][nc]==size or graph[nr][nc]==0):
                    queue.append((nr,nc,dist+1))
                    visited[nr][nc] = True 
    return result

def solution(sr,sc):
    currr = sr 
    currc = sc 
    
    size = 2
    time = 0
    fcnt = 0
    
    while(True):
        result = find_next(currr,currc,size)
        result = sorted(result,key=lambda x: (x[2],x[0],x[1]))
        if(len(result)==0):
            break
        nextr,nextc,temp = result[0][0],result[0][1], result[0][2]
        graph[nextr][nextc] = 0 
        fcnt += 1
        if(size==fcnt):
            fcnt = 0
            size += 1
        currr = nextr
        currc = nextc
        time += temp 
    return time 

sr=0
sc=0

N = int(input())
graph = []

for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j]==9:
            sr = i
            sc = j
            temp[j] = 0
    graph.append(temp)


print(solution(sr,sc))          


'''
이동할 수 있는 next 위치는 한 개이거나 아예 없거나 둘 중 하나임. 
이동할 수 있는 위치를 반환할 때 BFS를 사용하기 
거리가 같다면 상>좌>우>하
'''