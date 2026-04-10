import sys 

input = sys.stdin.readline 

N = int(input())
arr = list(map(int,input().split()))
seq = [] 

for i in range(N):
    if(len(seq)==0 or seq[-1]<arr[i]):
        seq.append(arr[i])
        continue 
    # lower bound 찾기 
    last_idx = len(seq)-1
    while(-1<=last_idx):
        if(last_idx==-1 or seq[last_idx]<arr[i]):
            seq[last_idx+1] = arr[i]
            break 
        else:
            last_idx -= 1 
    

print(len(seq))
'''

3
3 2 3

3
2
2 3 

'''