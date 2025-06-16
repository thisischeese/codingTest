import sys

def dfs(index, current_sum):
    global answer
    if index == N:
        if current_sum == S:
            answer += 1
        return
    
    dfs(index + 1, current_sum + numbers[index])
    dfs(index + 1, current_sum)

input = sys.stdin.readline
N, S = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0


dfs(0, 0)

if S == 0:
    answer -= 1

print(answer)
