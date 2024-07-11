n = int(input())
cnt = 0
def stair(walk,rest):
    global cnt
    if walk == n:
        cnt += 1
        return
    if walk > n:
        return
    if rest > 0:
        stair(walk+1,rest-1)
        stair(walk+2,rest-1)
    else:
        stair(walk+1,rest)
        stair(walk+2,rest)
        stair(walk+3,rest+2)
stair(0,0)
print(cnt)