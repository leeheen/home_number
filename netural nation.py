n,m = map(int,input().split())
parents = [ _ for _ in range(n+1)]



def find(node):
    if parents[node]==node:
        return node
    parents[node]=find(parents[node])
    return parents[node]

def union(n1,n2):
    n1=find(n1)
    n2=find(n2)
    if n1>n2:
        parents[n1]=n2
    else:
        parents[n2]=n1


for i in range(m):
    node1,node2=map(int,input().split())
    union(node1,node2)

for i in range(1,n+1):
    print(find(i),end=' ')
