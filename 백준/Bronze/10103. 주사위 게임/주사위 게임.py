import sys 

chang=100
sang=100

n = int(sys.stdin.readline())
for _ in range(n):
    c,s = map(int,sys.stdin.readline().split())
    if c>s:
        sang-=c
    elif s>c:
        chang-=s
    else:
        continue
print(chang,sang,sep='\n')