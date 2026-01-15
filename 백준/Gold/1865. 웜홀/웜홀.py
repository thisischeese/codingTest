import sys 
input = sys.stdin.readline 
INF = int(1e9)

def bf(V,E):
    distance = [INF]*(V+1)
    distance[1] = 0 

    for i in range(V): 
        for j in range(E):
            curr_node = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]

            if(distance[next_node]>distance[curr_node]+cost):
                distance[next_node] = distance[curr_node]+cost

                if(i==V-1): 
                    return True 
    return False  


TC = int(input())

for tc in range(TC):
    N,M,W = map(int,input().split())
    graph = []

    # 양의 간선 입력 
    for _ in range(M): 
        s,e,t = map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))


    # 음의 간선 입력 
    for _ in range(W): 
        s,e,t = map(int,input().split())
        graph.append((s,e,-t))

    if bf(N,2*M+W):
        print("YES")
    else:
        print("NO")




# 도로 -> 이동 후 시간 늘어남 : 양의 cost 
# 웜홀 -> 이동 후 시간 뒤로 줄어듬 : 음의 cost 
# 알고리즘 : 벨만 포드 
# 그래프 내 음의 사이클이 존재하는가? 를 체크하는 문제 
# 주의할 점 
# 도로는 방향이 없으나.. 웜홀은 방향이 있다..!!!!!!!!!!!!!


