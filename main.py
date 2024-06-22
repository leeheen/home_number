# import sys
# input = sys.stdin.readline
cnt = 0
N = int(input())
li = []
answers = []
visited = [[False for _ in range(N)]for _ in range(N)]
dx = [0,1,-1,0]
dy = [1,0,0,-1]
def find_d(row,col):
    print(row,col)
    global cnt
    cnt += 1
    visited[row][col]=True
    for i in range(4):
        nRow = row+dx[i]
        nCol = col+dy[i]
        if 0<=nRow<N and  0<=nCol<N:
            if not visited[nRow][nCol]:
                if li[nRow][nCol]=='1':
                    find_d(nRow,nCol)
for i in range(N):
    li.append(list(input()))
for i in range(N):
    for j in range(N):
      if li[i][j]=='1' and visited[i][j]==False:
        find_d(i,j)
        answers.append(cnt)
        cnt = 0
print(len(answers))
answers.sort()
for i in range(len(answers)):
    print(answers[i])
print("hello world")