# import sys
# input = sys.stdin.readline
answer = 0
temp = 0
N = int(input())
Map = []
for i in range(N):
    li = list(map(int,input().split()))
    Map.append(li)
def safe_sector(row,col):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited1[row][col] = True
    for i in range(4):
        nRow = row + dx[i]
        nCol = col + dy[i]
        if 0<=nRow<N and 0<=nCol<N:
            if not visited1[nRow][nCol] and 0 == ruined1[nRow][nCol]:
                safe_sector(nRow,nCol)
for i in range(100+1):
    depth = i
    visited1 = [[False for _ in range(N)] for _ in range(N)]
    ruined1 = [[0 for _ in range(N)]for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if Map[j][k] <= depth:
                ruined1[j][k] = 1
    for j in range(N):
        for k in range(N):
            if ruined1[j][k] != 1 and visited1[j][k] == False:
                safe_sector(j,k)
                temp += 1
    if temp > answer:
        answer = temp
    temp = 0
print(answer)
