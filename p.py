import math
N = int(input())
specimens = list(map(int,input().split()))
specimens.sort()
left = 0
right = N-1
values = [specimens[left],specimens[right]]
while left < right:
    if abs(specimens[left+1] + specimens[right]) < abs(specimens[left] + specimens[right-1]):
        left += 1
        if left < right and abs(sum(values))>=abs(specimens[left]+specimens[right]):
            values[0] = specimens[left]
            values[1] = specimens[right]
    elif left < right and abs(specimens[left] + specimens[right-1]) < abs(specimens[left+1] + specimens[right]):
        right -= 1
        if left < right and abs(sum(values))>=abs(specimens[left]+specimens[right]):
            values[0] = specimens[left]
            values[1] = specimens[right]
    else:
        left += 1
        right -= 1
print(*values)