def solution(words):
    answer = ""
    spaces = []
    idx=0
    temp = ""
    
    while(idx<len(words)):
        if(ord(words[idx])==32):
            temp+=" "
        elif(temp!=""):
            spaces.append(temp)
            temp = ""
        else:
            pass
            
        idx += 1 
    spaces.append(temp)
    
    words = words.split()
    
    for i in range(len(words)):
        word = words[i]
        if(97<=ord(word[0]) and ord(word[0])<=122):
            temp = chr(ord(word[0])-32)
        else:
            temp = word[0]

        for j in range(1,len(word)):
            if(65<=ord(word[j]) and ord(word[j])<=90):
                temp += chr(ord(word[j])+32)
            else:
                temp += word[j]
        words[i] = temp
    print(spaces)  
    if(len(spaces)>len(words)):
        answer = spaces[0]
    for space,word in zip(spaces,words):
        answer+= (word+space)
        
    return answer 
"""
0. 공백 기준으로 split 
1. 모든 단어에 순회 
2. 단어 첫 문자가 소문자 알파벳이면 대문자로 변경하기 (아스키 코드 97~122)
3. 첫 문자 이후의 알파벳을 모두 소문자로 변경하기 
4. 다시 문자열로 바꿔서 return 
"""