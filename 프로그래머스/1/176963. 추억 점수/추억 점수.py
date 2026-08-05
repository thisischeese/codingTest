def solution(name, yearning, photos):
    score = dict(zip(name,yearning))
    
    answer = [sum(score.get(person,0) for person in photo) \
              for photo in photos]
    return answer