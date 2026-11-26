def solution(elements):
    sums = {sum(elements)}|set(elements)
    temp = elements*2
    for length in range(2,len(elements)):
        for i in range(len(elements)):
            sums.add(sum(temp[i:i+length]))
    return len(sums)

"""
원형 수열의 가장 긴 길이는 원소 길이와 같다 

"""