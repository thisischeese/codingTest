from collections import deque 

def solution(rectangle, cX, cY, iX, iY):
    answer = 0
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    for i in range(len(rectangle)):
        for j in range(4):
            rectangle[i][j] = rectangle[i][j]*2
    
    board = [[False for _ in range(102)] for _ in range(102)]
    visited = [[False for _ in range(102)] for _ in range(102)]
    
    # 사각형 전체 채우기 
    for lr,lc,rr,rc in rectangle:
        for r in range(lr,rr+1):
            for c in range(lc,rc+1):
                board[r][c]=True
  
    # 사각형 내부 테두리 빼고 비우기 
    for lr,lc,rr,rc in rectangle:
        for r in range(lr+1,rr):
            for c in range(lc+1,rc):
                board[r][c]=False 
    
    def bfs(sr,sc,tr,tc):
        
        queue = deque([(sr,sc,0)]) 
        visited[sr][sc]=True
        
        while(queue):
            cr,cc,dist = queue.popleft() 
            
            if(cr==tr and cc==tc):
                return dist 
            
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if(1<=nr<102 and 1<=nc<102 and board[nr][nc] and not visited[nr][nc]):
                    queue.append((nr,nc,dist+1))
                    visited[nr][nc]=True
                    
        return -1 
    
    return bfs(cX*2, cY*2, iX*2, iY*2)//2

