import sys 

input = sys.stdin.readline 

def ccw(v1,v2,v3):
    p = v1[0]*v2[1] + v2[0]*v3[1] + v3[0]*v1[1]
    c = v1[1]*v2[0] + v2[1]*v3[0] + v3[1]*v1[0]
    return p-c

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

p1, p2 = (x1, y1), (x2, y2)
p3, p4 = (x3, y3), (x4, y4)

res1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
res2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if res1 <= 0 and res2 <= 0:
    if res1 == 0 and res2 == 0:
        if max(p1[0], p2[0]) >= min(p3[0], p4[0]) and \
           max(p3[0], p4[0]) >= min(p1[0], p2[0]) and \
           max(p1[1], p2[1]) >= min(p3[1], p4[1]) and \
           max(p3[1], p4[1]) >= min(p1[1], p2[1]):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
    

'''
CCW(Counter Clock Wise) 알고리즘 : 3점의 방향성 

직선이 아니라 선분임에 주의 -> 단순 기울기로는 알 수 x 

두 선분 교차하는 경우 : 1개의 교점 or 기울기 같아서 일부 겹침 
-> 1개의 교점 : 한 선분 끝나는 점에서 다른 선분 끝나는 2 지점까지 가는 방향 다름 
=> 1번점-2번점 선분 & 3번점-4번점 선분 주어질 때 
    v(1,3), v(1,4) 외적 V.S. v(2,3), v(2,4) 외적 비교 
    1. 둘 다 0 -> 기울기 동일 겹침
    2. 둘 다 0 x && 값의 곱이 음수 -> 기울기 다르고 교점 only 1 


'''