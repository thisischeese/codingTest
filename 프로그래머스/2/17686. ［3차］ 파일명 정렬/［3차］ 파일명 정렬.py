def solution(files):
    folder = []
    
    def check(s):
        ord_s = ord(s)
        if (97<=ord_s<=122 or 65<=ord_s<=90 or ord_s in [32,45,46]):
            return True 
        return False 
    
    for i in range(len(files)):
        file = files[i]
        
        head_idx = 0 
        HEAD = ""
        while(head_idx<len(file)):
            if not check(file[head_idx]):
                HEAD = file[:head_idx].lower()
                break 
            head_idx+=1
                
        number_idx = head_idx
        NUMBER = ""
        while(number_idx<=len(file)):
            if number_idx==len(file) or check(file[number_idx]):
                NUMBER = file[head_idx:number_idx]
                break 
            number_idx += 1
        
        folder.append((HEAD, int(NUMBER), i))
    
    folder.sort(key=lambda x : (x[0],x[1]))
        
    return [files[i] for _,_,i in folder]

"""
공백 : 32
점 : 46
a : 97, z : 122
A : 65, Z : 90

0. 모든 문자열을 순회한다. 
1. 처음으로 영문자가 아닌 문자가 나오는 부분을 HEAD로 분리한다.
2. HEAD 이후부터 가다가 처음으로 영문자 또는 공백 또는 점 나오는 부분 또는 더 이상 문자 없음 때까지가 NUMBER로 분리한다. 
3. folder에 (HEAD, int(NUMBER), file_idx)를 append한다. 
4. folder[:]의 [0]을 순서대로 정렬하되, 같으면 [1] 순서대로 정렬한다. 
5. folder의 file_idx를 따라서 answer 배열을 만든다. 
"""