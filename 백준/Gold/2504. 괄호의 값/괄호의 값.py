import sys  

strings = str(sys.stdin.readline().strip())

def solution(s):
    stack = []

    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if temp == 0 else 2 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    print(0)
                    exit()
            else:
                print(0)
                exit()
        elif char == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if temp == 0 else 3 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    print(0)
                    exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

    result = 0
    for val in stack:
        if isinstance(val, int):
            result += val
        else:
            print(0)
            exit()

    print(result)

solution(strings)
