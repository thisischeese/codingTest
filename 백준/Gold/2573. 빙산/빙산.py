import sys 
from collections import deque 

input = sys.stdin.readline 
  

def solution():
    N,M = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    icebergs = []
    for i in range(N):
        for j in range(M):
            if(graph[i][j]>0):
                icebergs.append((i,j))
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    time = 0 
     
    while(icebergs):

        
        queue = deque() 
        queue.append((icebergs[0][0],icebergs[0][1]))

        visited[icebergs[0][0]][icebergs[0][1]] = time 
        
        total = 0 
        
        while(queue):
            cr,cc = queue.popleft() 
            total += 1
            # print(f"total, ({cr},{cc})")
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]       
                if(0<=nr<N and 0<=nc<M and visited[nr][nc]!=time and graph[nr][nc]>0):
                    queue.append((nr,nc))
                    visited[nr][nc] = time 
                    
        if(len(icebergs)!=total):
            return time
        # 시뮬레이션 
        melt_list = []
        new_icebergs = [] 
    
        for r,c in icebergs:
            sea_cnt = 0 
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if(0<=nr<N and 0<=nc<M and graph[nr][nc]==0):
                    sea_cnt += 1
            melt_list.append(sea_cnt)
    
        for i in range(len(icebergs)):
            r,c = icebergs[i][0], icebergs[i][1]
            graph[r][c] = max(graph[r][c]-melt_list[i],0)
            if(graph[r][c]>0):
                new_icebergs.append((r,c))
        icebergs = new_icebergs 
        
        time += 1
    return 0






print(solution())

'''
1. 1초마다 시뮬레이션 돌리기 
2. 빙하 덩어리 개수 구하기 
    -> 모두 0이면 0 출력 후 종료 
    -> 덩어리 2개 이상면 소요 시간 출력 후 종료 

'''