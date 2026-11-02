def solution(land):
    dp = land[0][:]

    for r in range(1, len(land)):
        temp = [0] * 4

        for c in range(4):
            temp[c] = land[r][c] + max(dp[k] for k in range(4) if k != c)

        dp = temp

    return max(dp)