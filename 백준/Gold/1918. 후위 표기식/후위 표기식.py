import sys

precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
operators = set(['+', '-', '*', '/'])
parentheses = ['(', ')']

infix = list(map(str, sys.stdin.readline().strip()))

stack = []
postfix = []

for token in infix:
    if token.isalpha():
        postfix.append(token)
    elif token == '(':
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    elif token in operators:
        while (stack and stack[-1] != '(' and
               precedence.get(stack[-1], 0) >= precedence[token]):
            postfix.append(stack.pop())
        stack.append(token)

while stack:
    postfix.append(stack.pop())

print(''.join(postfix))
