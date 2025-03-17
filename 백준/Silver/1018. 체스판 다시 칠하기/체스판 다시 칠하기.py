import sys 
case=[]
jboard=[]
N,M=map(int,sys.stdin.readline().split())
for i in range(N):
    jboard.append(list(map(str,sys.stdin.readline().strip())))
    
for i in range(0,N-7,1):
    for j in range(0,M-7,1):
        cnt1,cnt2=0,0
        for n in range(i,i+8):
            for m in range(j,j+8):
                if((n%2==0 and m%2==0)or(n%2!=0 and m%2!=0)):
                    if(jboard[n][m]!="W"):
                        cnt1+=1
                    else:
                        cnt2+=1
                else:
                    if(jboard[n][m]!="B"):
                        cnt1+=1
                    else:
                        cnt2+=1
        case.append(cnt1)
        case.append(cnt2)
        
print(min(case))          