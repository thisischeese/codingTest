import sys 
from collections import deque 

input = sys.stdin.readline 
INF = 1e9 

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS01(sr,sc,er,ec):
    queue = deque() 
    queue.append((sr,sc))

    distance[sr][sc] = int(graph[sr][sc])

    while(queue): 
        curr_r, curr_c = queue.popleft() 

        if(curr_r == er and curr_c==ec): 
            break 

        for i in range(4): 
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if(0<=nr<N and 0<=nc<M): 
                cost = int(graph[nr][nc])
                if(distance[curr_r][curr_c]+cost<distance[nr][nc]):
                    distance[nr][nc] = distance[curr_r][curr_c] + cost 

                    if(cost==0):
                        queue.appendleft((nr,nc))
                    else: 
                        queue.append((nr,nc))
    return distance[er][ec]


M, N = map(int,input().split())
graph = []
distance = [[INF for _ in range(M)] for _ in range(N)] 

for i in range(N): 
    graph.append(list(input().strip()))

print(BFS01(0,0,N-1,M-1)) 
