import sys 

M = int(sys.stdin.readline())
S=set()

for _ in range(M):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp)==1:
        op = temp[0]
        if op == "all":    
            S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        elif op == "empty":
            S = set()    
    else:
        op,num = temp[0],temp[1]
        num = int(num)
        if op == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif op == "add":
            S.add(num)
        elif op == "remove":
            S.discard(num)
        elif op == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)

        
        