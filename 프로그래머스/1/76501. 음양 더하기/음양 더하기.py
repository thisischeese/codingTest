def solution(absolutes, signs):
    return sum(list(map(lambda a,s: a if s else -a,absolutes,signs)))