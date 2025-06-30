import sys

input = sys.stdin.readline

stack = []

N = int(input())
heights = list(map(int, input().split()))
answer = [0 for _ in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1] > heights[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, heights[i]))

for item in answer:
    print(item,end=' ')