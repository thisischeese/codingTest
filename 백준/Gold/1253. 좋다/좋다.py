import sys 

input = sys.stdin.readline 

def bs(i):
    target = arr[i]
    start = 0 if i!=0 else 1
    end = N-1 if i!=N-1 else N-2
    while(start<end):
        temp = arr[start]+arr[end]
        if(target>temp):
            if(start+1!=i):
                start += 1 
            else: 
                start += 2 
        elif(target<temp):
            if(end-1!=i):
                end -= 1
            else:
                end -= 2
        else:
            return True 

    return False


answer = 0 

N = int(input())
arr = list(map(int,input().split()))
arr.sort() 

for i in range(N): 
    if(bs(i)):
        answer +=1 

print(answer)
'''
N<=2*10^3 

A는 음의 정수 or 양의 정수인데 두 수의 합으로 나타낼 수 있다? 
-> 전 범위 탐색해야 함 => 8*10^9 > 2*10^8
원소마다 이분탐
-> (2*10^3)^2*log(2*10^3) = 24*10^6*log2 = 24log2 * 10^6 <2*10^8
'''