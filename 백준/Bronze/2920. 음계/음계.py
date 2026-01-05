import sys 

input = sys.stdin.readline 

def check()->str:
    flag_a = True 
    flag_d = True 
    prev = arr[0]
    for a in arr[1:]:
        if a==prev-1:
            flag_a = False
        elif a==prev+1:
            flag_d = False 
        else:
            return "mixed"
        prev = a
    return "ascending" if flag_a else "descending"


arr = list(map(int,input().split()))
print(check())