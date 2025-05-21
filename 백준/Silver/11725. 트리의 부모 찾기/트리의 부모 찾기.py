import sys 
sys.setrecursionlimit(10**6)


def DFS(curr_idx):
    global N,arr,visited,parents 
    flag = False 
    for next_idx in arr[curr_idx]:
        if visited[next_idx] == False:
            parents[next_idx] = curr_idx
            visited[next_idx] = True 
            flag = True 
            DFS(next_idx)
    if flag == False:
        return 
            
        
N = int(sys.stdin.readline())
# 0번째 노드는 무시 
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    v1,v2 = map(int,sys.stdin.readline().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
parents = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

visited[1] = True 
DFS(1)
for i in range(2,N+1):
    print(parents[i])