import sys
from collections import deque

input = sys.stdin.readline

def BFS(N, K):
    max_pos = 100001
    visited = [False] * max_pos
    queue = deque()
    queue.append((N, 0))
    visited[N] = True

    while queue:
        curr_pos, curr_time = queue.popleft()

        if curr_pos == K:
            return curr_time

        # 순간이동 (0초 소요): 큐 앞에 삽입
        next_pos = curr_pos * 2
        if 0 <= next_pos < max_pos and not visited[next_pos]:
            visited[next_pos] = True
            queue.appendleft((next_pos, curr_time))

        # 걷기 (-1, +1): 1초 소요
        for next_pos in [curr_pos - 1, curr_pos + 1]:
            if 0 <= next_pos < max_pos and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, curr_time + 1))

N, K = map(int, input().split())
print(BFS(N, K))
