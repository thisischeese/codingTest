import sys

N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

def cal(N, S, seq):
    left = 0
    total = 0
    answer = N + 1 

    for right in range(N):
        total += seq[right]
        while total >= S:
            answer = min(answer, right - left + 1)
            total -= seq[left]
            left += 1
            
    if answer!=N+1:
        return answer 
    else:
        return 0 

print(cal(N, S, seq))
