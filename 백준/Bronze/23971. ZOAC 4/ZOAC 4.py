import sys 
import math

H,W,N,M = map(int,sys.stdin.readline().split())
print(math.ceil(W/(M+1))*math.ceil(H/(N+1)))

