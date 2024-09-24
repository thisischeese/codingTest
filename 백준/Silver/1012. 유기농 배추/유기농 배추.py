import sys
sys.setrecursionlimit(10000)

# 상, 하, 좌, 우 네 방향을 나타냄
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# DFS로 인접한 배추들을 모두 탐색
def dfs(x, y, farm, visited, M, N):
    visited[y][x] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 농장 내에 있고, 배추가 있으며, 방문하지 않은 곳이면 DFS 재귀 호출
        if 0 <= nx < M and 0 <= ny < N and farm[ny][nx] == 1 and not visited[ny][nx]:
            dfs(nx, ny, farm, visited, M, N)

# 테스트 케이스 입력
T = int(input())
for _ in range(T):
    # M: 가로, N: 세로, K: 배추 위치 개수
    M, N, K = map(int, input().split())
    
    # 농장과 방문 여부를 저장할 리스트
    farm = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    # 배추 위치 입력
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1  # 배추가 심어진 곳을 1로 표시
    
    # 필요한 지렁이 수
    worm_count = 0
    
    # 농장을 순회하며 DFS 실행
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and not visited[i][j]:
                dfs(j, i, farm, visited, M, N)
                worm_count += 1  # 새로운 컴포넌트가 발견될 때마다 지렁이 한 마리 추가
    
    # 결과 출력
    print(worm_count)
