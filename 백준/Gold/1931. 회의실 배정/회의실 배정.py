import sys 

input = sys.stdin.readline 

n = int(input())
arr = []

ans = 1

for _ in range(n): 
    s,e = map(int,input().split())
    arr.append([s,e])

arr.sort(key = lambda x:(x[1],x[0]))

curr = arr[0][1]
for i in range(1,n):
    if(curr<=arr[i][0]):
        ans +=1 
        curr = arr[i][1]
        
print(ans)