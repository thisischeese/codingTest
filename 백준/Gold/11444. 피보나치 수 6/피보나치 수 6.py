import sys 
MOD = 1_000_000_007
input = sys.stdin.readline

def mul(arra,arrb): 
    a1,a2,a3,a4 = arra[0],arra[1],arra[2],arra[3]
    b1,b2,b3,b4 = arrb[0],arrb[1],arrb[2],arrb[3]

    return [(a1*b1+a2*b3)%MOD,(a1*b2+a2*b4)%MOD,(a3*b1+a4*b3)%MOD,(a3*b2+a4*b4)%MOD]

def fib(n): 
    if(n==1):
        return [1,1,1,0]
    
    if(n%2==0):
        temp = fib(n//2)
        return mul(temp,temp)
    else: 
        return mul([1,1,1,0],fib(n-1))

n = int(input())
# n은 1,000,000,000,000,000,000보다 작거나 같은 자연수 -> n=0에 대한 예외처리 필요 x 
arr = fib(n)
print(arr[1])