import sys

N,M = map(int,sys.stdin.readline().split())

n=min(N,M)
m=max(N,M)

print((n-1)+(m-1)*n)
