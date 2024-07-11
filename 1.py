n = int(input())
needs = list(map(int,input().split()))
limits = int(input())
needs.sort()
answer = 0
left = 0
right = needs[n-1]
while left <= right:
    mid = (left+right) // 2
    sums = 0
    for i in needs:
        if i < mid:
            sums += i
        else:
            sums += mid
    if sums <= limits:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)