import sys 
from collections import deque 

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    def bfs():
        dr = [1,-1,0,0]
        dc = [0,0,1,-1]
        
        queue = deque()
        queue.append((0,0,1))
    
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[0][0] = True
        
        while(queue):
            cr,cc,dist = queue.popleft() 
            if(cr==n-1 and cc==m-1):
                return dist
            
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                
                if(0<=nr<n and 0<=nc<m and visited[nr][nc]==False and maps[nr][nc]==1):
                    visited[nr][nc]=True 
                    queue.append((nr,nc,dist+1))
        return -1 
                
    return bfs()

