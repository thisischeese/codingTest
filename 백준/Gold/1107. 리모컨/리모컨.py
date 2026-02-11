import sys 

input = sys.stdin.readline

def check(num : str)->bool:
    for n in num:
        if(int(n) in arr): 
            return False
    return True 
        
def get_closest(num):

    snum = num 
    bnum = num 
    
    while(True):
        if(check(str(snum))):
            return snum 
        if(check(str(bnum))):
            return bnum 
        if(snum>0):
            snum -=1 
        bnum +=1 

    return num 
    
N = int(input())
M = int(input())
arr = list(map(int,input().split()))

if(N==100):
    print(0)
    sys.exit() 
elif(len(arr)==10): 
    print(abs(100-N))
    sys.exit()
    
closest = get_closest(N)
steps = abs(closest-N)
print(min(abs(100-N),steps+len(str(closest))))

'''

1. 숫자로만 갈 수 있는 가장 가까운 수 구하기 
    - 가까운 수는 더 클 수도 작을 수도 있음
    - 그러나 반드시 0 이상 && 5*1e5 이하여야 함 
    - 가장 큰 자릿수부터 훑으면서 정상인 수면 .join으로 붙여 버리기...? 
    - 가장 가까운 수는 반드시 N과 같은 자릿수일까? x 
2. + or - 버튼만을 사용해 N에 도달 가능한 차이 구하기 
3. 모두 더해서 출력 
채널은 무한대일 수 있다 
양방향으로 같은 depth로 수를 줄이거나 늘리다가 
하나 가장 가까운 거 나오면 종료하는 방향으로 가야 함 

분기 처리 주의해야 함 
1. 이미 현재 위치가 100이라서 더 이상 이동할 필요 없을 때  
2. 모든 숫자 버튼 사용 불가능할 때 
'''