import heapq
import sys
input = sys.stdin.readline
n,m,end = map(int,input().split())
graph = [[] for _ in range(n+1)]
que = []
answer = 0
INF = 1000000
for i in range(m):
    n1,n2,w = map(int,input().split())
    graph[n1].append((w,n2))
for start in range(1,n+1):
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0
    if start == end:
        continue
    heapq.heappush(que,(0,start))
    while que:
        weight,node = heapq.heappop(que)
        for w,next in graph[node]:
            if dist[next] > dist[node] + w:
                dist[next] = dist[node] + w
                heapq.heappush(que,(dist[next],next))
    for i in range(1,n+1):
        if i != end:
            dist[i] = INF
    heapq.heappush(que,(0,end))
    while que:
        weight, node = heapq.heappop(que)
        for w, next in graph[node]:
            if dist[next] > dist[node] + w:
                dist[next] = dist[node] + w
                heapq.heappush(que, (dist[next], next))
    if answer < dist[start]:
        answer = dist[start]
print(answer)