import sys 
import heapq 

input = sys.stdin.readline 
INF = 1e8

def dijkstra(s):
    pq = [] 
    heapq.heappush(pq,(0,s)) # cost, vertex
    dist[s] = 0 

    while(pq):
        total, curr = heapq.heappop(pq)
        if(dist[curr]<total): 
            continue
        for next in arr[curr]:
            if(total+next[1]<dist[next[0]]):
                dist[next[0]] = total+next[1]
                heapq.heappush(pq,(dist[next[0]],next[0]))

def print_all(answer):
    for i in range(1,len(answer)):
        if(answer[i]==INF):
            print("INF")
        else:
            print(answer[i])

V,E = map(int,input().split())
K = int(input())

arr = [[] for _ in range(V+1)]
dist = [INF for _ in range(V+1)]

for _ in range(E): 
    u,v,w = map(int,input().split())
    arr[u].append((v,w)) # u to v cost w 

dijkstra(K) 
print_all(dist)


# 1<=V<=2*10^4
# E<=3*10^5 
# 모든 k to 정점별 최단거리 구해야 함
# 다익스트라 -> 3*10^5*4*log2 < 10*8