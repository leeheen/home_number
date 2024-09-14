#플로이드 요법
n,m = map(int,input().split())
INF = 1000000
dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    n1,n2,w = input().split()
    n1 = ord(n1) - 64
    n2 = ord(n2) - 64
    w = int(w)
    dp[n1][n2] = w
    dp[n2][n1] = w

s,e = input().split()
s = ord(s) - 64
e = ord(e) - 64
for i in range(1,n+1):
    dp[i][i] = 0
for port in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            if start == port and end == port:
                continue
            if dp[start][port]+dp[port][end]<dp[start][end]:
                dp[start][end] = dp[start][port] + dp[port][end]
                dp[end][start] = dp[start][port] + dp[port][end]
if dp[s][e] == INF:
    print(-1)
else:
    print(dp[s][e])