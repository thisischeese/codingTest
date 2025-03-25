import sys 
import math 

s1,m1 = map(int,sys.stdin.readline().split())
s2,m2 = map(int,sys.stdin.readline().split())

answer = [s1*m2+s2*m1,m1*m2]

gcd = math.gcd(answer[0],answer[1])

print(answer[0]//gcd,answer[1]//gcd)
