N = int(input())
num = list(input(""))
class stack:
    def __init__(self):
        self.box = [0 for _ in range(N)]
        self.top = -1
    def push(self,data):
        self.top += 1
        self.box[self.top] = data
    def pop(self):
        RT = self.box[self.top]
        self.top -= 1
        return RT
    def size(self):
        return self.top + 1
answer = ""
check = 0
STACK = stack()
for i in num:
    STACK.push(i)
while STACK.size() != 0:
    if check == 3:
        check = 0
        answer += ","
    answer += STACK.pop()
    check += 1
print(answer[::-1])