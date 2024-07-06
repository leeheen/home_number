n,k = map(int,input().split())
li = list(map(int,input().split()))
answer = n+1
left = 0
right = n - 1
while left<=right:
    mid = (left+right)//2
    if li[mid] < k:
        left = mid+1
    else:
        answer = mid+1
        right = mid-1
print(answer)