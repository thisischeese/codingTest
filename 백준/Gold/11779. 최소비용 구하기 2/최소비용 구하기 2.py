import sys 
import heapq 

INF = int(10e9)
input = sys.stdin.readline 

def find_path(start,end,parents):
    path = []

    curr = end 
    while(True):
        path.append(curr)
        if(curr==start):
            break 
        curr = parents[curr]

    return path[::-1]


def dijkstra(start,end):
    distance = [INF]*(N+1)
    distance[start] = 0 
    parents = [0 for _ in range(N+1)]
    
    queue = [] 
    # 누적 거리, 현재 노드, 경로 
    heapq.heappush(queue,(0,start))

    while(queue):
        curr_dist, curr_node = heapq.heappop(queue)

        if(curr_dist>distance[curr_node]):
            continue 

        if(curr_node==end):
            break 
        
        for next_node,next_cost in graph[curr_node]:
            
            new_cost = curr_dist + next_cost 
            
            if(distance[next_node]>new_cost):
                distance[next_node]=new_cost
                parents[next_node] = curr_node
                heapq.heappush(queue,(new_cost,next_node))

    path = find_path(start,end,parents)
    
    return distance[end], path 
    
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,c = map(int,input().split())
    graph[s].append((e,c)) # 도착 노드, 가중치
    
S,E = map(int,input().split())    
dist, path = dijkstra(S,E)

print(dist)
print(len(path))
for p in path:
    print(p,end=' ')

# 출발점과 도착점이 고정되었을 때 
#     최소 비용, 최단 경로에 포함되는 도시 개수, 경로 구하기 
# 항상 시작 -> 도착 경로 존재함 
# 노드 : 10^3 개
# 간선(양의 가중치) : 10^5 개
# 다익스트라 O(10^5log10^3)-> O(3*10**5)<10**8
# 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스
# 有 방향 그래프 
# 경로 추적 HOW? 리스트를 우선순위 큐에 삽입 or 역추적 리스트 관리 
# 주의할 점 : 리스트 복사 TC O(len(리스트)) -> 시간 초과 
# 역추적 리스트 관리 HOW? 부모 노드 기록 -> end to start 역추적 

