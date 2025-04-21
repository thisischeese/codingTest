import sys 

def check(target,curr):
    num = 0 
    while(True):
        if curr == target:
            num+=1
            break 
        elif (curr > target and curr%2==0):
            curr = curr//2
            num+=1
        elif (curr > target and curr %10 ==1):
            curr = curr//10
            num+=1
        else:
            num = -1 
            break 
    return num
    

A, B = map(int,sys.stdin.readline().split())

answer = check(A,B)
print(answer)
