import sys 
import math 

input = sys.stdin.readline 

N = int(input())
cards = list(map(int,input().split()))
max_card = max(cards)
cards_bool = [False]*(max_card+1)

for card in cards:
    cards_bool[card] = True 

scores = [0 for _ in range(max_card+1)]

idx = 0 
while(idx<N):
    start = cards[idx]
    for next in range(start*2,len(scores),start):
        if(next%start==0 and cards_bool[next]):
            scores[next] -=1
            scores[start] +=1 
    idx+=1 

for card in cards:
    print(scores[card],end=' ')


'''
1~1e6 
if a%b==0 -> a -1, b +1 
else -> tied

3%4==3
3%12==3

4%3==1
4%12==4

12%3==0
12%4==0

3 4 12
1 1 -2

이중 for문 : (10^5)^2 > 10^8 
실제로 시뮬레이션을 돌리지 말고
O(NlogN) or O(N) 이 되는 알고리즘 구현해야 worst case 통과 
에라토스테네스의 체 시간복잡도는 O(Nlog(logN))


'''