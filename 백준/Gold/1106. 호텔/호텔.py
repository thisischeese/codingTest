import sys 
INF = int(1e9)
input = sys.stdin.readline 
# 사람 수, 도시 개수
people_cnt,cities_cnt = map(int,input().split())
cities = []

for _ in range(cities_cnt):
    # 비용, 사람 수 
    cities.append(list(map(int,input().split())))

# 도시별 최대 고객의 수 100
# dp[i] : i 명을 확보하는 데에 드는 최소 비용 
dp = [INF]*(people_cnt+100)
dp[0] = 0 

for cost,people in cities: 
    for i in range(people,len(dp)): 
        dp[i] = min(dp[i],dp[i-people]+cost)


print(min(dp[people_cnt:]))

'''
모든 도시별로 아래 로직 반복 
i명의 고객을 확보하는 데에 드는 최소 비용 
=> 최소 비용 V.S. i-people명의 고객을 확보하는 데에 드는 최소 비용 + people명 고객 확보에 드는 비용 

주의할 점 : C명 확보에 드는 최소 비용 xx -> 적어도 C명 확보에 드는 최소 비용 
'''