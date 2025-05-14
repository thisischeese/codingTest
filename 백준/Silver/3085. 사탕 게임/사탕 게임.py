import sys 
from collections import Counter 

answer = 0

def check(N,colors):
    max_num = 0 
    for i in range(N):
        cnt = 1 
        for j in range(1,N):
            if colors[i][j] == colors[i][j-1]:
                cnt +=1 
                max_num = max(max_num,cnt)
            else:
                cnt = 1
        
    for j in range(N):
        cnt = 1 
        for i in range(1,N):
            if colors[i][j] == colors[i-1][j]:
                cnt +=1 
                max_num = max(max_num,cnt)
            else:
                cnt = 1
        
    return max_num
        
                

N = int(sys.stdin.readline())
colors =[list(map(str,sys.stdin.readline().strip())) for _ in range(N)]

for i in range(N):
    for j in range(N-1):
        if colors[i][j]!=colors[i][j+1]:
            colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]
            answer = max(answer,check(N,colors))
            colors[i][j], colors[i][j+1] = colors[i][j+1], colors[i][j]

for i in range(N-1):
    for j in range(N):
        if colors[i][j]!=colors[i+1][j]:
            colors[i][j], colors[i+1][j] = colors[i+1][j], colors[i][j]
            answer = max(answer,check(N,colors))        
            colors[i][j], colors[i+1][j] = colors[i+1][j], colors[i][j]

print(answer)    
    