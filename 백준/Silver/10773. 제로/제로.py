import sys
from collections import deque 

K = int(sys.stdin.readline())
queue = deque()
answer=0

for _ in range(K):
    num = int(sys.stdin.readline())
    if num==0:
        queue.pop()
    else:
        queue.append(num)

for i in range(len(queue)):
    answer+=queue[i]
    
    
print(answer)
    
        
        