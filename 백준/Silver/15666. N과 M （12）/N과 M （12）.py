import sys 

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
visited = set()

def backtrack(start, path):
    if len(path) == M:
        tup = tuple(path)
        if tup not in visited:
            visited.add(tup)
            print(' '.join(map(str, path)))
        return
    
    for i in range(start, N):
        backtrack(i, path + [numbers[i]])

backtrack(0, [])
