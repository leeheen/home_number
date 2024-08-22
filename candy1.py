N = int(input())
board = [0 for _ in range(N)]
visited = [False for _ in range(N)]
for i in range(N):
    li = list(map(int,input().split()))
    board[i] = li
answer = 0
def solution(row,candy):
    global answer
    if row == N and candy > answer:
        answer = candy
        return
    if row >= N:
        return
    for col in range(N):
        if visited[col] == False:
            visited[col] = True
            solution(row+1,candy+board[row][col])
            visited[col] = False
solution(0,0)
print(answer)