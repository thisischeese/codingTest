def solution(words):
    words = list(words)
    for i in range(len(words)):
        if((i==0 or (i>0 and ord(words[i-1])==32)) and 97<=ord(words[i])<=122):
            words[i] = chr(ord(words[i])-32)
        elif((i>0 and ord(words[i-1])!=32) and 65<=ord(words[i])<=90):
            words[i] = chr(ord(words[i])+32)
    return "".join(words)
    
"""
1. 처음부터 문자열 스캔하기
2. 만약 문자가 공백이거나 숫자이다 -> 그대로 추가
3. 만약 문자가 소문자인데 이전 문자가 공백이거나 인덱스가 0이다 -> 대문자로 바꾸기
4. 만약 문자가 대문자인데 이전 문자가 공백이 아니다 -> 소문자로 바꾸기 
"""