import sys 
import math 
input = sys.stdin.readline 

def solution():
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]
    N,M,K = map(int,input().split())
    fireballs = [] 
    
    for _ in range(M):
        r,c,m,s,d = map(int,input().split())
        # graph[r-1][c-1].append((m,s,d))
        fireballs.append((r-1,c-1,m,s,d))
    
    for _ in range(K):
        graph = {}
        new_fireballs = []
        for r,c,m,s,d in fireballs:
            nr = (r + dr[d]*s)%N
            nc = (c + dc[d]*s)%N
            if((nr,nc) not in graph):
                graph[(nr,nc)] = []
            graph[(nr,nc)].append((m,s,d))

        for (r,c),balls in graph.items():
            if len(graph[(r,c)])<2:
                for m,s,d in balls:
                    new_fireballs.append((r,c,m,s,d))
                continue 
            cnt = 0 
            tm = 0
            ts = 0 
            even_cnt = 0
            odd_cnt = 0 
            for m,s,d in balls:
                cnt += 1
                tm += m 
                ts += s 
                if d%2==0:
                    even_cnt += 1
                else:
                    odd_cnt += 1
                
            nm = tm//5
            ns = ts//cnt  
            if(nm==0):
                continue 

            if(even_cnt==cnt or odd_cnt==cnt):
                td = [0,2,4,6]
            else:
                td = [1,3,5,7]
                
            for nd in td:
                new_fireballs.append((r,c,nm,ns,nd))
        fireballs = new_fireballs

   
    return sum(ball[2] for ball in fireballs) 

print(solution())
'''
그래프 크기 매우 작음
그래프 칸 별로 파이어볼을 관리해도 ok 
1. K번 이동 
    (1) 파이어볼 위치 업데이트 
    (2) 2개 이상 파이어볼 있는 칸에서 파이어볼 4개로 나누기 
2. 파이어볼 질량 합 출력 
'''