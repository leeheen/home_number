n,k = map(int,input().split())
cnt = 0
def f(idx,chair,sat):
    global cnt
    if idx == n and chair == k:
        cnt += 1
        return
    if idx >= n or chair > k:
        return
    if sat == 1:
        f(idx+1,chair,0)
    else:
        f(idx + 1, chair, sat)
        f(idx+1,chair+1,sat+1)
f(0,0,0)
print(cnt)