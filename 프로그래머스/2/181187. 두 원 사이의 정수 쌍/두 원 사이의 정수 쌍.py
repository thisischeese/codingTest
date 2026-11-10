from math import isqrt

def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        max_y = isqrt(r2**2 - x**2)

        if x >= r1:
            min_y = 0
        else:
            n = r1**2 - x**2
            min_y = isqrt(n)

            if min_y**2 < n:
                min_y += 1

        answer += max_y - min_y + 1

    return answer * 4