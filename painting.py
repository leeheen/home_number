# import sys
# input = sys.stdin.readline
board = []
visited = [[False for _ in range(10)]for _ in range(10)]
for i in range(10):
    li = list(input())
    board.append(li)
x,y = map(int,input().split())
def fill(row,col):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[row][col] = True
    board[row][col] = "*"
    for i in range(4):
        nRow = row + dx[i]
        nCol = col + dy[i]
        if 0<=nRow<10 and 0<=nCol<10:
            if not visited[nRow][nCol] and board[nRow][nCol] != "*":
                fill(nRow,nCol)
if board[y][x] != "*":
    fill(y,x)
for i in range(10):
    for j in range(10):
        print(board[i][j],end="")
    print("\n")