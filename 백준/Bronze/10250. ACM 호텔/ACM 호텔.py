import sys 

input = sys.stdin.readline 


t = int(input().strip())
arr = ['0000' for _ in range(t)]

for i in range(t):
    h,w,n = map(int,input().split())
    # th 
    th = n%h
    if th==0: th = h 
    # n = (tw-1)*h + th 
    # tw = (n-th)//h +1
    tw = (n-th)//h +1

    arr[i] = str(th) + format(tw,'02')


for a in arr:
    print(a)
'''
조건
걷는 거리 = XX  
1. a.XX == b.XX -> min(a,b)
2. a.XX > b.XX -> b 

input -> output 
h,w,n -> 방 번호 

예시 
6, 12, 13 -> 103 
13(n)%6(h) -> 층 
13(n)//6(h)+1 -> 방 

예시 
6, 12, 3 -> 301 
3%6 -> 3 
3//6 +1 -> 1

풀이 
n = (tw-1)*h + th 
'''