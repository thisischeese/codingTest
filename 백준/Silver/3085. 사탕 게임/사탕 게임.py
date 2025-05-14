import sys

def check(board, N):
    max_candies = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                count += 1
                max_candies = max(max_candies, count)
            else:
                count = 1
        count = 1
        for j in range(1, N):
            if board[j][i] == board[j - 1][i]:
                count += 1
                max_candies = max(max_candies, count)
            else:
                count = 1
    return max_candies

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

max_result = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            max_result = max(max_result, check(board, N))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            max_result = max(max_result, check(board, N))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(max_result)
