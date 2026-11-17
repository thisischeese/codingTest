def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    print(len(arr1))
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            for k in range(len(arr2[0])):
                answer[i][k] += arr1[i][j]*arr2[j][k]

    return answer 
"""
단순 구현이긴 한데 배열 원소 단 한 번씩만 조회해서 시간복잡도 줄이는 것이 중요
answer[i][k] = SUM(arr1[i][j]*arr2[j][k])
"""