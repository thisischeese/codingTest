import sys
from collections import deque

def bfs(start, fruits, graph):
    N = len(fruits)
    distances = [-1] * (N + 1)
    paths = [[start, start] for _ in range(N + 1)]
    distances[start] = fruits[start - 1]

    queue = deque([[start, start]]) 
    max_sum = 0
    max_nodes = []

    while queue:
        current, origin = queue.popleft()

        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + fruits[neighbor - 1]
                paths[neighbor] = [origin, neighbor]
                queue.append([neighbor, origin])

                if distances[neighbor] > max_sum:
                    max_sum = distances[neighbor]
                    max_nodes = [neighbor]
                elif distances[neighbor] == max_sum:
                    max_nodes.append(neighbor)

    result = {}
    for node in max_nodes:
        result[node] = [distances[node], min(paths[node])]

    return result

N = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))
graph = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

first_search = bfs(1, fruits, graph)

max_total = -1
answer_node = -1
for node in first_search:
    second_search = bfs(node, fruits, graph)
    for target in second_search:
        total = second_search[target][0]
        start_node = second_search[target][1]
        if total > max_total:
            max_total = total
            answer_node = start_node
        elif total == max_total:
            answer_node = min(answer_node, start_node)

if N == 1:
    print(fruits[0], 1)
else:
    print(max_total, answer_node)
