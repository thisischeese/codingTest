import sys 
import heapq

input = sys.stdin.readline
heap = []
heapq.heapify(heap)

N = int(input())
for _ in range(N):
    x = int(input())
    if x!=0:
        heapq.heappush(heap,(abs(x),x//abs(x)))
    else:
        if len(heap)!=0:
            temp = heapq.heappop(heap)
            print(temp[0]*temp[1])
        else:
            print(0)
    