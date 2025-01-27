import sys 

A,B,C = map(int,sys.stdin.readline().split())
D = int(sys.stdin.readline())

# 시간 단위 변화가 있을 경우 
a = D//3600
b = (D%3600)//60
c = D%60

if C+c>=60:
    C=(C+c)%60
    b+=1
else:
    C+=c

if B+b>=60:
    B=(B+b)%60
    a+=1
else:
    B+=b
    
if A+a>=24:
    A=(A+a)%24
else:
    A+=a


print(A,B,C)
