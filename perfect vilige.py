N = int(input())
num = list(map(int,input().split()))
num = [0] + num
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dp = [[0,num[i]] for i in range(N+1)]
for _ in range(N-1):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0] += max(dp[i][0],dp[i][1])
            dp[node][1] += dp[i][0]
dfs(1)
print(max(dp[1]))