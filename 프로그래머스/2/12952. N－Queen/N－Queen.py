def solution(n):
    answer = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 우상, 우, 우하만 고려 
    dr = [-1, 0, 1]
    dc = [1, 1, 1]
    
    def check(r,c,delta):
        for i in range(3):
            for j in range(1,n):
                if(0<=r+dr[i]*j<n and 0<=c+dc[i]*j<n):
                    visited[r+dr[i]*j][c+dc[i]*j]+=delta

    def bt(c,cnt):
        nonlocal answer 
        if(cnt==n):
            answer +=1 
            return 
        for i in range(n):
            if not visited[i][c+1]:
                check(i,c+1,1)
                bt(c+1,cnt+1)
                check(i,c+1,-1)
                
    bt(-1,0)   
    return answer


"""
서로 공격할 수 없도록 배치 == 이동했을 때 영원히 만나지 않는다. 
행과 열은 모두 달라야 한다. 
백트래킹으로 배치 완료가 N인 경우 답을 업데이트하기 

visited 배열 만든다. N이 작아서 가능 
1. 현재 노드에서 방문 가능한 것들 방문 처리한다. (0일 경우 예외 처리)
2. 자기 자신의 다음 col 중 방문 가능한 것 하나 선택해서 방문하고 cnt 업데이트 
3. 반복한다. 
4. 만약 cnt==N인 경우 종료하고 answer +=1 


"""