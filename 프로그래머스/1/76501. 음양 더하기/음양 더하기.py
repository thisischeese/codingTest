def solution(absolutes, signs):
    return sum(map(lambda a,s: a if s else -a,absolutes,signs))