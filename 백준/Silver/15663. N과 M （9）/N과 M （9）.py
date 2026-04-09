import sys 

input = sys.stdin.readline 

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr=sorted(arr)
visited = [False]*N


def bt(cnt,seq):
    if cnt==M:
        print(*seq)
        return 
    last = 0 
    for idx in range(N):
        if not visited[idx] and last!=arr[idx]:
            visited[idx] = True
            last = arr[idx]
            bt(cnt+1,seq+[arr[idx]])
            visited[idx] = False 

bt(0,[])
