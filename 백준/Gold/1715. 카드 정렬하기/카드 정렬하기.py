import sys 
import heapq

input = sys.stdin.readline 

N = int(input())
hq = []
heapq.heapify(hq)
answer = 0 

for _ in range(N):
    heapq.heappush(hq,int(input()))
    
while(len(hq)>1):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    heapq.heappush(hq,a+b)
    answer += (a+b)
    
print(answer)   
    
    
    
'''

그리디 
'''