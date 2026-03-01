import sys

input = sys.stdin.readline 

def solution():
    dr = [0,0,-1,-1,-1,0,1,1,1]
    dc = [0,-1,-1,0,1,1,1,0,-1]
        
    def get_cloud():
        temp = []
        for r in range(N):
            for c in range(N):
                if(graph[r][c]>=2 and not visited[r][c]):
                    graph[r][c] -= 2
                    temp.append((r,c))
                visited[r][c] = False 
        
        return temp 
                    
        
    def move_clouds(dir,cnt):
        temp = []
        for cr,cc in clouds:
            nr = (cr + dr[dir]*cnt)%N
            nc = (cc + dc[dir]*cnt)%N 

            temp.append((nr,nc))
            
        for r,c in temp:
            graph[r][c] += 1
            
        for cr,cc in temp:
            cnt = 0 
            for i in range(2,9,2):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if(0<=nr<N and 0<=nc<N and graph[nr][nc]!=0):
                    cnt += 1
            graph[cr][cc] += cnt 

        return temp 
        
    # def rain():
    #     for r,c in clouds:
    #         graph[r][c] += 1
            
    # def magic():
    #     # 2,4,6,8 
    #     for cr,cc in clouds:
    #         cnt = 0 
    #         for i in range(2,9,2):
    #             nr = cr + dr[i]
    #             nc = cc + dc[i]
    #             if(0<=nr<N and 0<=nc<N and graph[nr][nc]!=0):
    #                 cnt += 1
    #         graph[cr][cc] += cnt 
            
            
    N,M = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    move = [list(map(int,input().split())) for _ in range(M)]
    visited = [[False]*N for _ in range(N)]
    clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

    for i in range(len(move)):
        clouds = move_clouds(move[i][0],move[i][1])
        for cr,cc in clouds:
            visited[cr][cc] = True 
        # rain()
        # magic()
        clouds = get_cloud() 

    return sum(map(sum,graph)) 
                
print(solution())

'''
뭐가 어찌되었든.. 시뮬레이션 
규칙이 복잡한.. 
이동은 최대 100회 

graph 업데이트 
구름 좌표 계산 후 저장, 업데이트  

1. seq 순회하며 구름 좌표 계산 + 저장 
2. 비가 내려 그래프 업데이트 
3. 물복사버그 : 구름 좌표별로 순회하며 대각선 4방향 0 아닌 개수 세서 graph 업데이트 
4. 그래프 순회하며 직전에 구름 좌표가 아니었던 좌표 중 물의 양이 2이상인 칸을 구름 좌표로 지정하고 그래프 업데이트 
5. 이동 끝나고 그래프 순회하며 총합 출력하기 
'''