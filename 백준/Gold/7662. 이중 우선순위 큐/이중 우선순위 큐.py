import sys 
import heapq 
input = sys.stdin.readline 
t = int(input()) 

for _ in range(t): 
    qmax = []
    qmin = []
    visited = [False] * 1000000
    idx = 0
    
    k = int(input())
    for _ in range(k):
        mystr, mynum = input().split()
        mynum = int(mynum)
        
        if mystr == "I":
            heapq.heappush(qmax, (-mynum, idx))
            heapq.heappush(qmin, (mynum, idx))
            visited[idx] = True
            idx += 1
            
        elif mystr == "D":
            if mynum == 1:
                while qmax and not visited[qmax[0][1]]:
                    heapq.heappop(qmax)
                if qmax:
                    visited[qmax[0][1]] = False
                    heapq.heappop(qmax)
            else:
                while qmin and not visited[qmin[0][1]]:
                    heapq.heappop(qmin)
                if qmin:
                    visited[qmin[0][1]] = False
                    heapq.heappop(qmin)
    
    while qmax and not visited[qmax[0][1]]:
        heapq.heappop(qmax)
    while qmin and not visited[qmin[0][1]]:
        heapq.heappop(qmin)
    
    if not qmax or not qmin:
        print("EMPTY")
    else: 
        print(-qmax[0][0], qmin[0][0])