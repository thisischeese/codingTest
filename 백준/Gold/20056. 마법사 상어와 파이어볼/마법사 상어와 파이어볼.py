import sys 
import math 
input = sys.stdin.readline 

def solution():
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]

    def move():
        temp = [[[] for _ in range(N)] for _ in range(N)]
        for r in range(N):
            for c in range(N):
                for m,s,d in graph[r][c]:
                    nr = (r + dr[d]*s)%N
                    nc = (c + dc[d]*s)%N
                    temp[nr][nc].append((m,s,d))
                    
        for r in range(N):
            for c in range(N):
                cnt = 0 
                tm = 0
                ts = 0 
                even_cnt = 0
                odd_cnt = 0 
                if(len(temp[r][c])<2):
                    continue 
                for m,s,d in temp[r][c]:
                    cnt += 1
                    tm += m 
                    ts += s 
                    if d%2==0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                    
                nm = math.floor(tm/5)
                ns = math.floor(ts/cnt)  
                if(nm==0):
                    temp[r][c] = []
                    continue 

                if(even_cnt==cnt or odd_cnt==cnt):
                    td = [0,2,4,6]
                else:
                    td = [1,3,5,7]
                    
                next_balls = []
                for nd in td:
                    next_balls.append((nm,ns,nd))
                temp[r][c] = next_balls
                
        for r in range(N):
            for c in range(N):
                graph[r][c] = temp[r][c]
       
    N,M,K = map(int,input().split())
    graph = [[[] for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        r,c,m,s,d = map(int,input().split())
        graph[r-1][c-1].append((m,s,d))
    
    for _ in range(K):
        move()
        # for g in graph:
        #     print(*g)
        
    answer = 0
    for r in range(N):
        for c in range(N):
            for m,_,_ in graph[r][c]:
                answer += m
   
    return answer 

print(solution())
'''
그래프 크기 매우 작음
그래프 칸 별로 파이어볼을 관리해도 ok 
1. K번 이동 
    (1) 파이어볼 위치 업데이트 
    (2) 2개 이상 파이어볼 있는 칸에서 파이어볼 4개로 나누기 
2. 파이어볼 질량 합 출력 
'''