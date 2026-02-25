import sys 
from collections import deque 
INF = int(10**8)
input = sys.stdin.readline 

def solution():

    def get_power(curr,next):
        if(curr==0):
            return 2
        elif(curr==next):
            return 1
        elif(abs(curr-next)==2):
            return 4
        else:
            return 3      
    
    answer = INF
    seq = list(map(int,input().split()))[:-1]
    n = len(seq)
    if(n==0): 
        return 0 
    dp = [[[INF]*5 for _ in range(5)]for _ in range(n+1)]
    dp[0][0][0] = 0
    
    for i in range(n):
        target =seq[i]
        for l in range(5):
            for r in range(5):
                if(dp[i][l][r]==INF): continue 
                if(target!=r):
                    dp[i+1][target][r] = min(dp[i+1][target][r],dp[i][l][r]+get_power(l,target))
                if(target!=l):
                    dp[i+1][l][target] = min(dp[i+1][l][target],dp[i][l][r]+get_power(r,target))
    for l in range(5):
        for r in range(5):
            answer = min(answer, dp[n][l][r])
    return answer 

print(solution())