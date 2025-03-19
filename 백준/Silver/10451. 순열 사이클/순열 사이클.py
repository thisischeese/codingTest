import sys
sys.setrecursionlimit(2000)  

def dfs(node, seq_dict, visited):
    visited[node] = True
    next_node = seq_dict[node]
    
    if not visited[next_node]:
        dfs(next_node, seq_dict, visited)

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    seq_arr = list(map(int, sys.stdin.readline().split()))
    
    seq_dict = {} 
    for idx in range(1, N + 1):
        seq_dict[idx] = seq_arr[idx - 1]

    visited = [False] * (N + 1)
    answer = 0

    for node in range(1, N + 1):
        if not visited[node]:  
            answer += 1
            dfs(node, seq_dict, visited)

    print(answer)
