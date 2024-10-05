# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys 
from collections import Counter

N = sys.stdin.readline().strip()
A = Counter(list((map(int,sys.stdin.readline().split()))))
B = Counter(list((map(int,sys.stdin.readline().split()))))

def cal_rep(mydict,max_cnt,rep): 
	maxkey = int(max(mydict.keys()))
	# 가능한 모든 x
	for x in range(2,maxkey+1,1):
		cnt=0
		# 5개의 숫자 개수 세기 x-2부터 x+2까지 
		for size in range(x-2,x+3,1):
			cnt+=mydict.get(size,0)
		if max_cnt<cnt:
			max_cnt = cnt
			rep = x
	return rep

repA = cal_rep(A,0,2) 
repB = cal_rep(B,0,2)
print(repA, repB)
if repA>repB:
	print("good")
else:
	print("bad")
	
	