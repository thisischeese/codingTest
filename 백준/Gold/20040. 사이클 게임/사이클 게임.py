import sys 

input = sys.stdin.readline 

def find(a):
    if(parents[a]!=a):
        parents[a] = find(parents[a])
    return parents[a]
        
def union(a,b):
    pa = parents[a]
    pb = parents[b]
    if(pa<pb):
        parents[pb] = pa
    else:
        parents[pa] = pb 


n,m = map(int,input().split())
parents = [i for i in range(n+1)]

for i in range(1,m+1):
    x,y = map(int,input().split())
    if(find(x)==find(y)):
        print(i)
        sys.exit() 
    union(x,y)

print(0)



'''
union find 
1. 간선 입력받기
2. 입력받을 때마다 cycle 체크하기 
3. cycle 발생하는 순간 sys exit 
4. cycle 영원히 발생 x -> 0 출력 
'''