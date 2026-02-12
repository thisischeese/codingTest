import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 

class Node:
    def __init__(self):
        self.children = []
        self.cnt = 1 # 서브 트리 내부 원소 개수 -> 처음에는 자기 자신만 cnt하도록 
    def add_child(self,child):
        self.children.append(child)
    def is_leaf(self):
        return True if len(self.children)==0 else False 
    def get_cnt(self):
        return self.cnt 
    def update_cnt(self,cnt):
        self.cnt += cnt
        return self.cnt 
    def get_children(self):
        return self.children

def init_node(idx):
    visited[idx] = True 
    node = Node() 
    
    for child in arr[idx]:
        # 탑다운이니까 아직 방문하지 않았다면 자식이 맞음 
        if not visited[child]:
            node.add_child(child)

    tree[idx] = node            
    
    # 자식 없으면 추가적 호출 없이 종료 
    if(node.is_leaf()):
        return  
    
    for child in arr[idx]:
        if not visited[child]:
            init_node(child)

# 재귀적으로 leaf까지 내려가서 다시 올라오면서 cnt를 업데이트하기 
def update_node(idx):   
    if tree[idx].is_leaf():
        return tree[idx].get_cnt()
    total = 0
    for child in tree[idx].get_children(): 
        total += update_node(child)
    return tree[idx].update_cnt(total)
        
    

N,R,Q = map(int,input().split())
arr = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
tree = {} 

for _ in range(N-1): 
    u,v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

# 루트 노드부터 훑으면서 부모 자식 관계 정립하고 tree 초기화하기 
init_node(R)

# 말단 노드부터 훑으면서 subtree 원소 개수 업데이트 하기 
update_node(R)

for _ in range(Q):
    subR = int(input())
    print(tree[subR].get_cnt()) 

'''
완전이진트리도 아니고 이진트리도 아니다 => segtree 불가능 

입력 들어올 때 부모, 자식이 구분되어 들어오지 않음 
-> 그냥 인접 리스트 형태로 저장해두었다가 로직 거치며 처리하기 ? 

구하는 것 : 서브 트리별 노드 개수 
=> subproblem으로 쪼갤 수 있는데 subproblem의 값이 상위 problem의 답을 구할 때 사용됨 
=> DP..?
=> 각자 바로 자기 직계 자식의 노드 개수만을 합산해서 dp 배열을 업데이트 하기..? 
노드를 각각 한 번씩만 훑도록 구현 => O(N)으로 업데이트 하기..? 

주의할 점은 어느 노드가 부모 노드인지 모른다..는 점..
=> visited 배열이 필요하다.. 

'''