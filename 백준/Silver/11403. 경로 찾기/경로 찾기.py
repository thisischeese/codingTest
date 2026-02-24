import sys 
from collections import deque 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 


def solution():

    def BFS(N,start):

        visited = [False for _ in range(N)]
        visited[start] = True 
        
        queue = deque()
        queue.append((start,0))
    
        while(queue):
            curr_idx,curr_total = queue.popleft()
            
            for next_idx in adj[curr_idx]:
                if(curr_total+1>0):
                    answers[start][next_idx] = 1
                if(not visited[next_idx]):
                    queue.append((next_idx,curr_total+1))
                    visited[next_idx]=True 


    
    N = int(input())
    adj = [[] for _ in range(N)] 
    answers = [[0 for _ in range(N)] for _ in range(N)] 
    
    
    for i in range(N):
        temp = list(map(int,input().split()))
        for j in range(N): 
            if(temp[j]==1):
                adj[i].append(j)
    for i in range(N):
        BFS(N,i) 
    for answer in answers:
        print(*answer)

       
solution()      


'''
길이가 양수인 경로가 존재하는가? 
1->1 이 0이 아니라 양수인 경로가 존재하는가 

'''