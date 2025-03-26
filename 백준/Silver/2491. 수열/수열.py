import sys 

N = int(sys.stdin.readline())
seq = list(map(int,sys.stdin.readline().split()))
up = [1 for _ in range(N)]
down = [1 for _ in range(N)]

for i in range(N-1):
    if seq[i]>=seq[i+1]:
        down[i] = max(down[i],down[i-1]+1)
    if seq[i]<= seq[i+1]:
        up[i] = max(up[i],up[i-1]+1)

        
print(max(max(up),max(down)))        