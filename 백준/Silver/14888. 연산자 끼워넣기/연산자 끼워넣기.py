import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))  

max_num = -1e9
min_num = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == N:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)