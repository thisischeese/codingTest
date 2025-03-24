import sys 

total = 0 
N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
P.sort()

for i in range(N):
    total += P[i]*(N-i)

print(total)