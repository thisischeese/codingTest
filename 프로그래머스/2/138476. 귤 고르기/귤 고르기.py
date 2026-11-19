from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnts = sorted(Counter(tangerine).values(), reverse=True)
    
    for cnt in cnts:
        k -= cnt
        answer += 1
        if k <= 0:
            break
            
    return answer
