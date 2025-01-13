import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    com = sys.stdin.readline().split()
    op = com[0]
    if op =='1':
        stack.append(int(com[-1]))
    elif op == '2':
        if stack:
            print(stack.pop(-1))
            continue
        print(-1)
    elif op == '3':
        print(len(stack))
    elif op == '4':
        if stack:
            print(0)
            continue
        print(1)
    elif op == '5':
        if stack:
            print(stack[-1])
            continue
        print(-1)