import sys 
import heapq 

INF = 1e8
input = sys.stdin.readline 

def dijkstra(start):
    distance = [INF for _ in range(V+1)]
    distance[start] = 0 
    
    queue = []
    heapq.heappush(queue,(0,start))
    

    while(queue):
        curr_dist,curr_idx = heapq.heappop(queue)

        for next_idx, next_cost in adj[curr_idx]:
            temp_dist = next_cost + distance[curr_idx]
            if (temp_dist<=distance[next_idx]):
                distance[next_idx] = temp_dist
                heapq.heappush(queue,(temp_dist,next_idx))
      
    return distance 

V = int(input())
adj = [[] for _ in range(V+1)]
leaves = [False for _ in range(V+1)]

for i in range(1,V+1):
    temp = list(map(int,input().split()))
    idx = temp[0]
    for i in range(1,len(temp)-1,2):
        adj[idx].append((temp[i],temp[i+1])) # 연결된 idx, 가중치 

max_dist = -1 
start_idx=1
distance =  dijkstra(1)
for i in range(1,len(distance)):
    if(max_dist<distance[i]):
        max_dist=distance[i]
        start_idx = i 

max_dist = -1 
distance = dijkstra(start_idx)
for i in range(1,len(distance)):
    if(max_dist<distance[i]):
        max_dist = distance[i]

print(max_dist)

    

'''
모든 노드가 연결되어 있는지는 잘 모르겠는데..
트리라 함은 모든 노드가 연결되어 있음을 가정하는 것이겠죠..? 

1. 한 노드에서 다른 노드까지의 거리 구하기 
2. 그 중 가장 긴 거리의 idx 구하기 
3. 그 노드에서 다른 노드까지의 거리 구하기
3. 그 중 가장 긴 거리가 정답 
'''