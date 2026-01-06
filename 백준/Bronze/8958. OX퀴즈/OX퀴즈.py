import sys 
input = sys.stdin.readline 


test_cases = int(input())
answers = [0 for _ in range(test_cases)]

for t in range(test_cases):
    answer = 0 
    problems = list(input().strip())
    for i in range(len(problems)):
        p = problems[i]
        if p=='O':
            problems[i] = 1
            if(i!=0): problems[i] += problems[i-1] 
        else:
            problems[i] = 0 

    for p in problems:
        answers[t] += p 

for ans in answers:
    print(ans)    

