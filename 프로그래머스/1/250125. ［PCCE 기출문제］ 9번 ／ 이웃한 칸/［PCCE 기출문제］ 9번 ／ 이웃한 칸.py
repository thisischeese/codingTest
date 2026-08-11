def solution(board, h, w):
    return len(list(filter(lambda p: 0<=p[0]<len(board) \
                           and 0<=p[1]<len(board[0])\
                           and board[p[0]][p[1]] == board[h][w],\
                           [(h+1,w),(h-1,w),(h,w+1),(h,w-1)])))
