import sys
from collections import deque

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

result = [-1] * N
stack = deque()

for i in range(N):
    while len(stack) and seq[stack[-1]] < seq[i]:
        temp = stack.pop()
        result[temp] = seq[i]
    
    stack.append(i)  

for item in result:
    print(item, end = ' ')
