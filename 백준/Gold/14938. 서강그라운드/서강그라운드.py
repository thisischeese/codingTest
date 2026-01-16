import sys 
import heapq 

input = sys.stdin.readline 
INF = int(1e9)

def dijkstra(start):

    answer = 0
    distance = [INF]*(n+1)
    distance[start] = 0 

    queue = [] 
    heapq.heappush(queue, (0,start))

    while(queue): 
        curr = heapq.heappop(queue)

        for next in graph[curr[1]]: 
            next_node = next[0]
            next_cost = next[1]

            if(distance[next_node]<distance[curr[1]]+next_cost):
                continue 
            distance[next_node]=distance[curr[1]]+next_cost
            heapq.heappush(queue,(distance[curr[1]]+next_cost,next_node))

    for i in range(1,len(distance)):
        dist = distance[i]
        if(dist<=m): 
            answer += items[i]

    # print(answer)
    answers[start] = answer 

    return 



n,m,r = map(int,input().split())
items = [0]+list(map(int,input().split()))
answers = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(r): 
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

for start in range(1,n+1): 
    dijkstra(start)

print(max(answers))








'''
1. 특정 노드가 주어진다 
2. 방문 가능한 노드의 모든 아이템 sum 노드별로 기록 
    (해당 노드로부터 최단거리가 m 이하인 노드는 방문 가능)
3. 노드별 기록 중 최고 기록 출력 


# 무방향 가중치 있는 간선 그래프 
# 시작 노드 고정 -> 각 노드별 최단 거리 구하기 : 다익스트라 
# O(ElogV) : 2*10**4<10**8 

# n별로 시작 노드 설정 
    # 시작 노드별로 다익스트라로 최단 거리 구하기 
    # dist 리스트 돌며 조건 만족할 경우 아이템 개수 더하기 
    # 아이템 개수 answers 리스트에 기록하기 
# answers 리스트에서 가장 큰 수 출력하기  
'''

