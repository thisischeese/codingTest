def solution(topping):
    answer = 0
    dp = [[0,0] for _ in range(len(topping))]
    cnt_topping_f = set()
    cnt_topping_r = set()
    
    for i in range(len(topping)):
        cnt_topping_f.add(topping[i])
        cnt_topping_r.add(topping[len(topping)-i-1])
        
        dp[i][0]=len(cnt_topping_f)
        dp[len(topping)-i-1][1]=len(cnt_topping_r)
        
    for i in range(len(topping)-1):
        if dp[i][0]==dp[i+1][1]:
            answer +=1 
        
    return answer

"""
롤케이크를 공평하게 자르는 방법의 수를 return 해야 함 
그런데 topping의 길이가 1e6이다. 
그렇기에 자르는 구간마다 앞 구간 뒷 구간의 토핑 개수를 count하면 1e7됨 
뭔가 dp로 풀이하는 방법도 가능할 것 같기는 한데
그냥 구현으로 풀어도 통과는 할 듯?
"""