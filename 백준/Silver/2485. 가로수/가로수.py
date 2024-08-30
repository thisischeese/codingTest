
def init_list():
    # 가로수 개수 
    n = int(input())
    tree=[]
    dist = []
    
    # 간격 리스트 생성 
    for i in range(1,n+1,1):
        tree.append(int(input()))
        if i!=1:
            dist.append(tree[i-1] - tree[i-2])
    return tree,dist

def cal_euclidean(n,m):
    # 두 수 중 큰 수를 작은 수로 나눈다
    if n>m:
        max_num = n
        min_num = m
    else:
        max_num = m
        min_num = n
    # 나머지가 0 아님 -> 작은 수 = 큰 수, 나머지 = 작은 수  설정 후 처음부터 반복 
    remainder = max_num%min_num
    if (remainder):
        return cal_euclidean(min_num,remainder)
    # 나머지가 0 -> 작은 수가 최대공약수 
    else:
        return min_num

def cal_divisor(tree,dist):
    divisor=dist[0]
   
    for item in dist[1:]:
        divisor = cal_euclidean(divisor,int(item))
    return divisor
    
def answer():
    tree,dist = init_list()
    divisor = cal_divisor(tree,dist)
    answer = (tree[-1]-tree[0])/divisor +1
    
    answer -= len(tree)
    
    
    return int(answer)
    
print(answer())
