from collections import Counter

def solution(phone_book):
    # 접두사 가능한 리스트 
    max_num = len(max(phone_book,key=len))
    min_num = len(min(phone_book,key=len))
   
    if max_num!=min_num:
        prefix = [p for p in phone_book if (len(p)<max_num)]
    else:
        prefix = phone_book[:]
        
    for i in range(min_num,max_num,1):
        temp = [p[:i] for p in phone_book]
        phone_dict = Counter(temp)
        for key in phone_dict.keys():
            if phone_dict[key]!=1:
                if key in prefix:
                    return False        


    return True