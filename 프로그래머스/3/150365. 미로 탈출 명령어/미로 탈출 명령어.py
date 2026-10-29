def solution(n, m, sr, sc, er, ec, k):
    answer = ""

    dist = abs(sr-er) + abs(sc-ec)

    if dist > k or (k-dist)%2 != 0:
        return "impossible"

    directions = [("d",1,0),("l",0,-1),("r",0,1),("u",-1,0)]

    cr,cc = sr,sc

    for i in range(k):
        for p,dr,dc in directions:
            nr,nc = cr+dr,cc+dc

            if not (1<=nr<=n and 1<=nc<=m):
                continue

            remain = k-i-1
            dist = abs(nr-er)+abs(nc-ec)

            if dist <= remain and (remain-dist)%2 == 0:
                answer += p
                cr,cc = nr,nc
                break

    return answer