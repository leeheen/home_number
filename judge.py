n,m = map(int,input().split())
set = [0 for _ in range(n)]
for i in range(n):
    set[i] = int(input())
set.sort()
left = 1
right = set[n-1]*m
answer = set[n-1]*m
while left<=right:
    mid = (left+right) // 2
    num = 0
    for i in set:
        num += mid // i
    if num<m:
        left=mid+1
    else:
        answer=mid
        right=mid-1
print(answer)