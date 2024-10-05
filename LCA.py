import sys
sys.setrecursionlimit(10**6)
T = int(input())
def dfs(node):
    visited[node] = True
    if len(graph[node]) == 0:
        return
    for next in graph[node]:
        if not visited[next]:
            depth[next] = depth[node]+1
            dfs(next)
def lca(n1,n2):
    if n1 == n2:
        return n1
    if depth[n2] > depth[n1]:
        n1,n2 = n2,n1
    #n1 더 깊은 상태
    while depth[n1]>depth[n2]:
        n1=parent[n1]
    if n1==n2:
        return n1
    else:
        while n1 != n2:
            n1 = parent[n1]
            n2 = parent[n2]
        return n1
for _ in range(T):
    N = int(input())
    parent = [0 for _ in range(N+1)]
    depth = [1 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for i in range(N-1):
        n1,n2 = map(int,input().split())
        parent[n2] = n1
        graph[n1].append(n2)
    root = 1
    for i in range(1,N+1):
        if parent[i] == 0:
            root = i
            break
    dfs(root)
    n1,n2 = map(int,input().split())
    print(lca(n1,n2))