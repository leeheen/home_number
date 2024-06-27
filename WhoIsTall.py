# import sys
# input = sys.stdin.readline
from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
checkT = [0 for _ in range(N+1)]
checkS = [0 for _ in range(N+1)]
answer = 0
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
que = deque()
for i in range(1,N+1):
    que.append(i)
    visited1 = [0 for _ in range(N+1)]
    while que:
        n = que.popleft()
        visited1[n] = True
        for j in graph[n]:
            if not visited1[j]:
                que.append(j)
                checkT[i] += 1
                checkS[j] += 1
                visited1[j] = True
for i in range(1,N+1):
    if checkT[i] + checkS[i] == N-1:
        answer += 1
print(answer)