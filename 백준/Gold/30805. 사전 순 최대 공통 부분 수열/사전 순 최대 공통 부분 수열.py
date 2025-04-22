import sys
sys.setrecursionlimit(10**6)

def find(A,B,answer):
    #print("find ",A,B,answer)
    if len(A) == 0 or len(B) == 0:
        return answer
    a_max,b_max = max(A),max(B)
    a_idx,b_idx = A.index(a_max), B.index(b_max)
    if a_max == b_max:
        answer.append(a_max)
        return find(A[a_idx+1:],B[b_idx+1:],answer)
    elif a_max > b_max:
        A.pop(a_idx)
        return find(A,B,answer)
    else:
        B.pop(b_idx)
        return find(A,B,answer)


        


N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
B = list(map(int,sys.stdin.readline().split()))

temp = find(A,B,[])
if temp:
    print(len(temp))
    for t in temp:
        print(t,end=' ')
else:
    print(0)

