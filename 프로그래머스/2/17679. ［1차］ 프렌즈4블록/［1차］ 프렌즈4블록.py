from collections import deque 

def solution(m, n, board):
    answer = 0
    
    for r in range(m):
        board[r] = [b for b in board[r]]
     
    def check(r,c):
        c1 = board[r][c]
        c2 = board[r+1][c]
        c3 = board[r][c+1]
        c4 = board[r+1][c+1]
        if (c1!="" and 65<=ord(c1)<=90 and c1==c2 and c2==c3 and c3==c4):
            return True 
        return False

    while(True):
        visited = [[False for _ in range(n)] for _ in range(m)]
        temp = 0 
        for r in range(m-1):
            for c in range(n-1):
                if check(r,c):
                    temp += 1
                    visited[r][c]=True
                    visited[r+1][c]=True
                    visited[r][c+1]=True
                    visited[r+1][c+1]=True
        if temp==0: break 
        
        
        # delete 
        for r in range(m):
            for c in range(n):
                if visited[r][c]:
                    answer += 1
                    board[r][c] = ""
                    
        # push update 
        for c in range(n):
            queue = deque([])
            for r in range(m):
                if board[r][c]!="":
                    queue.append(board[r][c])
            for i in range(m-len(queue)):
                queue.appendleft("")
            for r in range(m):
                board[r][c] = queue.popleft()

    return answer

"""
시뮬레이션 
한 변의 길이가 2인 정방향 블록을 모두 찾는다. 찾을 때마다 answer+=1 하고 방문 표시한다. 
방문 체크된 블록을 한 번에 삭제한다. 
나머지 블록에 대해 빈 공간을 제거한다. 
한 변의 길이가 2인 정방향 블록이 0개일 때 종료하고 answer 반환한다. 

정방향 블록을 어떻게 찾아낼 것인가

시작 노드가 이미 방문이라면 더 이상 방문하지 않기.. 
4개의 노드 종류가 모두 동일하다면?
4개의 노드 모두 방문 처리하기 
다르다면 나가기 
"""