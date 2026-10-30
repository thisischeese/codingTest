def solution(s):
    answer = []
    visited = set()

    # 바깥 괄호 제거하고 집합별로 나누기
    groups = s[2:-2].split("},{")
    groups = [list(map(int, group.split(","))) for group in groups]

    # 원소 개수 적은 순으로 정렬
    groups.sort(key=len)

    for group in groups:
        for num in group:
            if num not in visited:
                visited.add(num)
                answer.append(num)

    return answer