def solution(clothes):
    answer = 1

    closet = {}

    for i in range(len(clothes)):
        category = clothes[i][1]

        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1

    for count in closet.values():
        answer *= (count + 1)

    return answer - 1