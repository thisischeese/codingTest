import sys 

def find_bound(arr, tar,lower=True):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if lower == True and arr[mid] < tar:
            left = mid + 1
        elif lower == False and arr[mid] <= tar:
            left = mid + 1
        else:
            right = mid
    return left

N, M = map(int,sys.stdin.readline().split())
dots = sorted(map(int,sys.stdin.readline().split()))
lines = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

for start,end in lines:
    start_idx= find_bound(dots,start,lower=True)
    end_idx= find_bound(dots,end,lower=False)
    print(end_idx - start_idx)
    
    
    