import sys

def make_prime(N):
    arr = [False,False]+[True for _ in range(2, N+1)]
    primes = []
    
    for i in range(2,N+1):
        if arr[i] == True:
            for j in range(2*i,N+1,i):
                arr[j] = False
    for i in range(len(arr)):
        if arr[i] == True:
            primes.append(i)
        
    return primes


def solution(N):
    if N ==1:
        return 0 
        
    answer = 0 
    total = 0 
    start,end = 0,0
    
    primes = make_prime(N)
    
    while True:
        if total >= N:
            total -= primes[start]
            start += 1
        elif end == len(primes):
            break
        else:
            total += primes[end]
            end += 1

        if total == N:
            answer += 1

    return answer
  
        


N = int(sys.stdin.readline())
print(solution(N))