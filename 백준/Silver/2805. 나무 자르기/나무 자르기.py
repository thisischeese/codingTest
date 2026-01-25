import sys 

input = sys.stdin.readline 

def cal(tar):
    total = 0 
    for height in arr:
        temp = height - tar 
        if(temp>0): total += temp 
    return total 

N,M = map(int,input().split())
arr = list(map(int,input().split()))

start = 1
end = max(arr)

while(start<=end):
    mid = (start+end)//2
    total = cal(mid)
    if(total>=M): 
        start = mid+1 
    else:
        end = mid-1  
print(end)
'''
이분탐색으로 적당한 길이 찾기 -> log2_10^9
절단 높이 주어졌을 때 가져갈 수 있는 나무 계산하는 값 -> 10^6

10^6 *9* log2_10 < 10^8 
'''
