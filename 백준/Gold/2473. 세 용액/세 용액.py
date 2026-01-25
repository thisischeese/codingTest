import sys 

input = sys.stdin.readline 


def solution():
    target = 3*1e9
    a = 0 
    b = (N-1)//2
    c = N-1
    for i in range(N-2):
        start = i+1
        end = N-1
        while(start<end): 
            sum = arr[i]+arr[start] + arr[end]
            if(sum==0): return i,start,end
            if(target>=abs(sum)):
                target = abs(sum)
                a = i 
                b = start
                c = end 
            if(sum>=0):
                end -=1
            else:
                start +=1
    return a,b,c

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

a,b,c = solution() 

print(arr[a],arr[b],arr[c])
    
'''
3 포인터???
2포인터를 N번 돌림 
=> N<=5*10^3 ok 가능 
'''