import sys 

def get_input():
    num=int(sys.stdin.readline().strip())
    mylist=[]
    for i in range(num):
        word=list(sys.stdin.readline().strip())
        mylist.append(word)
    return mylist

def check_word(words):
    count=0
    for i in range(len(words)):
        temp=[]
        word=words[i]
        for j in range(len(word)):
            if ((word[j] in temp)and(word[j-1]!=word[j])):
                break
            else:
                temp.append(word[j])
            if (j==(len(word)-1)):
                count+=1
    return count


wlist=get_input()
count=check_word(wlist)
print(count)
    