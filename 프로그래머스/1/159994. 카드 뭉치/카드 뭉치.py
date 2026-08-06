def solution(cards1, cards2, goal):
    idx_c1,idx_c2,idx_g = 0, 0, 0
    len_c1,len_c2,len_g = len(cards1), len(cards2), len(goal)
    while(idx_g<len_g):
        if(idx_c1<len_c1 and goal[idx_g]==cards1[idx_c1]): idx_c1 += 1
        elif(idx_c2<len_c2 and goal[idx_g]==cards2[idx_c2]): idx_c2 += 1
        else: return "No" 
        idx_g += 1
    return "Yes"