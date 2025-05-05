import sys 
stack =[]
mystr = sys.stdin.readline().strip()
target =sys.stdin.readline().strip()
for i in range(0,len(mystr)):
    stack.append(mystr[i])
    if len(stack)<len(target):
        continue 
    else:
        if stack[-len(target):]==list(target):
            del stack[-len(target):]

if len(stack)==0:
    print("FRULA",end='')
else:
    print(''.join(s for s in stack),end='')            
            
