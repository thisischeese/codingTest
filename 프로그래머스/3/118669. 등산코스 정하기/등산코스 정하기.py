import heapq 

def solution(n, paths, gates, summits):
    answer = []
    summits = {s:True for s in summits}
    INF = float('inf')
    adj = [[] for _ in range(n+1)]
    
    for i,j,w in paths:
        adj[i].append((j,w))
        adj[j].append((i,w))
    
    def dijkstra(starts):
        intensity = [INF for _ in range(n+1)]
        hq = []
        heapq.heapify(hq)
        for start in starts:
            intensity[start] = 0
            heapq.heappush(hq,(0,start))       
        
        while(hq):
            curr_intensity, curr_node = heapq.heappop(hq) 
            if curr_intensity>intensity[curr_node]:
                continue 
            for next_node,next_cost in adj[curr_node]:
                temp = max(next_cost,curr_intensity)
                
                if(intensity[next_node]>temp):
                    intensity[next_node] = temp
                    if not summits.get(next_node,False):
                        heapq.heappush(hq,(temp,next_node))

        return intensity 
    
    dist = dijkstra(gates)

    answer = [] 
    
    for i in summits.keys():
        answer.append([i,dist[i]])
            
    answer.sort(key=lambda x: (x[1],x[0]))
    
    return answer[0]

"""
intensity가 최소인 등산코스가 대칭이어야 전체 등산에 대해 가장 작은 intensity를 도출할 수 있음
그러면 역으로 산봉우리에서 gates별 최소 intensity를 다익스트라로 구하면 됨. 
intensity는 가장 긴 cost 값인데 이걸 기준으로 힙 정렬

초기수도코드 -> 시간초과 산봉우리가 최대 n개라서 O((N+E)logN)
1. 산봉우리별로 다익스트라를 돌려서 dist 배열을 구한다. 
2. gates에 해당하는 값 중 가장 작은 값과 해당 산봉우리를 return 한다. 

시간초과 이후 수도코드 
어느 gate에서 출발하는지 알 필요가 없다 그냥 산봉우리까지의 최단거리만 알면 됨. 
1. gate 시작을 모두 힙에 넣는다. 
2. 다익스트라를 돌린다. 
3. intensity -> 산봉우리 idx 순으로 정렬해서 첫번째 출력
"""