import sys

N, X = map(int,sys.stdin.readline().split())
visitors = list(map(int,sys.stdin.readline().split()))

total = sum(visitors[:X])
max_num = total 
stack = [total]

for i in range(1,N-X+1):
    temp = total + visitors[X+i-1] - visitors[i-1]
    total = temp
    if max_num < temp:
        max_num = temp
        stack = [temp]
    elif max_num == temp:
        stack.append(temp)
    
if stack[0]!=0:
    print(stack[0],len(stack),sep='\n')
else:
    print("SAD")
    