T = int(input())
strings = []
for i in range(T):
    strings.append(input())
for i in strings:
    check = 2
    left = 0
    right = len(i) - 1
    if i[::-1] == i:
        print(0)
        continue
    else:
        while left < right:
            if i[left] != i[right]:
                left_part = i[left+1:right+1]
                right_part = i[left:right]
                if left_part[::-1] == left_part:
                    check = 1
                if right_part[::-1] == right_part:
                    check = 1
                break
            left += 1
            right -= 1
        print(check)