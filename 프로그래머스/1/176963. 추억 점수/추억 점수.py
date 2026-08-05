from collections import defaultdict

def solution(name, yearning, photos):
    answer = [0 for _ in range(len(photos))]
    score = defaultdict(int)
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
        
    for p_idx in range(len(photos)):
        for j in range(len(photos[p_idx])):
            answer[p_idx] += score[photos[p_idx][j]]

    return answer