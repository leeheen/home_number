# import sys
# input = sys.stdin.readline
from collections import deque

N = int(input())
x,y = map(int,input().split())
visited = [[False for _ in range(N)]for _ in range(N)]
mountain = [[0 for _ in range(N)]for _ in range(N)]

def BFS(row,col):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    mountain[row][col] = 1
    que = deque()
    que.append([row,col])
    visited[row][col] = True
    while que:
        Row,Col = que.popleft()
        for i in range(4):
            nRow = Row + dx[i]
            nCol = Col + dy[i]
            if 0<=nRow<N and 0<=nCol<N:
                if not visited[nRow][nCol]:
                    visited[nRow][nCol] = True
                    que.append([nRow,nCol])
                    mountain[nRow][nCol] = mountain[Row][Col]+1
BFS(x-1,y-1)
for i in mountain:
    for j in i:
        print(j,end=" ")
    print("")