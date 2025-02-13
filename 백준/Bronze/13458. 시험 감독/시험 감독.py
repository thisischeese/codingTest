import sys 

n = int(sys.stdin.readline())
t = list(map(int,sys.stdin.readline().split()))
a,b=map(int,input().split())

cnt = n 
for i in t:
    i-=a
    if i>0:
        if i%b:
            cnt+=(i//b)+1
        else:
            cnt +=(i//b)
            
print(cnt)