import sys

n, m = map(int, sys.stdin.readline().split())  
r, c, direction = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]

visited[r][c] = 1
clean_count = 1

while True:
    cleaned = False

    for _ in range(len(d_row)):
        direction = (direction + 3) % 4 
        next_r = r + d_row[direction]
        next_c = c + d_col[direction]

        if (0 <= next_r < n) and (0 <= next_c < m) and (room[next_r][next_c]) == 0:
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = 1 
                clean_count += 1  
                r, c = next_r, next_c  
                cleaned = True  
                break  

    if not cleaned:
        back_r = r - d_row[direction]
        back_c = c - d_col[direction]

        if room[back_r][back_c] == 1:
            print(clean_count)
            break

        r, c = back_r, back_c
