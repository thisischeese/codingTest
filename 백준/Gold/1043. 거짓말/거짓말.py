import sys 

input = sys.stdin.readline

answer = 0 

N,M = map(int,input().split())
truths = list(map(int,input().split()))
parties = [list(map(int,input().split())) for _ in range(M)]

if len(truths)==1:
    answer = M
else:
    true_ones = set(truths[1:])
    for i in range(M):
        for party in parties:
            party_ones = set(party[1:])
            if(true_ones & party_ones):
                true_ones = true_ones | party_ones
    for i in range(M):
        party_ones = set(parties[i][1:])
        if not (true_ones & party_ones):
            answer +=1 
print(answer)
        