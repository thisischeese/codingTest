import sys 

input = sys.stdin.readline 

N,M = map(int,input().split())

def bt(curr,cnt,seq):
    if cnt == M:
        print(*seq)
        return 
    for next in range(curr+1,N+1):
        bt(next,cnt+1,seq+[next])


bt(0,0,[])
    