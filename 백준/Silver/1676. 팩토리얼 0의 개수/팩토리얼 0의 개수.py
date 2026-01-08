import sys 

input = sys.stdin.readline 

def factorial(n:int) -> int:
    if (n>1):
        return n*factorial(n-1)
    else: 
        return 1



ans = 0 
n = int(input())
tar = reversed(list(str(factorial(n))))

for t in tar:
    if (t!='0'):
        break
    ans +=1 
print(ans)

