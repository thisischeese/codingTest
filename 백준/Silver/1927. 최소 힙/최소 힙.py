import sys 
import heapq 

heap = []
heapq.heapify(heap)

input = sys.stdin.readline 

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) ==0:
            print(0)
        else:
            temp = heapq.heappop(heap)
            print(temp)
    else:
        heapq.heappush(heap,x)

        