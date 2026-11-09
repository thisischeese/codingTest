from collections import deque 

def solution(rows, columns, queries):
    
    INF = float('inf')
    
    result = []
    queue = deque() 
    
    board = [[i for i in range(j,j+columns)] \
             for j in range(1,rows*columns,columns)]
    
    for r1,c1,r2,c2 in queries:
        r1 -=1
        c1 -=1
        r2 -=1
        c2 -=1 
        
        min_result = INF
        # 맨위넣기 -> 
        cr = r1
        for cc in range(c1,c2+1):
            queue.append(board[cr][cc])
            min_result = min(min_result,board[cr][cc])
        # 오른쪽넣기 down
        cc = c2
        for cr in range(r1+1,r2):
            queue.append(board[cr][cc])
            min_result = min(min_result,board[cr][cc])
        # 맨아래넣기 <-
        cr = r2
        for cc in range(c2,c1-1,-1):
            queue.append(board[cr][cc])
            min_result = min(min_result,board[cr][cc])
        # 왼쪽넣기 up 
        cc = c1
        for cr in range(r2-1,r1,-1):
            queue.append(board[cr][cc])
            min_result = min(min_result,board[cr][cc])
        
        result.append(min_result)
        # queue에서 하나 빼서 돌리기 
        tail = queue.pop()
        queue.appendleft(tail)
        # 맨위넣기 -> 
        cr = r1
        for cc in range(c1,c2+1):
            board[cr][cc]=queue.popleft() 
        # 오른쪽넣기 down
        cc = c2
        for cr in range(r1+1,r2):
            board[cr][cc]=queue.popleft() 
        # 맨아래넣기 <-
        cr = r2
        for cc in range(c2,c1-1,-1):
            board[cr][cc]=queue.popleft() 
        # 왼쪽넣기 up 
        cc = c1
        for cr in range(r2-1,r1,-1):
            board[cr][cc]=queue.popleft() 
        
        # 비우기 
        queue.clear() 
        
    
    return result

"""
0. r,c 맞춰서 board 만들기 
1. 1~3을 모든 query에 대해 반복한다. 
2. query에 해당하는 사각형 테두리 구간을 찾느다. 
3. 현재 상태에서 가장 작은 수를 구하고 result에 저장한다. 
4. 시계방향으로 한 칸씩 회전하고 board 업데이트한다. 
"""