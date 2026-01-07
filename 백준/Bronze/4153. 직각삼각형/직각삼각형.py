import sys 


lines = sys.stdin.readlines() 
for line in lines:

    total = 0 
    arr = list(map(int,line.split()))
    max_val = max(arr)
    
    if(max_val==0): break
    for a in arr:
        total += a*a 
        
    if(2*max_val*max_val==total):
        print("right")
    else:
        print("wrong")