def solution(cacheSize, cities):
    answer = 0  
    if(cacheSize==0): return 5*len(cities)
    cities = [city.lower() for city in cities]
    cache = []
    for i in range(len(cities)):
        city = cities[i]
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache)!=0 and len(cache)>=cacheSize:
                del cache[0]
            cache.append(city)
            answer += 5
    return answer
"""
1. for문 순회 
2. 원소가 캐시에 존재하는지 검사
    2.1 존재한다면 원소 캐시 순서 가장 위로 변경 && answer += 1
    2.2 존재하지 않는다면 가장 마지막 원소 제거 && 캐시 삽입 && answer += 5
"""