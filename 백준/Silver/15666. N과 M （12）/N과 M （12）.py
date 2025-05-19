import sys 
sys.setrecursionlimit(10000)

def DFS(idx,seq):
    global arr,M
    
    if len(seq) == M:
        print(' '.join(map(str,seq)))
        return 
        
    for i in range(idx,len(arr)):
        seq.append(arr[i])
        DFS(i,seq[:])
        seq.pop()
      

N,M = map(int,sys.stdin.readline().split())
arr = list(set(list(map(int,sys.stdin.readline().split()))))
arr.sort()
DFS(0,[])


