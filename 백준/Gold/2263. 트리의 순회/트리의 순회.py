import sys 
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 

def divide_tri(psidx,peidx,isidx,ieidx):

    if(psidx>peidx or isidx>ieidx):
        return 
    
    # post에서 root(peidx) 찾기 + 출력 
    root = postorder[peidx]
    print(root,end=' ')
    
    # inorder에서 root의 idx 찾기 
    in_root_idx = position[root]
    
    step = in_root_idx-1-isidx
    # 왼 subtree 호출 
    divide_tri(psidx,psidx+step ,isidx,in_root_idx-1)
    # 오 subtree 호출 
    divide_tri(psidx+step+1,peidx-1,in_root_idx+1,ieidx)
    
    
    

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

position = [0]*(n+1)
for i in range(n):
    position[inorder[i]]=i


divide_tri(0,n-1,0,n-1)

'''
inorder : left -> root -> right 
postorder : left -> right -> root 
현재 관찰 중인 subtree 내부에서 
가장 오른쪽 postorder 원소는 root임 
inorder에서 root idx를 찾고 이를 기준으로 
왼쪽 :eidx에 대해서 재귀 호출, 오른쪽 sidx:에 대해서 재귀 호출 

preorder : root -> left -> right 
'''