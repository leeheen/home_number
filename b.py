n = int(input())
cnt = 0
def binary(one,zero,take):
    global cnt
    if one + zero == n:
        cnt += 1
        return
    if one + zero > n:
        return
    if take == 1:
        binary(one+1,zero,0)
    else:
        binary(one+1,zero,take)
        binary(one,zero+1,take+1)
binary(0,0,0)
print(cnt)
