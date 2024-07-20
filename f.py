n = int(input())
li = [0 for i in range(n+1)]
def f(x):
    if x == 0:
        return x
    elif x == 1:
        return x
    elif li[x] != 0:
        return li[x]
    else:
        li[x] = f(x-1) + f(x-2)
        return li[x]
answer = f(n)
print(answer)