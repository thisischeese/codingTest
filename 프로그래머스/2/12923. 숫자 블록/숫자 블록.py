import math 
MAX = 10_000_000
def solution(begin, end):
    answer = [1 for _ in range(end-begin+1)]
    if(begin==1): 
        answer[0] = 0 
        
    for num in range(begin, end+1):
        for div in range(2,math.ceil(math.sqrt(num))+1):
            if(num%div==0):
                if(num//div<=MAX):
                    answer[num-begin] = num//div
                    break 
                else:
                    answer[num-begin] = max(answer[num-begin],div)
    return answer