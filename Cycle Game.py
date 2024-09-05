import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
parents = [i for i in range(n)]
answer = 0
def union(a,b):
    a = Find(a)
    b = Find(b)
    if a<b:
        parents[b] = a
    else:
        parents[a] = b
def Find(node):
    if node == parents[node]:
        return node
    parents[node] = Find(parents[node])
    return parents[node]
for i in range(1,m+1):
    node1,node2 = map(int,input().split())
    if Find(node1) == Find(node2):
        answer = i
        break
    union(node1,node2)
print(answer)