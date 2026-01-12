import sys

input = sys.stdin.readline

def fac(n):
    if(n<=1):
        return 1 
    return n*fac(n-1)

N,K = map(int,input().split())

print(fac(N)//(fac(N-K)*fac(K)))

# nCk = n!/k!*(n-k)!
