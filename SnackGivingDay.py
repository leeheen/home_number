N = int(input())
line = list(map(int,input().split()))
stay = []
num = 1
for i in line:
    if i == num:
        num += 1
        while stay and num == stay[-1]:
            stay.pop()
            num += 1
    else:
        stay.append(i)

if num == N+1:
    print('Nice')
else:
    print('Sad')