import sys
from collections import Counter

N = int(sys.stdin.readline().strip()) 
original = sys.stdin.readline().strip()
words = [sys.stdin.readline().strip() for _ in range(N - 1)]  

original_count = Counter(original)

answer = 0 
for word in words:
    word_count = Counter(word)

    # 같은 구성
    if word_count == original_count:
        answer += 1
        continue

    # 한 글자 추가 or 삭제
    diff_add = sum((word_count - original_count).values())  
    diff_remove = sum((original_count - word_count).values())

    if diff_add == 1 and diff_remove == 0:
        answer += 1
    elif diff_add == 0 and diff_remove == 1:
        answer += 1
    elif diff_add == 1 and diff_remove == 1:
        answer += 1

print(answer)
