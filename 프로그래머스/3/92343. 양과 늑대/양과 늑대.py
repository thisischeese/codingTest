from collections import deque 

def solution(info, edges):

    answer = 0
    adj = [[] for _ in range(len(info)+1)]
    for se,ee in edges:
        adj[se].append(ee)
        
    def dfs(sheep_cnt, wolf_cnt,candidates):
        nonlocal answer
        answer = max(answer,sheep_cnt)
        
        for candidate in candidates:
            temp_sheep_cnt = sheep_cnt + (info[candidate]==0)
            temp_wolf_cnt = wolf_cnt + (info[candidate]==1)
            if temp_sheep_cnt<=temp_wolf_cnt:
                continue 
            # 자식과 형제만 다음에 방문 가능함 
            next_candidates = (candidates-{candidate}|set(adj[candidate]))
            dfs(temp_sheep_cnt,temp_wolf_cnt,next_candidates)
        
        answer = max(answer,sheep_cnt)

 
    dfs(1,0,set(adj[0]))
    return answer

