#최단 경로 알고리즘(다익스트라)
import heapq
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
INF = 1000000
dist = [INF for _ in range(n)]
graph=[[] for i in range(n+1)]
que = []
for i in range(m):
    n1,n2,w = input().split()
    n1 = ord(n1) - 65
    n2 = ord(n2) - 65
    w = int(w)
    graph[n1].append((w, n2))
    graph[n2].append((w, n1))

start,end = map(ord,input().split())
start -= 65
end -= 65
dist[start] = 0
heapq.heappush(que,(0,start))
while que:
    weight,node = heapq.heappop(que)
    for w,next in graph[node]:
        if dist[node] + w < dist[next]:
            dist[next] = dist[node] + w
            heapq.heappush(que,(dist[next],next))

if dist[end] == INF:
    print(-1)
else:
    print(dist[end])