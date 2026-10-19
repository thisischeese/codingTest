def solution(info, n, m):
    answer = int(1e6)
    items_cnt = len(info)
    visited = set()
    
    def bt(a,b,idx):
        nonlocal answer
        
        if idx==items_cnt:
            answer = min(answer,a)
            return 
        
        if (a,b,idx) in visited:
            return 
        
        visited.add((a,b,idx))
        
        if a+info[idx][0]<n:
            bt(a+info[idx][0],b,idx+1)
        if b+info[idx][1]<m:
            bt(a,b+info[idx][1],idx+1)
            
    bt(0,0,0)
    return answer if answer!=int(1e6) else -1


"""
백트래킹인데
n개 또는 m개 이상이면 탐색 중단
그리고 모든 물건 탐색하지 않았다면 a 훔친 개수 업데이트 안함. 
"""