n = int(input())
horizontal = [0 for _ in range(1000000+1)]
vertical = [0 for _ in range(1000000+1)]
o = 500000
prex,prey='x','y'
first_pos = [0,0]
last_pos = [0,0]
for i in range(n):
    x,y = map(int,input().split())
    if i == 0:
        first_pos = [x,y]
    elif i == n-1:
        last_pos = [x,y]
    if prex == 'x' and prey == 'y':
        prex = x
        prey = y
    else:
        if x == prex:
            max_y = max(y,prey)
            min_y = min(y,prey)
            horizontal[o+min_y] += 1
            horizontal[o+max_y] += -1
            prey = y
        if y == prey:
            max_x = max(x,prex)
            min_x = min(x,prex)
            vertical[o+min_x] += 1
            vertical[o+max_x] += -1
            prex = x
if first_pos[0] == last_pos[0]:
    max_y = max(first_pos[1],last_pos[1])
    min_y = min(first_pos[1],last_pos[1])
    horizontal[o+min_y] += 1
    horizontal[o+max_y] += -1
if first_pos[1] == last_pos[1]:
    max_x = max(first_pos[0],last_pos[0])
    min_x = min(first_pos[0],last_pos[0])
    vertical[o+min_x] += 1
    vertical[o+max_x] += -1
i = 0
j = 0
while i < 1000000:
    horizontal[i+1] += horizontal[i]
    i += 1
h = max(horizontal)
while j < 1000000:
    vertical[j+1] += vertical[j]
    j += 1
v = max(vertical)
print(max(h,v))