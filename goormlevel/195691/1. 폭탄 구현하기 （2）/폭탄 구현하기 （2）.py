# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys 
from copy import deepcopy

N, K = map(int,sys.stdin.readline().split())
graph = [list(map(str,sys.stdin.readline().split())) for _ in range(N)]
bombed_graph = [[0 for _ in range(N)] for _ in range(N)]
target = [[t[0]-1,t[1]-1] for t in (list(map(int,sys.stdin.readline().split())) for _ in range(K))] # 주의 : (y,x) 꼴 
dxs = [0,0,-1,1]
dys = [-1,1,0,0]
# 영역 밖 벗어남 or '#' -> 유지
# 0 -> 1 증가 
# @ -> 2 증가 
# 주의 : target 위치 표기 (y:1,x:1) ~ (y:N,x:N)

def cal_bomb(tar,G,newG):

	if G[tar[0]][tar[1]]=="0":
		newG[tar[0]][tar[1]] += 1
	elif G[tar[0]][tar[1]] == "@":
		newG[tar[0]][tar[1]] += 2
	return newG

def update_graph(G,B,N,K,dxs,dys,newG):
	# 1. 폭탄 떨어진 위치에서 상하좌우 영역 내 확인, 값에 따라 어떻게 변할지 값 갱신 
	# 2. 전체 리스트에서 max값 출력 
	for curr in B:
		positions = [curr]
		#print(curr)
		for dx,dy in zip(dxs,dys):
			#print(dx)
			if ((0<=curr[0]+dx<=N-1) and (0<=curr[1]+dy<=N-1)): 
				positions.append([curr[0]+dx,curr[1]+dy])
		for pos in positions:
			#print(pos)
			newG = cal_bomb(pos,G,newG)
	
	return newG
result_graph = update_graph(graph,target,N,K,dxs,dys,bombed_graph)
maxr = 0
for r in result_graph:
	temp = max(r)
	maxr = max(temp,maxr)
print(maxr)

