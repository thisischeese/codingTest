from collections import deque 

def solution(land):
    answer = [0]
    oil = {}
    
    row_length = len(land)
    col_length = len(land[0])
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    def bfs(sr,sc,idx):
        total = 0
        
        queue = deque() 
        
        land[sr][sc] = idx 
        queue.append((sr,sc))
        
        while(queue):
            cr,cc = queue.popleft()
            total += 1
            
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if (0<=nr<row_length and 0<=nc<col_length and land[nr][nc]==1):
                    land[nr][nc] = idx 
                    queue.append((nr,nc))
                
        return total 
        
        
    idx = 2
    for r in range(row_length):
        for c in range(col_length):
            if land[r][c]==1:
                val = bfs(r,c,idx)
                oil[idx] = val
                idx += 1
    # print(land)  
    # print(oil)
    for c in range(col_length):
        temp = []
        for r in range(row_length):
            temp.append(land[r][c])  
        answer.append(sum([oil[idx] for idx in set(temp) if idx>=2]))
    
    return max(answer)


"""
1. land를 bfs로 탐색하며 (덩어리 인덱스, 덩어리 석유량)을 자료구조에 기록하고 셀에는 덩어리 인덱스 기록 
2. 열에 기록된 덩어리 인덱스 unique 값에 대한 석유량을 더하고 answer에 기록한다. 
3. answer return 

"""