import math
def solution(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n-1)%i==0: return i
    return n-1

'''
사실 (n-1)의 약수 중 1보다 큰 것 찾기  
'''