#SCC
import sys
sys.setrecursionlimit(10**6)
v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
ids = [-1 for i in range(v+1)] #방문 기록
finished=[False for i in range(v+1)] #SCC 형성
SCC=[]
id=1
stack=[]
for i in range(e):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
def dfs(node):
    global id
    ids[node]=id
    ret=id
    id+=1
    stack.append(node)
    for next in graph[node]:
        if ids[next]==-1: # 탐색이 되지 않은 경우
            ret=min(ret,dfs(next)) # 현 id값 또는 다음 노드의 값 중 작은것으로 ret설정
        elif finished[next]==False: #탐색되었지만, 아직 scc를 형성하지 못한 경우
            ret=min(ret,ids[next]) # 현 id값과 전 id값중 작은 값으로 변경
    if ids[node]==ret: # 현 id값이 나올때까지 탐색
        scc=[]
        while stack: # SCC 형성
            temp=stack.pop()
            scc.append(temp)
            finished[temp]=True
            if temp==node:
                break
        scc.sort() #작은 값을 기준으로 SCC정렬
        SCC.append(scc)
    return ret
for i in range(1,v+1):
    if ids[i]==-1:
        dfs(i)
SCC.sort()
print(len(SCC)) # 슌환 개수
for i in SCC:
    print(*i,-1)
