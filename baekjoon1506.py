#백준 온라인 저지 1506 경찰서

n = int(input())
cost = list(map(int,input().split())) #경찰서 비용
city = [[0 for _ in range(n+1)]] #도로 상태
scc = []
IS = [False for _ in range(n+1)]
finished = [False for _ in range(n+1)]
graph=[[]for _ in range(n+1)]
stack = []
id = 1
for i in range(n):
    li = [0]+list(map(int,input()))
    city.append(li)
for i in range(1,n+1):
    for j in range(1,n+1):
        if city[i][j] == 1: #도로를 갈 수 있는 경우(간선이 존재하는 경우)
            graph[i].append(j)
def dfs(node):
    global id
    IS[node] = id
    id += 1
    ret = IS[node]
    stack.append(node)
    for next in graph[node]:
        if IS[next] == False:
            ret = min(ret,dfs(next))
        elif finished[next] == False:
            ret = min(ret,IS[next])
    if ret == IS[node]: #만일 그래프가 순환을 이룬 경우
        li = []
        while stack:
            temp = stack.pop()
            li.append(temp)
            finished[temp] = True #SCC 형성
            if temp == node:
                break
        if li:
            scc.append(li) #SCC를 한 노드의 형태로 저장
    return ret
for i in range(1,n+1): #모든 경로를 탐색
    if IS[i] == False:
        dfs(i)
answer = 0
for i in scc: #강하게 연결된 경찰서들을 포함하여 최소 가격 구하기
    temp = 10**6+1
    for j in i:
        if temp > cost[j-1]:
            temp = cost[j-1]
    answer += temp
print(answer)