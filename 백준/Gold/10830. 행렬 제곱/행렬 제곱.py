import sys 

N, B = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def dot(X,Y):
    # X,Y의 크기 같다고 가정 
    temp = [[0 for _ in range(len(X))] for _ in range(len(X))]
    for i in range(len(temp)):
        for j in range(len(temp)):
            for k in range(len(temp)):
                temp[i][j] += X[i][k]*Y[k][j] 
            temp[i][j] %= 1000
    return temp                 
                
def power(a, n):
    if n == 0:
        # 항등행렬 : 대각성분만 1
        return [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    
    x = power(a, n//2)

    if n % 2 == 0:
        return dot(x,x)
    
    else:
        return dot(dot(x,x),a)
        
answer = power(A,B)   

for row in answer:
    print(*row)