# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys 
from collections import deque

# 스택에 저장 
A, B = list(map(str,sys.stdin.readline().split()))

def sep_oper(myarr):
	newarr = []
	mystr=''
	for idx in range(len(myarr)):
		if myarr[idx] not in ["*","-","+"]:
			mystr+=myarr[idx]
		else:
			newarr.append(int(mystr))
			newarr.append(myarr[idx])
			mystr=''
		if idx==len(myarr)-1:
			newarr.append(int(mystr))
		
	return newarr

# 곱하기 먼저 계산
def cal_mul(myarr):
	stack = []
	idx=0
	while(True):
		if idx==len(myarr):
			break
		elif idx==0:
			stack.append(myarr[idx])
			idx+=1
		elif myarr[idx] =="*":
			temp = stack.pop()
			stack.append(temp*myarr[idx+1])
			idx+=2
		else:
			stack.append(myarr[idx])
			idx+=1

	return stack

# 덧셈 뺄셈 계산 
def cal_others(myarr):
	queue = deque(myarr)
	idx=0
	while(True):
		if idx==0:
			num1 = queue.popleft()
			answer=num1
			idx+=1
		elif idx == len(myarr):
			break
		else:
			op = queue.popleft()
			num2 = queue.popleft()
			if op=="-":
				answer-=num2
			else:
				answer+=num2
			idx+=2
	
	return answer

answer_A = cal_others(cal_mul(sep_oper(A)))
answer_B = cal_others(cal_mul(sep_oper(B)))

print(max(answer_A,answer_B))


			
		
	
	