import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    garments = Counter()
    for _ in range(n):
        name, category = input().strip().split()
        garments[category] += 1

    result = 1
    for count in garments.values():
        result *= (count + 1)
    print(result - 1)
