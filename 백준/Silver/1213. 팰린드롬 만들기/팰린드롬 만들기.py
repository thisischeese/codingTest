import sys
from collections import Counter

name = str(sys.stdin.readline().rstrip())
alpha_dict = Counter(name)

def palindrome(alpha_dict):
    center = ''
    half_part = ''

    odd_count = sum(1 for v in alpha_dict.values() if v % 2 == 1)
    if odd_count > 1:
        return "I'm Sorry Hansoo"

    for key in sorted(alpha_dict.keys()):
        half_part += key * (alpha_dict[key] // 2) 
    
    
    for key, value in alpha_dict.items():
        if value % 2 == 1:
            center = key
            break

    return half_part + center + half_part[::-1]

print(palindrome(alpha_dict))
