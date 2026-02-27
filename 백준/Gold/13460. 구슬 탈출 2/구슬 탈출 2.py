import sys 
from collections import deque 

input = sys.stdin.readline 

def solution():
    # N행 M열 
    N, M = map(int,input().split())
    graph = [list(input().strip()) for _ in range(N)]
    visited = [[[[False for _ in range(M)]for _ in range(N)] for _ in range(M)]for _ in range(N)]
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    rr = 0
    rc = 0
    br = 0
    bc = 0

    for i in range(N):
        for j in range(M):
            if(graph[i][j]=="R"):
                rr = i
                rc = j 
                graph[i][j]="."
            if(graph[i][j]=="B"):
                br = i
                bc = j  
                graph[i][j]="."

    def BFS():
        queue = deque() 
        queue.append((0,rr,rc,br,bc))
        visited[rr][rc][br][bc] = True 
        
        while(queue):
            curr_cnt,curr_rr,curr_rc,curr_br,curr_bc = queue.popleft() 
            #print(curr_cnt,curr_rr,curr_rc,curr_br,curr_bc)
            if(curr_cnt>10):
                continue 
            elif(graph[curr_br][curr_bc]=="O"):
                continue 
            elif(graph[curr_rr][curr_rc]=="O"):
                return curr_cnt 

                
            next_cnt = curr_cnt+1

            
            for i in range(4):
                next_rr = curr_rr
                next_rc = curr_rc 
                next_br = curr_br 
                next_bc = curr_bc 
                while(0<=next_rr<N and 0<=next_rc<M):
                    next_rr += dr[i]
                    next_rc += dc[i]
                    if(graph[next_rr][next_rc]=="#"):
                        next_rr -= dr[i]
                        next_rc -= dc[i]
                        break                         
                    elif(graph[next_rr][next_rc]=="O"):
                        break 
                while(0<=next_br<N and 0<=next_bc<M):
                    next_br += dr[i]
                    next_bc += dc[i]
                    if(graph[next_br][next_bc]=="#"):
                        next_br -= dr[i]
                        next_bc -= dc[i]
                        break                         
                    if(graph[next_br][next_bc]=="O"):
                        break 
                
                #print("next : ",next_rr,next_rc,next_br,next_bc)
                if(graph[next_br][next_bc]!="O" and graph[next_rr][next_rc]!="O" and next_rr == next_br and next_rc == next_bc):
                    # 더 많이 움직인 쪽을 한 칸 뒤로 밀기 
                    if(abs(next_rr-curr_rr)+abs(next_rc-curr_rc)<abs(next_br-curr_br)+abs(next_bc-curr_bc)):
                        next_br -= dr[i]
                        next_bc -= dc[i]
                    else:
                        next_rr -= dr[i]
                        next_rc -= dc[i]
                        
                if(not visited[next_rr][next_rc][next_br][next_bc]):
                    visited[next_rr][next_rc][next_br][next_bc] = True 
                    queue.append((next_cnt,next_rr,next_rc,next_br,next_bc))        

        return -1
    
    
    return BFS() 
    
print(solution())
'''
4방향 중 한 방향이 확정된다면 
빨간 구슬, 파란 구슬의 굴러가는 순서, 방향, 장애물 여부, 장애물 만나는 순서는 고정됨? 
r next == b next -> 가장 최근에 움직인 next를 이전 값으로 1칸 밀어버린다 
모든 공은 #을 만나는 순간 이전 값으로 1칸 밀고 업데이트하지 않는다 
r_next가 O를 먼저 만났다면 b_next가 이후 같은 시간대 안에 O를 만나지 않는다면 성공
만난다면 실패
b_next가 O를 먼저 만났다면 (r_next가 만나지 않았는데) 실패 


'''