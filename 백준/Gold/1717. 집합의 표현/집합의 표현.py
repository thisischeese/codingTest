import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a_root = find(parent, a)
    b_root = find(parent, b)
    if a_root != b_root:
        parent[b_root] = a_root 

n, m = map(int, input().split())
parent = [i for i in range(n+1)] 


for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(parent, a, b)
    elif op == 1:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")

