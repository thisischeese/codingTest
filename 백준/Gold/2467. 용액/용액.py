import sys 

input = sys.stdin.readline 

N = int(input())
arr = list(map(int,input().split()))

target = 2*1e9
a = 0 
b = N-1

start = 0 
end = N-1

while(start<end): 

    sum = arr[start] + arr[end]
    if(target>=abs(sum)):
        target = abs(sum)
        a = start
        b = end 
    if(sum>=0):
        end -=1
    else:
        start +=1
        
print(arr[a],arr[b])
    
'''
1<=|산성 특성값| <=1e9 
1<=|알칼리성 특성값|<=1e9

arr에서 2개 원소 더해 0에 가장 가까워지는 순간 원소 2개 출력하기 

N<=1e6 => 이중 for문 돌릴 수는 x => 이진탐색 

'''