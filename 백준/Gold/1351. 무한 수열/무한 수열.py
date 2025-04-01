import sys 
sys.setrecursionlimit(10000)

seq = {0:1,1:2}

N,P,Q = map(int,sys.stdin.readline().split())
P, Q = min(P,Q),max(P,Q)

def solution(n):
    
    if n in seq.keys():
        return 
    
    if n//P not in seq.keys():
        solution(n//P)  
    if n//Q not in seq.keys():
        solution(n//Q)
        
    seq[n] = seq[n//P] + seq[n//Q] 
    
solution(N)        
print(seq[N])        