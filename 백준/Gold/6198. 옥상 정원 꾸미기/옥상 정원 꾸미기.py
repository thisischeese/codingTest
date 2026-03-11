import sys

input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]

stack = []
total_count = 0

for h in heights:
    while stack and stack[-1] <= h:
        stack.pop()
    
    total_count += len(stack)
    
    stack.append(h)

print(total_count)