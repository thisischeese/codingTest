from collections import deque 

def solution(s):
    answer,idx = len(s), 0
    comb = (("(",")"),("{","}"),("[","]"))
    stack = deque() 
    
    while(idx<len(s)):
        target = s[idx:]+s[:idx]
        for tar in target:
            if(len(stack) and (stack[-1],tar) in comb):
                stack.pop() 
            else:
                stack.append(tar)
        if(stack): 
            answer -= 1
        idx += 1
        stack.clear()
    
    return answer


"""

이거 완탐으로 구현해야 하는 것 말고는 별로 방법이 생각이 안나는데 

1. s를 왼쪽으로 x칸만큼 회전했다고 가정하고 인덱스 설정 (물론 진짜 회전시키면 시간복잡도 xxx) 
2. 여기에서 스택으로 괄호 구조 체크하는 로직 구현하는 것임 -> 만약 올바르지 못하면 answer -=1 
    a. 주어진 문자열을 왼쪽부터 차례로 보면서 넣기 전에 큐 empty 아니면 짝 맞는지 체크 
    b. 짝 아니라면 그리고 큐 empty였다면 스택에 하나씩 넣는다. 
    c. 만약 짝이 맞다면 스택에 있던 원소 pop시키기 
    .. 반복 
    d. 최종적으로 문자열 다 돌았는데 스택에 여전히 원소가 남아있다면 올바르지 못한 괄호 문자열인 것이다. 
    
"""