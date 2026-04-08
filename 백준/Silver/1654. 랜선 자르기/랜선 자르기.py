import sys 

input = sys.stdin.readline 

K,N = map(int,input().split())
arr = [int(input()) for _ in range(K)]

start = 1
end = max(arr)

while(start<=end):
    cnt = 0 
    mid = (start+end)//2
    for a in arr:
        cnt += a//mid
    
    if(cnt<N):
        end = mid-1
    else:
        start = mid+1
    
print(end)

