import heapq
v,e = map(int,input().split())
que = []
li = [[]for _ in range(v+1)]
degree = [0 for _ in range(v+1)]
answers = []
for i in range(e):
    node1,node2 = map(int,input().split())
    li[node1].append(node2)
    degree[node2]+=1

for i in range(1,v+1):
    if degree[i] == 0:
        heapq.heappush(que,i)
check = 0
cnt = 0
while que:
    node = heapq.heappop(que)
    answers.append(node)
    cnt += 1
    for next in li[node]:
        degree[next] -= 1
        if degree[next] < 0:
            check = 1
            break
        if degree[next] == 0:
            heapq.heappush(que,next)
    if check:
        break
if check or cnt != v:
    print(-1)
else:
    for i in answers:
        print(i)