def solution(n):
    DIV = 1234567

    if n==2:
        return 1
    
    p0 = 1
    p1 = 2

    for _ in range(3, n + 1):
        p0, p1 = p1, (p0 + p1) % DIV

    return p0