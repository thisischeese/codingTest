answer = 0

def solution(numbers, target):
    global answer 
    DFS(0,0,numbers,target)
    return answer

def DFS(idx,total,numbers,target):
    global answer
    if idx==len(numbers):
        if total == target:
            answer +=1 
        return 
    else:
        return DFS(idx+1,total+numbers[idx],numbers,target), DFS(idx+1,total-numbers[idx],numbers,target)