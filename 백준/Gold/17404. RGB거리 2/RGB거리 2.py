import sys 

input = sys.stdin.readline 
INF = int(1e9)

def solution(start):
    # dp 배열 초기화 
    dp = [[INF,INF,INF] for _ in range(N)]
    dp[0][start] = graph[0][start]

    for i in range(1,N-1):
        for color in range(3):
            for j in range(3):
                if color==j: continue 
                dp[i][color] = min(dp[i][color],dp[i-1][j]+graph[i][color])
    
    for i in range(3): 
        if i==start: continue 
        for j in range(3): 
            if i==j: continue 
            dp[-1][i] = min(dp[-1][i],dp[-2][j]+graph[-1][i])  
    
    return min(dp[-1])

N = int(input())
graph = [] 

for i in range(N): 
    graph.append(list(map(int,input().split())))

print(min(min(solution(0),solution(1)),solution(2)))




# 1번 집과 N번 집의 색이 겹치지 않게 구현할 방법? 
# 모든 경로 기록 -> 0.5초 시간 제한 있어서 시간 초과 
# 시작점을 고정하기(R,G,B별로 로직 돌리기) -> 종료점을 제한할 수 있음 
# 시작점이 고정될 때의 DP 배열을 어떻게 구현해야 하는가??? 
# 시작점으로 잡지 않을 부분을 절대 접근하지 못하도록 구현하면 됨 
# 현재 접근 기준은? 작은 값 -> 매우 큰 값을 부여하면 접근 x 