import sys

input = sys.stdin.readlines

def check(num):
    for i in range(0,len(num)//2,1): 
        if(num[i]!=num[len(num)-i-1]):
            print("no")
            return 
    print("yes")
    return 

lines = input()
for line in lines[:-1]:
    check(str(int(line[:-1]))) 

# 10^5 