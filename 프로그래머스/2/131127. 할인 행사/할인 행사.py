from collections import Counter 

def solution(want, number, discount):
    jung = {w: n for w,n in zip(want,number)}
    comp = Counter(discount[:sum(number)])
    if jung==comp: 
        answer =1
    else: 
        answer =0
    for i in range(sum(number),len(discount)):  
        prev = i-sum(number)
        comp[discount[i]]+=1
        comp[discount[prev]] -=1
        for j in jung.keys():
            if jung[j]!=comp[j]:
                break 
        else:
            answer +=1               
    return answer