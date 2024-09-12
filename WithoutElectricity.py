import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]
def union(node1,node2):
    node1 = find(node1)
    node2 = find(node2)
    if node1 > node2:
        parents[node2] = node1
    else:
        parents[node1] = node2
while True:
    m,n = map(int,input().split())
    if m==n==0:
        break
    graph = []
    parents = [i for i in range(m)]
    answer = 0
    for i in range(n):
        node1,node2,weight = map(int,input().split())
        answer += weight
        graph.append((weight,node1,node2))
    graph.sort()
    for i in range(n):
        w,n1,n2 = graph[i]
        if find(n1) != find(n2):
            union(n1,n2)
            answer -= w
    print(answer)