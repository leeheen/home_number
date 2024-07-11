import sys
sys.setrecursionlimit(10**6)
n,k = map(int,input().split())
cnt = 0
def f(idx,chair):
    global cnt
    if idx == n and chair == k:
        cnt += 1
        return
    if idx >= n or chair > k:
        return
    f(idx+1,chair)
    f(idx+1,chair+1)
f(0,0)
print(cnt)