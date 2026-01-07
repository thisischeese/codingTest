import sys 

input = sys.stdin.readline 

N = int(input())
sizes = list(map(int,input().split()))
t,p = map(int,input().split())

answer_t = 0 
for size in sizes:
    if(size%t==0):
        answer_t += size//t
    else: 
        answer_t += size//t+1

print(answer_t)
print(N//p,N%p)