from collections import deque 

def solution(begin, target, words):
    
    def cal_diff(curr,next):
        cnt =0 
        for c,n in zip(curr,next):
            if(c!=n):
                cnt+=1 
        return cnt 
        
    def bfs(b, t):
        
        visited = {word : False for word in words}
        
        queue = deque()
        queue.append((b,0))
        
        while(queue):
            curr,total = queue.popleft()
            visited[curr] = True 
            
            if(curr==t):
                return total 
            
            for next in words:
                if(visited[next]==False and cal_diff(curr,next)==1):
                    queue.append((next,total+1))
            
        return 0 
        
    return bfs(begin,target)

"""
완전탐색 풀이법 
1. 모든 words를 순회하며 curr과 몇개 차이나는지 확인한다. 
2. 1개 차이 나는 경우가 존재한다면 큐에 넣는다. 
3. 큐에서 빼고 visited 처리한다. 
4. 모든 words 순회하며 방금 뺀 것과 몇 개 차이나는지 확인한다. 
5. 1개 차이 나는 경우가 존재한다면 큐에 넣는다. (넣을 때 total +1 처리)
6. 만약에 없다? 없으면 넣지 않는다. 
.. 반복
7. 반복하다가 큐에서 뺀 것이 target 과 동일하다. 동일하다면 total을 return 해줄 것 
8. 큐가 빌 때까지 반복하는데도 종료 안했응면 0 return 
"""