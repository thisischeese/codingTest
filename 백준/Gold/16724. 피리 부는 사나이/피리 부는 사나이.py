import sys 
from collections import deque 

input = sys.stdin.readline 

def solution():
    answer = 0
    cnt = 0
    N,M = map(int,input().split())
    graph = [list(input().strip()) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    
    def BFS(sr,sc,cnt):
        queue = deque() 
        queue.append((sr,sc))
        visited[sr][sc] = cnt

        while(queue):
            cr, cc = queue.popleft() 
            if(graph[cr][cc]=="D"):
                nr = cr + 1 
                nc = cc
            elif(graph[cr][cc]=="U"):
                nr = cr - 1
                nc = cc 
            elif(graph[cr][cc]=="R"):
                nr = cr 
                nc = cc + 1
            else:
                nr = cr
                nc = cc - 1             

            if(0<=nr<N and 0<=nc<M):
                if(visited[nr][nc]==0):
                    queue.append((nr,nc))
                    visited[nr][nc] = cnt 
                elif(visited[nr][nc]==cnt):
                    return 1
                elif(visited[nr][nc]<cnt):
                    return 0 
        return 0
                

    for i in range(N):
        for j in range(M):
            if visited[i][j]==0:
                cnt += 1
                answer += BFS(i,j,cnt)
                
    return answer 

print(solution())

'''
지도 내부에 사이클이 최소 몇개 존재하는가? 
경로는 이미 정해짐
시작점에 따라 사이클을 덜 포착할 수 있다는 것임

visited 배열을 cnt로 기록 
BFS를 돌리다가 자신과 같은 cnt를 만나면 == 사이클 발생 모두 탐색했으며 더 이상 탐색 불가 return 1
              자신보다 작은 (not 0) 만나면 이전 그룹과 합쳐져야 함 return 0 
              0 만나면 한 번도 가본 적 없는 길 경로에 추가

'''