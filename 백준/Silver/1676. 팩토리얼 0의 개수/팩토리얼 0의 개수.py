import sys 
import math 

input = sys.stdin.readline 

def factorial(n:int) -> int:
    if (n>1):
        return n*factorial(n-1)
    else: 
        return 1


'''
ans = 0 
n = int(input())
tar = reversed(list(str(factorial(n))))

for t in tar:
    if (t!='0'):
        break
    ans +=1 
print(ans)

'''

def cnt_zeros(n:int)-> int : 
    cnt = 0
    power = 1  
    while(math.pow(5,power)<=n):
        cnt += n//int(math.pow(5,power))
        power += 1 
    return cnt 


n = int(input())
'''# test
print(factorial(n))'''
print(cnt_zeros(n))