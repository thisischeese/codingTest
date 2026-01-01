import sys 
import math 

arr  = sys.stdin.readline().split()
num = 0 
for a in arr:
    num += int(a)*int(a)
print(num%10)    