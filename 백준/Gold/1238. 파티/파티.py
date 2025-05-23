import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
max_time = 0


def dijkstra(start, graph):
    distance = [INF] * (N + 1)
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for neighbor, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(hq, (new_cost, neighbor))
    return distance

N, M, X = map(int, input().split())
roads = [[] for _ in range(N + 1)]
reverse_roads = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    roads[start].append((end, cost))
    reverse_roads[end].append((start, cost))  
    
to_home = dijkstra(X, roads)

to_party = dijkstra(X, reverse_roads)

for i in range(1, N + 1):
    total_time = to_home[i] + to_party[i]
    max_time = max(max_time, total_time)

print(max_time)
