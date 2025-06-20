import sys
from collections import deque

input = sys.stdin.readline

def BFS(N, K):
    cnt = 0
    min_time = 1e9
    visited = [1e9] * 100001
    queue = deque([(0, N)])
    visited[N] = 0

    while queue:
        time, node = queue.popleft()

        if time > min_time:
            break

        if node == K:
            if time < min_time:
                min_time = time
                cnt = 1
            elif time == min_time:
                cnt += 1
        else:
            for next_node in [node - 1, node + 1, node * 2]:
                if 0 <= next_node <= 100000 and visited[next_node] >= time + 1:
                    visited[next_node] = time + 1
                    queue.append((time + 1, next_node))

    return min_time, cnt

N, K = map(int, input().split())

time, cnt = BFS(N, K)
print(time)
print(cnt)
