import sys 

input = sys.stdin.readline 

N = int(input())
M = int(input())
S = input().rstrip() 

answer = 0 
cnt = 0 
i = 1 
while(i<M-1):
    if(S[i-1]=='I' and S[i]=='O' and S[i+1]=='I'):
        cnt += 1 
        if cnt>=N:
            answer += 1
        i+=2 
    else:
        cnt = 0 
        i+= 1
print(answer)

'''
어떻게 보면 DP 
누적된 IO 개수 기록하기 
'''