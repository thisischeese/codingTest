from collections import defaultdict 

def solution(n, words):
    check = {words[0]:1}
    for i in range(1,len(words)): 
        if (check.get(words[i],0)==0 and words[i-1][-1]==words[i][0]):
            check[words[i]]=1 
        else: 
            return [i%n+1,i//n+1]
    return [0,0]