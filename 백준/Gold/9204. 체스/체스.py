import sys 

pos = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
inv_pos = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}

def find_path(x0, y0, x1, y1):
    if (x0 + y0) % 2 != (x1 + y1) % 2:
        return "Impossible", []
    
    if x0 == x1 and y0 == y1:
        return 0, [inv_pos[x0],str(y0+1)]
    
    if abs(x0 - x1) == abs(y0 - y1):
        return 1, [inv_pos[x0],str(y0+1), inv_pos[x1],str(y1+1)]
    
    for i in range(8):
        for j in range(8):
            if abs(x0 - i) == abs(y0 - j) and abs(x1 - i) == abs(y1 - j):
                return 2, [inv_pos[x0],str(y0+1), inv_pos[i],str(j+1), inv_pos[x1],str(y1+1)]
    
    return "Impossible", []

def solution(x0, y0, x1, y1):
    result, path = find_path(x0, y0, x1, y1)
    if result == "Impossible":
        return "Impossible"
    else:
        return str(result) + ' ' + ' '.join(path)

T = int(sys.stdin.readline())
for _ in range(T):
    a, b, c, d = sys.stdin.readline().split()
    x0, y0 = pos[a], int(b) - 1
    x1, y1 = pos[c], int(d) - 1
    print(solution(x0, y0, x1, y1))
