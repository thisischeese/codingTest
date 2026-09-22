def solution(word):
    words = []

    def dfs(s):
        if len(s) == 5:
            return
        for c in "AEIOU":
            words.append(s + c)
            dfs(s + c)

    dfs("")
    return words.index(word) + 1