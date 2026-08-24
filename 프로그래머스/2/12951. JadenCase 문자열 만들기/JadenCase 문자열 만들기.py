def solution(words):
    return " ".join(word.capitalize() for word in words.split(" "))
    
"""
1. 처음부터 문자열 스캔하기
2. capitalize 수행하기 
"""