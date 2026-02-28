import sys 

input = sys.stdin.readline 

def solution():
    answer = 0
    N = int(input())
    graph = [[0]*N for _ in range(N)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    # seq = []
    like_dict = {}
    
    for _ in range(N*N):
        temp = list(map(int,input().split()))
        # seq.append(temp)
        like_dict[temp[0]] = temp[1:]
 
    def simulation(self,like):
        # 클수록, 클수록, 작을수록, 작을수록 
        best_pos = (-1,-1,-N,-N)

        for cr in range(N):
            for cc in range(N):
                if(graph[cr][cc]!=0):   
                    continue 
                like_cnt = 0
                empty_cnt = 0 
                for i in range(4):
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if(0<=nr<N and 0<=nc<N):
                        if(graph[nr][nc] in like):
                            like_cnt += 1
                        elif(graph[nr][nc]==0):
                            empty_cnt += 1 
                # heapq.heappush(pq,(-like_cnt,-empty_cnt,cr,cc))
                curr_pos = (like_cnt,empty_cnt,-cr,-cc)
                if(curr_pos > best_pos):
                    best_pos = curr_pos 
                # print(f"-like_cnt:{-like_cnt},-empty_cnt:{-empty_cnt},cr:{cr},cc:{cc}")
        # a_like,a_empty,ar,ac = heapq.heappop(pq)
        # print(f"a_like:{a_like},a_empty:{a_empty},ar:{ar},ac:{ac}")
        return -best_pos[2],-best_pos[3]
                
        
    for key in like_dict.keys(): 
        r,c = simulation(key,like_dict[key])
        graph[r][c] = key 
        # for g in graph:
        #     print(*g)
        
    for cr in range(N):
        for cc in range(N):
            cnt = 0
            like = like_dict[graph[cr][cc]]
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if(0<=nr<N and 0<=nc<N and graph[nr][nc] in like):
                    cnt += 1
            if(cnt==1):
                answer += 1
            elif(cnt==2):
                answer += 10 
            elif(cnt==3):
                answer += 100 
            elif(cnt==4):
                answer += 1000

            # print(f"cr:{cr},cc:{cc},cnt:{cnt},answer:{answer}")
         
    return answer 

print(solution())
'''
시뮬레이션
빈 칸 중 한 칸에 학생 1명을 배치한다 
칸의 우선순위 조건 
인접 칸 좋아하는 학생 수 최대 > 인접 칸 빈 칸 최대 > 행 숫자 최소 > 열 숫자 최소  

조건에 의하면 한 시점에 학생이 앉을 위치는 고정된다. 
조건을 어떻게 처리할 것인가? 우선순위 큐에서 pop 시켜서 조건 만족하는 최적 한 개 구하기 

1. seq을 순회하며 학생의 위치를 정한다. 
(1) 좋아하는 사람을 반영해 graph를 순회하며 큐를 업데이트 한다. 
(2) 큐에서 하나를 우선순위 가장 높은 튜플 하나를 뽑는다
(3) 튜플의 r,c에 self를 기록한다 
2. graph를 순회하며 학생의 만족도를 합한다. 


1e8인데 
N 최대 20 
heapq는 값 오름차순 순으로 정렬 



'''