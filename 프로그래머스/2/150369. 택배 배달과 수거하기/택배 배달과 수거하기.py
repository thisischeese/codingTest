
def solution(cap, n, deliveries, pickups):
    answer = 0

    d_idx = n - 1
    p_idx = n - 1

    while True:
        
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1

        while p_idx >= 0 and pickups[p_idx] == 0:
            p_idx -= 1

        if d_idx < 0 and p_idx < 0:
            break

        answer += (max(d_idx, p_idx) + 1) * 2

        d_cap = cap
        p_cap = cap

        # 배송
        while d_idx >= 0 and d_cap > 0:
            amount = min(d_cap, deliveries[d_idx])
            deliveries[d_idx] -= amount
            d_cap -= amount

            if deliveries[d_idx] == 0:
                d_idx -= 1

        # 수거
        while p_idx >= 0 and p_cap > 0:
            amount = min(p_cap, pickups[p_idx])
            pickups[p_idx] -= amount
            p_cap -= amount

            if pickups[p_idx] == 0:
                p_idx -= 1

    return answer


"""
거꾸로 방문하면서 배송과 수거 처리하기
배송과 수거는 각각 cap만큼 가능하므로 개별적으로 관리

0. 배송과 수거가 모두 완료될 때까지 while -> 모두 0이면 수거 및 배송 종료 
1. d_idx와 p_idx를 각각 배송과 수거 필요한 가장 먼 인덱스로 갱신
2. answer += max(d_idx,p_idx)
3. d_cap과 p_cap을 cap으로 초기화하기
4. 배송 배열을 뒤에서부터 훑으면서 min(d_cap, deliveries[d_idx])만큼 처리하기
   - 배송 완료한 집이면 d_idx 감소시키기
   - d_cap이 0이면 중단하기
5. 수거 과정 동일하게 3,4 진행 
"""

