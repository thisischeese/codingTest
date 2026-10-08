import sys 
sys.setrecursionlimit(int(1e6))

def solution(n, t, m, p):
    
    elements = [str(i) for i in range(10)]+["A","B","C","D","E","F"]
    seq = []
    
    def get_num(num,n):
        if(num<n):
            return elements[num]
        else:
            return get_num(num//n,n)+elements[num%n]


    for num in range(m*t+1):
        trans = get_num(num,n)
        for temp in trans:
            seq.append(temp)
            
    return "".join([seq[i] for i in range(p-1,len(seq),m)])[:t]

"""
1. t 개수의 숫자 순회한다. 
2. 순회하며 이를 n 진법으로 바꿔서 seq에 넣는다. 
3. 튜브의 순서에 해당하는 seq 원소를 result로 구성해 반환한다. 
"""