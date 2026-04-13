import sys 
from collections import deque 

input = sys.stdin.readline 

N,K = map(int,input().split())

def find(curr):
    answers = [0]*100001
    answers[curr] = 1
    
    visited = [-1]*100001
    visited[curr] = 0 
    
    queue = deque()
    queue.append((curr,0)) 
    
    while(queue):
        curr,time = queue.popleft() 
        
        for next in (curr*2,curr-1,curr+1):
            if(0<=next<=100000 and (visited[next]==-1 or visited[next]==time+1)):
                queue.append((next,time+1))
                visited[next] = time+1 
                answers[next] +=1 
                
    return visited[K], answers[K]
                
time,methods = find(N)
print(time)
print(methods)
'''
같은 depth에서 탐색하면 됨 
'''