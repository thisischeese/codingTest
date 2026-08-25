def solution(words):
    words = list(words)
    stack = []
    for word in words:
        if(len(stack) and stack[-1]==word):
            stack.pop()
        else:
            stack.append(word)
    return 0 if len(stack) else 1

"""
1. 문자열을 문자 단위로 split시켜 순회할 수 있는 자료구조로 변형시키기 
2. 문자가 저장된 자료구조를 처음부터 순회하며 하나의 문자열 빼기  
3. 스택에 문자열을 넣기 
    3.1 만약에 스택이 비었다. -> 그냥 넣는다. 
    3.2 만약 스택에 문자가 존재한다. 
        3.2.1 만약 맨 위가 동일한 문자일 경우 맨 위를 빼고 자신도 넣지 않기
        3.2.2 만약 맨 위가 동일하지 않으면 그냥 넣는다. 
4. 다 돌았는데 스택에 아직도 문자가 남아있다면 실패 
"""