import math 
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

"""
최소공배수 : 대각선이 x와 y가 모두 정수인 좌표를 지나는 횟수 

"""