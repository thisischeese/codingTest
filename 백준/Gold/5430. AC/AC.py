import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()[1:-1].split(",")

    if n == 0:
        arr = deque()
    else:
        arr = deque(arr)

    reverse_flag = False
    error_flag = False

    for cmd in p:
        if cmd == 'R':
            reverse_flag = not reverse_flag  
        elif cmd == 'D':
            if arr:
                if reverse_flag:
                    arr.pop() 
                else:
                    arr.popleft() 
            else:
                print("error")
                error_flag = True
                break

    if not error_flag:
        if reverse_flag:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
