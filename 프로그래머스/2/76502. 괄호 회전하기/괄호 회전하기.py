def solution(s):
    answer = len(s)
    comb = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    for idx in range(len(s)):
        stack = []
        target = s[idx:] + s[:idx]

        for tar in target:

            # 1. 여는 괄호
            if tar in "({[":
                stack.append(tar)

            # 2. 닫는 괄호인데 스택이 비어있음
            elif not stack:
                answer -= 1
                break

            # 3. 닫는 괄호이고 짝이 맞음
            elif comb[stack[-1]] == tar:
                stack.pop()

            # 4. 닫는 괄호인데 짝이 안 맞음
            else:
                answer -= 1
                break

        else:
            # break 없이 문자열 끝까지 검사했는데
            # 여는 괄호가 남아있음
            if stack:
                answer -= 1

    return answer