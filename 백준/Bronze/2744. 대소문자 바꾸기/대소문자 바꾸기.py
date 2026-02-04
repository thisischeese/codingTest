import sys 

input = sys.stdin.readline 

word = input().strip() 

for w in word:
    if(ord(w)>=96):
        print(chr(ord(w)-32),end='')
    else:
        print(chr(ord(w)+32),end='')
