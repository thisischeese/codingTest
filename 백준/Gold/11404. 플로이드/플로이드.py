import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(n + 1): graph[_][_] = 0

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    if graph[s][e] > c:
        graph[s][e] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):

            if j == k:
                graph[j][k] = 0

            else:
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()