def solution(arr):
    
    arr.sort()
    answer = arr[0]

    def gcd(a,b):
        while a!=0:
            a,b = b%a, a
        return b
    
    def lcm(a,b):
        return a*b//gcd(a,b)
    
    for i in range(1,len(arr)):
        answer = lcm(answer,arr[i])

    return answer

"""
모든 수들에 대한 최소공배수를 구하기
1. 오름차순으로 나열하기 
2. 앞에서부터 2개씩 묶으면서 최소공배수 구하고 넘어가기 
"""
