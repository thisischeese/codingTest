import sys 

input = sys.stdin.readline 

while(True):
    n,m = map(int,input().split())
    if(n==0 and m==0):
        sys.exit()
    if(n>m):
        print("Yes")
    else:
        print("No")
