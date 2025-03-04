import sys 
from collections import deque 

leftq = deque(list(sys.stdin.readline().strip()))  
n = int(sys.stdin.readline())
rightq = deque()

for _ in range(n):
    temp = sys.stdin.readline().split()
    ctrl = temp[0]
    
    if ctrl == "L":
        if leftq:
            rightq.appendleft(leftq.pop())
    elif ctrl == "D":
        if rightq:
            leftq.append(rightq.popleft())
    elif ctrl == "B":
        if leftq:
            leftq.pop()
    else: 
        leftq.append(temp[1])

print("".join(leftq) + "".join(rightq))
