import sys 
from itertools import combinations

vowels= []
cons= []
result = []

L,C = map(int,sys.stdin.readline().split())
alphabet = list(map(str,sys.stdin.readline().split()))

# 모음 구하기
for alpha in alphabet:
    if alpha in ['a','e','i','o','u']:
        vowels.append(alpha)
    else:
        cons.append(alpha)


# 가능한 자음 개수 : 2 ~ (L-1)
# 가능한 모음 개수 : 1 ~ (L-2)
for i in range(1,L-1):
    vcomb = list(combinations(vowels,i))
    ccomb = list(combinations(cons,L-i))
    
    for v in vcomb:
        for c in ccomb:
            # 리스트
            word = sorted(v+c)
            result.append("".join(word))
            
result.sort()
for word in result:
    print(word)
    