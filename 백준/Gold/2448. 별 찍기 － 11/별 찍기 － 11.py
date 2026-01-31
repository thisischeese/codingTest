import sys 
import math 

input = sys.stdin.readline 


def print_tri(i,j,n):
    if n==3:
        stars[i][j] = '*'
        stars[i+1][j-1] = stars[i+1][j+1] = '*'
        for k in range(-2,3):
            stars[i+2][j+k] ="*"
    else:
        print_tri(i,j,n//2)
        print_tri(i+n//2,j-n//2,n//2)
        print_tri(i+n//2,j+n//2,n//2)
        
        

N = int(input())
stars = [[' ']*2*N for _ in range(N)]
print_tri(0,N-1,N)
for s in stars:
    print("".join(s))


    