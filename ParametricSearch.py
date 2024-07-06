k,n = map(int,input().split())
line = [0 for _ in range(k)]
for i in range(k):
    line[i] = int(input())
line.sort()
answer = 0
left = 1
right = line[k-1]
while left<=right:
    SUM = 0
    mid = (left+right)//2
    for i in line:
        SUM += i // mid
    if SUM < n:
        right = mid-1
    elif SUM >= n:
        left = mid+1
        if answer < mid:
            answer = mid
print(answer)