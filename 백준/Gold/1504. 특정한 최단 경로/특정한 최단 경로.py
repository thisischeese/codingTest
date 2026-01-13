import sys 
import heapq

input = sys.stdin.readline
INF = 1e9 

def solution(s,m1,m2,e):
    mid_cost = dijkstra(m1,m2) 
    if(mid_cost==-1): return -1

    sm1_cost = dijkstra(s,m1)
    m2e_cost = dijkstra(m2,e) 

    if(sm1_cost!=-1 and m2e_cost!=-1):
        return sm1_cost + mid_cost + m2e_cost 

    return -1 

def dijkstra(start,end): 
    queue = [] 
    distance = [INF]*(N+1)
    heapq.heappush(queue,(0,start))
    distance[start] = 0 

    while(queue):
        curr_dist,curr_node = heapq.heappop(queue)
        if distance[curr_node] < curr_dist:
            continue 
        for next in arr[curr_node]: 
            next_dist = curr_dist + next[1]
            if(next_dist<distance[next[0]]):
                distance[next[0]] = next_dist 
                heapq.heappush(queue,(next_dist,next[0]))
                
    if(distance[end]!=INF): return distance[end]
    else: return -1 



N, E = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

v1,v2 = map(int,input().split())


s1 = solution(1,v1,v2,N)
s2 = solution(1,v2,v1,N)

if(min(s1,s2)!=-1):print(min(s1,s2))
else: print(-1)




# 2*10^5
