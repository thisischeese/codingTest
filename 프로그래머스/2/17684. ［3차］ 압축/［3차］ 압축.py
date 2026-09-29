from collections import defaultdict 
def solution(msg):
    
    alpha = defaultdict()
    for i in range(26):
        alpha[chr(i+65)]=i+1 
        
    answer = []
    start = 0
    idx = 27
    
    while(start<len(msg)):
        length =1
        
        while(start+length<=len(msg) and alpha.get(msg[start:start+length]) is not None):
            length += 1
        answer.append(alpha.get(msg[start:start+length-1]))
        #print(start,msg[start:start+length-1],msg[start:start+length])
        if alpha.get(msg[start:start+length]) is None:
            alpha[msg[start:start+length]] = idx
        start = start+length -1 
        idx+=1
        
    return answer

"""
0.사전에서 일치하지 않는 w가 나올 때까지 한 개에서 시작해 점점 길이 늘려간다. 
1.가장 마지막 일치한 것을 w로 지정하고 출력하기 (나오지 않을 수 없음. 대문자 문자열로 초기화되어 있기 때문) 
2.다음 글자 존재하는지 확인한다. 
3.남아있다면 다음 글자랑 합친 글자가 사전에 있는지 대조한다. 
4.사전에 없으면 단어 추가하기 

"""