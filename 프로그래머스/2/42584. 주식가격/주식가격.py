def solution(prices):

    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        tar = prices[i]
        for j in range(i+1,len(prices)):
            answer[i]+=1
            if tar>prices[j]:
                break
    return answer

"""

"""