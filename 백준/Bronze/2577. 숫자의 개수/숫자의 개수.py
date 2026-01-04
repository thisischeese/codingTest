import sys 

input = sys.stdin.readline 

a = int(input()) 
b = int(input())
c = int(input())
mul = str(a*b*c)
for i in range(0,10,1):
    temp = 0 
    for m in mul:
        if m==str(i):
            temp+=1 
    print(temp)
            
    