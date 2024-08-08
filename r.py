N,S = map(int,input().split())
nums = list(map(int,input().split()))
answer = 100001
left = -1
right = -1
hap = 0
check = 0
while right < N:
    if hap < S:
        right += 1
        if right < N:
            hap += nums[right]
    if hap >= S:
        if right - left < answer:
            answer = right - left
        check = 1
        left += 1
        if left < N:
            hap -= nums[left]
if check:
    print(answer)
else:
    print(0)