from collections import deque

def solution(priorities, location):
    queue = deque((p, i) for i, p in enumerate(priorities))
    cnt = 0

    while queue:
        curr_p, curr_i = queue.popleft()

        if any(curr_p < p for p, _ in queue):
            queue.append((curr_p, curr_i))
        else:
            cnt += 1

            if curr_i == location:
                return cnt