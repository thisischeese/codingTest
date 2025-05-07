import sys 


expression = list(sys.stdin.readline().split('-'))
new_expression = [0 for _ in range(len(expression))]

for t in range(len(expression)):
    token = expression[t]
    if "+" in token:
        temp = ''
        for i in range(len(token)):
            if token[i]!="+":
                temp+=token[i]
            else:
                new_expression[t] += int(temp)
                temp = ''
            if i == (len(token)-1):
                new_expression[t] += int(temp)
    else:
        new_expression[t] = int(expression[t])
        
for i in range(len(new_expression)):
    if i ==0:
        answer = new_expression[i]
    else:
        answer -= new_expression[i]
    
print(answer)