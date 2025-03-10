import sys

N = int(sys.stdin.readline().strip()) 
count = 0

def check(num):
    numarr = [int(d) for d in str(num)]
    
    if len(numarr) <= 2: 
        return True
    
    diff = numarr[1] - numarr[0] 
    
    for i in range(1, len(numarr) - 1):
        if numarr[i + 1] - numarr[i] != diff:
            return False
        
    return True

 
for i in range(1, N + 1): 
    if check(i):
        count += 1

print(count)
