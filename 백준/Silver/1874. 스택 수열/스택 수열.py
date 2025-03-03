import sys 

stack = []
curr = 1
n = int(sys.stdin.readline())

def solution(n,curr):
    answer = []
    for _ in range(n):
        num = int(sys.stdin.readline())

        while(curr<=num):
            stack.append(curr)
            answer.append("+")
            curr+=1
        if num==stack[-1]:
            stack.pop()
            answer.append("-")
        else:
            answer = ["NO"]
            return answer
    return answer
    
ans = solution(n,curr)

for item in ans:
    print(item)