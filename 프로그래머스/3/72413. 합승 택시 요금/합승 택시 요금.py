import heapq

def solution(n, s, a, b, fares):
    INF = float("inf")
    answer = INF
    
    adj = [[] for _ in range(n+1)]
    
    for c,d,f in fares:
        adj[c].append((d,f))
        adj[d].append((c,f))    
    
    def dijkstra(start):
        
        dist = [INF for _ in range(n+1)] 
        dist[start] = 0 
        
        hq = [(0,start)]
        heapq.heapify(hq) 
        
        while(hq):
            curr_dist,curr_idx = heapq.heappop(hq) 
            
            for next_idx,cost in adj[curr_idx]:
                temp = curr_dist + cost 
                if dist[next_idx]>temp:
                    dist[next_idx]=temp 
                    heapq.heappush(hq,(temp,next_idx))

        return dist

    dist = dijkstra(s)  
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    
    for i in range(1,n+1):
        if(dist[i]==INF):
            continue 
        total = dist[i]
        total+=(dist_a[i]+dist_b[i])
        answer=min(answer,total)

    return answer


"""
양방향 사이클 있는 그래프에서 최단거리 구하기 -> 간선별 cost 다르니까 다익스트라 사용하기  

다익스트라 수도코드 
1. dist 배열과 우선순위 힙 큐 정의 
2. 시작하는 노드 기준으로 dist 배열과 힙 큐 초기화 
3. 인접 노드 방문해서 예상 이동 값 계산해본다. 
3.1 만약 예상 이동값이 dist 배열 값보다 작으면 dist 업데이트하고 힙 큐에 다음 노드 넣기 
3.2 만약 크거나 같으면 pass 하기 
4. 힙 큐에 더 이상 노드 없으면 종료 

결정해야 하는 것  
같이 탈지 안탈지 
s에서 어디까지 같이 탈지 

1. answer=INF, s에서 각 노드별 최단거리 미리 구해두고 distance에 저장  
2. s를 제외한 노드 i까지 같이 탄다고 가정하고 total = distance[i] 초기화 
2.1. total += (i노드에서 a노드까지 가는 최단거리 + i노드에서 b노드까지 가는 최단거리)
2.2. answer = min(total,answer)
"""