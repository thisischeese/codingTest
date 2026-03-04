import sys 

input = sys.stdin.readline 

def move(dir,cr,cc):
    out = 0 
    total = 0 
    origin = graph[cr][cc]
    dir = dir%4
    
    # 10% 
    for i in range(dir,dir+2):
        nr = cr + ddr[i%4]
        nc = cc + ddc[i%4]
        total += int(origin*0.1)
        if(0<=nr<N and 0<=nc<N):
            graph[nr][nc] += int(origin*0.1)
        else: out += int(origin*0.1)

    # 1% 
    for i in range(dir+2,dir+4):
        nr = cr + ddr[i%4]
        nc = cc + ddc[i%4]
        total += int(origin*0.01)
        if(0<=nr<N and 0<=nc<N):
            graph[nr][nc] += int(origin*0.01)
        else: out += int(origin*0.01)

    # dir-1, dir +1
    for i in range(dir -1, dir +2,2):
        
        nr = cr + dr[i%4]
        nc = cc + dc[i%4]
        total += int(origin*0.07)
        if(0<=nr<N and 0<=nc<N):
            graph[nr][nc] += int(origin*0.07)
        else: out += int(origin*0.07)
            
        nr = cr + dr[i%4]*2
        nc = cc + dc[i%4]*2
        total += int(origin*0.02)
        if(0<=nr<N and 0<=nc<N):
            graph[nr][nc] += int(origin*0.02)
        else: out += int(origin*0.02)

    # dir 
    nr = cr + dr[dir%4]*2
    nc = cc + dc[dir%4]*2
    total += int(origin*0.05)
    if(0<=nr<N and 0<=nc<N):
        graph[nr][nc] += int(origin*0.05)
    else: out += int(origin*0.05)

    nr = cr + dr[dir%4]
    nc = cc + dc[dir%4]
    if(0<=nr<N and 0<=nc<N):
        graph[nr][nc] += origin - total
    else:
        out += origin-total

    graph[cr][cc] = 0


    return out 

# 좌 하 우 상 
dr = [0,1,0,-1]
dc = [-1,0,1,0]
# 
ddr = [-1,1,1,-1]
ddc = [-1,-1,1,1]

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dir = 0 
cr = N//2
cc = N//2
dist =1 
answer = 0 
while(True):
    for j in range(2):
        for _ in range(dist):    
            cr += dr[dir%4]
            cc += dc[dir%4]
            if(cr==0 and cc==0):
                answer += move(dir,cr,cc)
                print(answer)
                sys.exit() 
            answer += move(dir,cr,cc)
        dir += 1
    dist += 1

print(answer)

'''
반시계로 도는 중이니까 반시계 방향으로
dr, ddr 작성해줘야 함!!!
'''