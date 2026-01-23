import sys 

input = sys.stdin.readline 

answer = 0 
N = int(input())
arr = []
for _ in range(N): 
    x,y = map(int,input().split())
    arr.append([x,y])

for i in range(N-1):
    answer += (arr[i][0]*arr[i+1][1]-arr[i][1]*arr[i+1][0])

print(abs(round(0.5*(answer+arr[-1][0]*arr[0][1]-arr[-1][1]*arr[0][0]),1)))
    

'''
신발끈 공식 
'''