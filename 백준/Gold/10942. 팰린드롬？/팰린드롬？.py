import sys 

input = sys.stdin.readline 

N = int(input())
numbers = list(map(int,input().split()))
M = int(input())
questions = [list(map(int,input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(N)]


for length in range(N+1):
    for s in range(N-length):
        e = s + length 
        if(s==e): 
            dp[s][e] = 1
        elif(s+1==e and numbers[s]==numbers[e]):
            dp[s][e] = 1
        elif(e-s>=2 and dp[s+1][e-1]==1 and numbers[s]==numbers[e]):
            dp[s][e] = 1

for qs,qe in questions:
    print(dp[qs-1][qe-1])