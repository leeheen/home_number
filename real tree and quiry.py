N,R,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
start = [0 for _ in range(Q)]
dp =[1 for _ in range(N + 1)]

visited = [False for _ in range(N+1)]
answers = []
for i in range(N-1):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(Q):
    start[i] = int(input())
def dfs(p):
    visited[p]=True
    for i in graph[p]:
        if not visited[i]:
            dp[p] += dfs(i)
    return dp[p]
dfs(R)
for i in start:
    answers.append(dp[i])
print(*answers)