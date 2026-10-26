def solution(dirs):
    answer = 0
    sr = 0
    sc = 0

    move = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }

    visited = set()

    for dir in dirs:
        nr = sr + move[dir][0]
        nc = sc + move[dir][1]

        if not (-5 <= nr <= 5 and -5 <= nc <= 5):
            continue

        path = tuple(sorted([(sr, sc), (nr, nc)]))

        if path not in visited:
            visited.add(path)
            answer += 1

        sr, sc = nr, nc

    return answer