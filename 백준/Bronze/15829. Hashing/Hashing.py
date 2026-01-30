import sys 

R = 31
MOD = 1234567891
 
input = sys.stdin.readline 

def hash(mystr):
    answer = 0 
    for i in range(len(mystr)):
        answer += (ord(mystr[i])-ord('a')+1)*pow(R,i,MOD)
    return answer%MOD


L = int(input())
mystr = input().strip()
print(hash(mystr))
