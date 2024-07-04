setting = list(input())
stack = []
answer = 0
i = 0
while i < len(setting):
    if setting[i] == "(" and setting[i+1] == "(":
        stack.append('(')
        i += 1
    elif setting[i] == "(" and setting[i+1] == ")":
        answer += len(stack)
        i += 2
    elif setting[i] == ")":
        stack.pop(-1)
        answer += 1
        i += 1
print(answer)