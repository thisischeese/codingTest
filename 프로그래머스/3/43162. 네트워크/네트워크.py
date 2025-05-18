from collections import deque 

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i]==False:
            visited = BFS(i,visited,n,computers)
            answer += 1
                 
    return answer

def BFS(start,visited,n,computers):
    
    queue = deque([start])
    while(len(queue)):
        idx = queue.pop()
        for i in range(len(computers[idx])):
            if (i!=idx and computers[idx][i]==1 and visited[i]==False):
                queue.append(i)
                visited[i]=True
    
    return visited