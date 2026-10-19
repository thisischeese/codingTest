def solution(info, n, m):
    INF = float('inf')

    dp = [INF] * m
    dp[0] = 0
    
    for a, b in info:
        next_dp = [INF] * m

        for j in range(m):
            if dp[j] == INF:
                continue

            # A가 훔치는 경우
            if dp[j] + a < n:
                next_dp[j] = min(next_dp[j], dp[j] + a)

            # B가 훔치는 경우
            if j + b < m:
                next_dp[j + b] = min(next_dp[j + b],dp[j])

        dp = next_dp

    answer = min(dp)
    return answer if answer != INF else -1