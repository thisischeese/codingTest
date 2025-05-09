import sys 

N = int(sys.stdin.readline())
arr = [list(map(str,sys.stdin.readline().split()))[1:] for _ in range(N)]
arr.sort()

def find_start(prev_arr,curr_arr):
    for i in range(min(len(prev_arr),len(curr_arr))):
        if prev_arr[i]!=curr_arr[i]:
            return i
    return min(len(prev_arr),len(curr_arr))
        

for i in range(N):
    if i>0 and arr[i][0] == arr[i-1][0]:
        start = find_start(arr[i-1],arr[i])
    else:
        start = 0 
    for j in range(start,len(arr[i])):
        print("--"*j + arr[i][j])
        