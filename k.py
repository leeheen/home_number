T = int(input())
answer = [0,0,0]
if T % 300 != 0 and T % 60 != 0 and T % 10 != 0:
    print(-1)
else:
    while T != 0:
        if 10 <= T < 60:
            answer[2] += T // 10
            T %= 10
        elif 60 <= T < 300:
            answer[1] += T // 60
            T %= 60
        else:
            answer[0] += T // 300
            T %= 300
    print(*answer)