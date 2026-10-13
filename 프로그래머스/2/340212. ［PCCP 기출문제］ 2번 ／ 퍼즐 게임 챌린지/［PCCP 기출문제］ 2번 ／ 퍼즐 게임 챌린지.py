def solution(diffs, times, limit):

    def cal_time(level):
        total = 0 
        for i in range(len(diffs)):
            temp = diffs[i]-level
            if temp<=0:
                total += times[i]
            else:
                time_prev = 0
                if i>0:
                    time_prev = times[i-1]
                total += temp*(times[i] + time_prev) + times[i]
        return True if total<=limit else False
    
    
    left = 1
    right = limit 
    while(left<right):
        mid = (left+right)//2
        # 계산할 수 있다면 더 줄이기 
        if cal_time(mid):
            right = mid 
        else:
            left = mid+1 

    return left


"""
temp = diffs[i]-level
temp<=0 -> time_cur
temp>0 -> temp*(time_cur + time_prev) + time_cur

시뮬레이션으로 할 생각 했지만
이거 이분탐색이네

limit이 넘으면 탐색을 멈춘다. 

"""