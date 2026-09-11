def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    for i in range(len(numbers)-1,-1,-1):
        while(stack and stack[-1]<=numbers[i]):
            stack.pop() 
        if stack:
            answer[i]=stack[-1]
        # 현재 자기 자신보다 큰 수만 스택에 역순으로 남기기 
        stack.append(numbers[i])
    
    return answer

"""
생각해보니까 무조건 마지막 원소의 뒷큰수는 -1인데 
그러면 이거 어떻게 보면 앞에서부터 찾는 것보다 
뒤에서부터 찾으면 한 번만 봐도 되는 것 

그리고 numbers가 1e6이라서 무조건 한 번만 탐색해야 함

처음에는 그 스택에 건물 높이 넣는 건물 문제 떠올랐음..
어떻게 보면 Least 
"""
  