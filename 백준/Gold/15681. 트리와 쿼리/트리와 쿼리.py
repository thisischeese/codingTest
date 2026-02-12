import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def solve():
    N, R, Q = map(int, input().split())
    
    # 인접 리스트 생성
    adj = [[] for _ in range(N + 1)]
    # 양방향 그래프 
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # 서브트리 크기를 저장할 배열 (1로 초기화: 자기 자신 포함)
    subtree_size = [1] * (N + 1)
    visited = [False] * (N + 1)

    def count_subtree(curr):
        visited[curr] = True
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                # 자식 노드의 서브트리 크기를 구해서 현재 노드에 더함
                subtree_size[curr] += count_subtree(neighbor)
        return subtree_size[curr]

    # 루트(R)부터 시작해서 단 한 번의 순회로 모든 결과 계산
    count_subtree(R)

    # 쿼리 처리
    results = []
    for _ in range(Q):
        sub_root = int(input())
        results.append(str(subtree_size[sub_root]))
    
    # 출력 최적화 (매번 print하는 것보다 한 번에 모아서 출력하는 것이 빠름)
    sys.stdout.write("\n".join(results) + "\n")

solve()