import sys 

input = sys.stdin.readline

A, B, C = map(int, input().split())

def sol(A,B,C):
    if B == 1:
        return A%C
    else:
        temp = sol(A,B//2,C)
        if B%2 == 0:
            return temp*temp%C
        else:
            return temp*temp*A%C 
            
print(sol(A,B,C))