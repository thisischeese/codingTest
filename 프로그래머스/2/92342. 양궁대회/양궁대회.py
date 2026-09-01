from copy import copy
def solution(n, apeach):
    answer = [-1]
    diff = 0 
    
    def getscore(apeach, lion):
        atemp,ltemp = 0,0
        for i in range(len(apeach)):
            if(apeach[i]==lion[i] and lion[i]==0):
                continue  
            if(apeach[i]<lion[i]):
                ltemp += (10-i)
            else:
                atemp += (10-i)
        return atemp, ltemp  

    # total : 과녁에 쏜 전체 화살 개수 
    def backtrack(idx,lion,total):
        if(total>n or idx>11):
            return
        elif(idx==11):
            tascore, tlscore = getscore(apeach,lion)
            nonlocal answer
            nonlocal diff 
            tdiff = tlscore - tascore
            if (diff<tdiff):
                diff = tlscore - tascore
                lion[10] = n-sum(lion)
                answer = lion.copy()
            elif(tdiff!=0 and diff==tdiff):
                if(answer[::-1]<lion[::-1]):
                    diff = tlscore - tascore
                    answer = lion.copy()
            return 
        for arrow_num in [0,apeach[idx]+1]:
            lion[idx] = arrow_num 
            backtrack(idx+1,lion,total+arrow_num)
        
    backtrack(0,[0 for _ in range(11)],0)
    
    return answer


"""
라이언이 어피치를 가장 큰 점수 차이로 이기도록 하는 과녁 점수 구하기 
만약 이 경우가 여러 가지이면 점수를 더 고르게 분포시켜서 얻을 수 있는 경우를 return해야 한다... 

1. 어피치가 n번 -> 라이언이 n번 
2. k점을 맞춘 횟수 a  v.s. b
    2.1 a!=0, b!=0, 차이 있음 : 더 큰 횟수를 가진 선수에게 k점 부여
    2.2 a!=0, b!=0, 차이 없음 : 어피치가 k점 
    2.3 a==b==0 : pass 
3. 최종 점수 계산하기 
    3.1 차이 있을 경우 더 큰 사람이 우승
    3.2 차이 없을 경우 어피치 우승 

전체 합이 n이어야 하기 때문에 점수 배분 최적화가 필요함. 
-> 어떻게 보면 그리디가 아닌가?
=> 가장 큰 점수 차이를 원하니까 10점부터 scan을 해야? 
10점부터 0점까지 총 11개의 어피치 점수를 담은 info 주어짐
매우 숫자가 작다. 일반적인 구현인가? 싶기는 한데 
info는 거꾸로 이미 나열됨 

고민되는 것은 라이언이 어떻게 하든 어피치보다 지는 경우를 어떻게 판별할 것인가? 이기 ㄴ한데.. 

라이언이 무조건 이겨야 하잖아. 
그러면 라이언이 어피치보다 작은 점수를 받는 케이스 고려할 필요가 없음. 

어피치 : [2,1,1,1,0,0,0,0,0,0,0]
라이언 : 0이거나 어피치 점수보다 1 크거나 (단, 가용 가능한 범위보다 작을 것)
백트래킹 + 완탐 

문득 드는 생각이 n발을 꼭 다 사용하지 않아도 이길 수 있는 것 아님?? 아님. 
라이언도 n발 사용해야 하기 때문에 낮은 점수 더 많이 맞추도록 뒤에 붙여줘야 하마. 
"""