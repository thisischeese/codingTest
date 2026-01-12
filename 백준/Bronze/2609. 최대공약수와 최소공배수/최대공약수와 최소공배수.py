import sys

input = sys.stdin.readline

# 최대공약수 
def gcd(a,b):
    while(b>0):
        a,b = b,a%b
    return a 

# 최소공배수 
def lcm(a,b): 
    return (a*b)//gcd(a,b)

a,b = map(int,input().split())

print(gcd(a,b))
print(lcm(a,b))

# 유클리드 호제법 
# a%b=r 일 때 a와 b의 최대공약수 == b와 r의 최대공약수 
