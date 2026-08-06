from collections import deque 

def solution(cards1, cards2, goal):
    
    q1 = deque(cards1)
    q2 = deque(cards2)
    qg = deque(goal)
    
    while(qg):
        prev = qg.popleft() 
        if(q1 and prev==q1[0]):
            q1.popleft() 
        elif(q2 and prev==q2[0]):
            q2.popleft() 
        else: 
            return "No"
      
    return "Yes"