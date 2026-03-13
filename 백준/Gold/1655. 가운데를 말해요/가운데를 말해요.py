import sys 
import heapq

input = sys.stdin.readline 

N = int(input())

left = [] # med보다 작거나 같
right = [] # med보다 크다
answers = []

heapq.heapify(left)
heapq.heapify(right)

for i in range(N):
    
    num = int(input())
    
    if(len(left)==len(right)):
        heapq.heappush(left,-num)
    else:
        heapq.heappush(right,num)

    # left의 max > right max -> 교체
    if(right and -left[0]>right[0]):
        left_val = -heapq.heappop(left)
        right_val = heapq.heappop(right)
        heapq.heappush(left,-right_val)
        heapq.heappush(right,left_val)

    answers.append(str(-left[0]))
        
            
            
print("\n".join(answers))  
    


'''
insert가 빈번히 발생함 -> insert 값이 작아야 한다 
insert 값을 어떻게 작게 만들 것인가? bs? 로 해도 log(N^2)이 됨
heap을 2개 만들어서 insert할 때 양 끝 값만 대조하도록 시간 복잡도 줄이기
'''