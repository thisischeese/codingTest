import sys 

N = int(sys.stdin.readline())

for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    if i ==0:
        dp_max = [temp[0],temp[1],temp[2]]
        dp_min = [temp[0],temp[1],temp[2]]
    else:
        prev0,prev1,prev2 = dp_max[0],dp_max[1],dp_max[2]
        dp_max[0] = max(prev0,prev1)+temp[0]
        dp_max[1] = max(max(prev0,prev1),prev2)+temp[1]
        dp_max[2] = max(prev1,prev2)+temp[2]
        
        prev0,prev1,prev2 = dp_min[0],dp_min[1],dp_min[2]
        dp_min[0] = min(prev0,prev1)+temp[0]
        dp_min[1] = min(min(prev0,prev1),prev2)+temp[1]
        dp_min[2] = min(prev1,prev2)+temp[2]

print(max(dp_max),min(dp_min))


