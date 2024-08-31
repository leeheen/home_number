n,m = map(int,input().split())
parents = [i for i in range(n+1)]
change = 0
def MakeSet(a,b):
    a = Find(a)
    b = Find(b)
    if a>b:
        parents[b]=a
    else:
        parents[a]=b
def Find(node):
    if parents[node] == node:
        return node
    parents[node] = Find(parents[node])
    return parents[node]
for i in range(m):
    order,a,b = map(int,input().split())
    if order == 0:
        MakeSet(a,b)
    if order == 1:
        Find(a)
        Find(b)
        if parents[a] == parents[b]:
            print('YES')
        else:
            print('NO')