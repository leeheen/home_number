import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
visited = [False for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
dp = [[0,0] for _ in range(N+1)]
for i in range(N-1):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
def dfs(node):
    dp[node][0] = 0
    dp[node][1] = 1
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0] += dp[i][1]
            dp[node][1] += min(dp[i][0],dp[i][1])
dfs(1)
print(min(dp[1]))