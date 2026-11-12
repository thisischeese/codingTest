
def solution(n, left, right):
    answer = []

    def cal_rc(num):
        r = num // n
        c = num % n
        return r, c

    for i in range(left, right + 1):
        r, c = cal_rc(i)
        answer.append(max(r, c) + 1)

    return answer



"""
n이 10의 7승이라서 brute한 완탐으로 풀면 시간 초과난다... 
한 번씩 쓴다고 하면 10^7 * 10^7 -> 10^8 1s 딱 맞는데 
배열을 또 만들면 left to right에 대해 지워야 하기 때문에 
2*10^8 -> 무조건 시간초과 

그러면 애초에 board를 새롭게 만들고 작성하는 게 아니라
그냥 j번째 숫자가 left to right이 아닌지 확인하고
아니라면 몇번째 행 열에 속하는지 구하고
max(행,열)을 answer 에 append하기 


"""