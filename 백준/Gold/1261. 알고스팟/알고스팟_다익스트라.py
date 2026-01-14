import sys 
import heapq 

input = sys.stdin.readline 
INF = 1e9 

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def dijkstra(sr,sc,er,ec):

    queue = [] 
    heapq.heappush(queue,(int(graph[sr][sc]),sr,sc))
    distance[sr][sc] = int(graph[sr][sc])

    while(queue): 
      curr = heapq.heappop(queue)
      curr_dist = curr[0]
      curr_r,curr_c = curr[1], curr[2]

      if(distance[curr_r][curr_c]<curr_dist):
         continue 
      
      if(curr_r==er and curr_c==ec):
         break

      for i in range(4): 
         nr = curr_r + dr[i]
         nc = curr_c + dc[i]  
         if(0<= nr and nr<N and 0<=nc and nc<M and curr_dist+int(graph[nr][nc])<distance[nr][nc]):
            distance[nr][nc] = curr_dist+int(graph[nr][nc])
            heapq.heappush(queue,(distance[nr][nc],nr,nc))

    return distance[er][ec]

M, N = map(int,input().split())
graph = []
distance = [[INF for _ in range(M)] for _ in range(N)] 

for i in range(N): 
    graph.append(list(input().strip()))

print(dijkstra(0,0,N-1,M-1)) 



# 벽을 최소 몇 개 부수어야 하는가? 
# (0,0) -> (n-1,m-1) 이동 최단거리 (0+1+...)
# 시작점과 종료점 고정됨 
# 간선 가중치 x 그래프 -> BFS
# 100x100 행렬 그래프 
