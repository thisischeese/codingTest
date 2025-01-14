import sys 
from collections import deque

def update_score(score, x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    score_sum = 0

    while queue:
        x, y = queue.popleft()
        score_sum += score

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if data[nx][ny] == score:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return score_sum


def turn_dice(dir, x, y):
    global dice

    if dir == 0:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

    elif dir == 1:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    elif dir == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

    else:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    if dice[-1] > data[x][y]:
        dir = (dir + 1) % 4
    elif dice[-1] < data[x][y]:
        dir = (dir - 1) % 4

    return dir

n, m, k = map(int,sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
answer = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dice = [1, 2, 3, 4, 5, 6]
x, y, dir = 0, 0, 0

for _ in range(k):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 > nx or nx >= n or 0 > ny or ny >= m:
        nx = x + dx[dir] * (-1)
        ny = y + dy[dir] * (-1)
        dir = (dir + 2) % 4

    dir = turn_dice(dir, nx, ny)
    answer += update_score(data[nx][ny], nx, ny)

    x, y = nx, ny

print(answer)
