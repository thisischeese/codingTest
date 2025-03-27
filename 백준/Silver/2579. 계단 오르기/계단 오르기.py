import sys

# 입력 처리
N = int(sys.stdin.readline())
S = [int(sys.stdin.readline()) for _ in range(N)]

if N == 1:
    print(S[0])
    sys.exit()
else:
    dp = [0] * N
    dp[0] = S[0] 
    dp[1] = S[0] + S[1]  

if N == 2:
    print(dp[1])
    sys.exit()
else:
    dp[2] = max(S[0] + S[2], S[1] + S[2])


for i in range(3, N):
    dp[i] = max(dp[i - 2] + S[i], dp[i - 3] + S[i - 1] + S[i])


print(dp[N - 1])
