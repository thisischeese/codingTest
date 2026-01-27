import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
n, m = len(s1), len(s2)

# 1. DP 테이블 (0으로 초기화)
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 2. LCS 길이 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 길이 출력
print(dp[n][m])

# 3. 역추적 (이 부분의 오타를 수정했습니다)
if dp[n][m] != 0:
    result = []
    curr_i, curr_j = n, m
    
    while curr_i > 0 and curr_j > 0:
        # 두 문자가 같으면 결과에 추가하고 대각선 위로 이동
        if s1[curr_i-1] == s2[curr_j-1]:
            result.append(s1[curr_i-1])
            curr_i -= 1
            curr_j -= 1
        # 다르면 dp 테이블 값이 더 큰 쪽으로 이동
        elif dp[curr_i-1][curr_j] >= dp[curr_i][curr_j-1]: # j -> curr_j로 수정
            curr_i -= 1
        else:
            curr_j -= 1
            
    print("".join(reversed(result)))