import sys 
from collections import OrderedDict

seq = OrderedDict()
cnt = 0 

K, L = map(int,sys.stdin.readline().split())
students = list(sys.stdin.readline().strip() for _ in range(L))

for id in students:
    if id in seq:
        del seq[id]
    seq[id] = True
    
for id in seq.keys():
    if cnt < K:
        print(id)
        cnt+=1
    else:
        break

