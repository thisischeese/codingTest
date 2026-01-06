import sys 
import collections 

input = sys.stdin.readline 

queue = collections.deque() 

cnt = int(input())
for _ in range(cnt):
    cmd = input().strip()  
    if cmd[:4]=="push": 
        num = int(cmd[5:])
        queue.append(num)
    elif(cmd=="pop"):
        if(len(queue)==0): 
            print(-1)
        else : 
            p = queue.popleft() 
            print(p)
    elif (cmd=="size"):
        print(len(queue))
    elif(cmd=="front"):
        p = -1 if len(queue)==0 else queue[0]
        print(p)
    elif(cmd=="back"):
        p = -1 if len(queue)==0 else queue[-1]
        print(p)     
    else:
        print(0) if len(queue) else print(1)   
