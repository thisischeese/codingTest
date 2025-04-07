import sys 

T = int(sys.stdin.readline())
for _ in range(T):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    planets = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    start =[]
    end = [] 
    
    for i in range(len(planets)):
        cx,cy,r = planets[i][0],planets[i][1],planets[i][2]
        # 출발점이 위치한 행성 idx 
        if (x1-cx)**2 + (y1-cy)**2 < r**2:
            start.append(i)
        # 도착점이 위치한 행성 idx 
        if (x2-cx)**2 + (y2-cy)**2 < r**2:
            end.append(i)            
    
    answer = list(set(start) ^ set(end))
    print(len(answer))
    
    
    