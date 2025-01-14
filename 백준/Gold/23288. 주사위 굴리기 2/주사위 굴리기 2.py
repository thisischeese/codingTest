from collections import deque

def get_score(score, x, y):
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


def turn(direction, x, y):
    global dice

    if direction == 0:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

    elif direction == 1:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    elif direction == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

    else:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    if dice[-1] > data[x][y]:
        direction = (direction + 1) % 4
    elif dice[-1] < data[x][y]:
        direction = (direction - 1) % 4

    return direction

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dice = [1, 2, 3, 4, 5, 6]
x, y, direction = 0, 0, 0

for _ in range(k):
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 > nx or nx >= n or 0 > ny or ny >= m:
        nx = x + dx[direction] * (-1)
        ny = y + dy[direction] * (-1)
        direction = (direction + 2) % 4

    direction = turn(direction, nx, ny)
    answer += get_score(data[nx][ny], nx, ny)

    x, y = nx, ny

print(answer)