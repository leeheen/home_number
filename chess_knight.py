# import sys
# input = sys.stdin.readline
from collections import deque

N = int(input())
knight = list(map(int,input().split()))
knight[0] -= 1
knight[1] -= 1
target = list(map(int,input().split()))
target[0] -= 1
target[1] -= 1
board = [[0 for _ in range(N)]for _ in range(N)]
visited = [[False for _ in range(N)]for _ in range(N)]
que = deque()
que.append(knight)
d = [[2,1],[2,-1],[1,2],[-1,2],[-2,1],[-2,-1],[1,-2],[-1,-2]]
while que:
    row,col = que.popleft()
    visited[row][col] = True
    if row==target[0] and col==target[1]:
        print(board[row][col])
        break
    for i in d:
        nRow = row + i[0]
        nCol = col + i[1]
        if 0<=nRow<N and 0<=nCol<N:
            if not visited[nRow][nCol]:
                if board[nRow][nCol] == 1:
                    break
                board[nRow][nCol]=board[row][col]+1
                que.append([nRow,nCol])
                visited[nRow][nCol] = True
