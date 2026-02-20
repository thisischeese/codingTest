import sys 
from collections import deque 

INF = int(1e8)
input = sys.stdin.readline 

def ts():
    queue = deque() 
    for i in range(1,N+1):
        if(indegree[i]==0):
            queue.append(i)

    while(queue):
        curr = queue.popleft() 
        print(curr)
        for next in graph[curr]:
            indegree[next] -= 1
            if(indegree[next]==0):
                queue.append(next)

            
# 사이클 판별 
def dfs(curr):
    global flag 
    visited[curr] = True  
    recur[curr] = True 
    for next in graph[curr]:
        if not visited[next]:
            dfs(next)
        elif recur[next]:
            flag = True 
    recur[curr] = False

start = 1  

N,M = map(int,input().split())
graph = [set() for _ in range(N+1)]
indegree = [INF]+[0 for _ in range(1,N+1)]
seqs = [list(map(int,input().split()))[1:] for _ in range(M)]

for seq in seqs:
    for i in range(len(seq)-1):
        if(seq[i+1] not in graph[seq[i]]):
            graph[seq[i]].add(seq[i+1])
            indegree[seq[i+1]] += 1

for i in range(1,N+1):
    flag = False
    visited = [True]+[False for _ in range(1,N+1)]
    recur = [True]+[False for _ in range(1,N+1)]
    dfs(i) 
    if(flag):
        print(0)
        sys.exit()
       
ts() 
    



'''
순서를 정하는 것이 불가능한 경우 : 사이클이 발생하는 경우 

1. 그래프 입력 
2. 사이클 발생 탐색
3. 발생하지 않는다면 위상정렬 알고리즘 적용 

주의할 점 : PD들이 같은 순서를 들고 올 수 있다. 
-> 이미 존재하는 간선일수도 

방향그래프에서 사이클을 탐색해야 함.. 

'''