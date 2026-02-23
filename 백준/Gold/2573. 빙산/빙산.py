import sys 
from collections import deque 

input = sys.stdin.readline 

def simulation(graph):

    dup = [[graph[r][c] for c in range(M)] for r in range(N)]


    sr = 0
    sc = 0
    cnt = 0 
    
    for r in range(N):
        for c in range(M):
            if(graph[r][c]!=0): 
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if(0<=nr<N and 0<=nc<M and graph[nr][nc]==0):
                        if(dup[r][c]>0):
                            dup[r][c] -= 1
    for r in range(N):
        for c in range(M):
            if(dup[r][c]!=0):
                cnt += 1
                sr = r
                sc = c
                
          
    return dup,cnt,sr,sc

def solution(graph):
    time = 0 
     
    while(True):
        graph,cnt,sr,sc = simulation(graph)
        # print(f"time:{time}, cnt : {cnt}")
        # for g in graph:
        #     print(*g)
        
        time += 1 
        if(cnt==0):
            return 0  
        
        queue = deque() 
        queue.append((sr,sc))

        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[sr][sc] = True
        
        total = 0 
        
        while(queue):
            cr,cc = queue.popleft() 
            total += 1
            # print(f"total, ({cr},{cc})")
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]       
                if(0<=nr<N and 0<=nc<M and not visited[nr][nc] and graph[nr][nc]!=0):
                    queue.append((nr,nc))
                    visited[nr][nc] = True 
                    
        if(cnt!=total):
            # print(cnt,total)
            return time



N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

print(solution(graph))

'''
1. 1초마다 시뮬레이션 돌리기 
2. 빙하 덩어리 개수 구하기 
    -> 모두 0이면 0 출력 후 종료 
    -> 덩어리 2개 이상면 소요 시간 출력 후 종료 

'''