import sys 

min_wait = pow(2,31)
N, T = map(int,sys.stdin.readline().split())
info = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for s,l,c in info:
    for time in range(s,s+l*c,l):
        if time >= T:
            min_wait = min(min_wait,time-T)
            break
if min_wait == pow(2,31):
    print(-1)
else:
    print(min_wait)

