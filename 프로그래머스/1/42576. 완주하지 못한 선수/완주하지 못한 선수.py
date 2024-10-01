def solution(participant, completion):
    answer = ''

    pdict = {p:0 for p in participant}
    for p in participant:
        pdict[p]+=1
    cdict = {p:0 for p in participant}
    for c in completion:
        cdict[c]+=1
    
    for p in participant:
        if pdict[p]!=cdict[p]:
            answer+=p
            break
        
    return answer