from collections import deque
f,s,g,u,d = map(int,input().split())
building = [-1 for _ in range(f+1)]
visited = [False for _ in range(f+1)]
que = deque()
que.append(s)
visited[s] = True
building[s] = 0
while que:
    floor = que.popleft()
    if floor + u <= f:
        if not visited[floor+u]:
            que.append(floor+u)
            building[floor+u] = building[floor] + 1
            visited[floor+u] = True
    if floor - d > 0:
        if not visited[floor-d]:
            que.append(floor-d)
            building[floor-d] = building[floor] + 1
            visited[floor-d] = True
if building[g] != -1:
    print(building[g])
else:
    print('use the stairs')