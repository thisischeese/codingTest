from collections import deque 

def solution(x, y, n):
    
    def bfs():
        answer = 1000000
        queue = deque([(x,0)])
        visited = [True]+[False for _ in range(x+1,y+1)]

        while(queue):
            curr_val,curr_step = queue.popleft() 
            
            if curr_val==y:
                answer = min(answer,curr_step)
                continue
            for next_val in [curr_val*3,curr_val*2,curr_val+n]:
                if next_val<=y and not visited[next_val-x]:
                    queue.append((next_val,curr_step+1))
                    visited[next_val-x]=True 

        return answer if answer!=1000000 else -1

    return bfs()
"""
dfs? 
y를 넘어가는 순간 더 이상 방문 x 


"""