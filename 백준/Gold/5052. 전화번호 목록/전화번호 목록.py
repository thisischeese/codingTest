import sys 

def check(arr,n):
    for i in range(n-1):
        curr_len = len(arr[i]) 
        temp = arr[i+1][:curr_len]
        if temp == arr[i]:
            return "NO"
    return "YES"

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [str(sys.stdin.readline().strip()) for _ in range(n)]
    arr.sort()
    answer = check(arr,n)
    print(answer)
            
        
        