import sys

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1_dict = {}
arr2_dict = {}

for i in range(N):
    temp = 0
    for j in range(i, N):
        temp += arr1[j]
        arr1_dict[temp] = arr1_dict.get(temp, 0) + 1

for i in range(M):
    temp = 0
    for j in range(i, M):
        temp += arr2[j]
        arr2_dict[temp] = arr2_dict.get(temp, 0) + 1

a = list(arr1_dict.keys())
answer = 0

for i in range(len(a)):
    diff = T - a[i]
    if diff in arr2_dict:
        answer += arr1_dict[a[i]] * arr2_dict[diff]

print(answer)
