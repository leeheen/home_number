board = [0 for _ in range(9)]
zero = []
checks=True
for i in range(9):
    board[i] = list(map(int,input().split()))
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i,j])
def check(row,col):
    for i in range(9):
        if i==col:continue
        if board[row][i]==board[row][col]:
            return False
    for i in range(9):
        if i==row:continue
        if board[i][col]==board[row][col]:
            return False
    for i in range(row//3*3,row//3*3+3):
        for j in range(col//3*3,col//3*3+3):
            if i == row and j == col:
                continue
            if board[i][j] == board[row][col]:
                return False
    return True
def sudoku(state):
    global checks
    if state == len(zero):
        checks=False
        for i in range(9):
            for j in range(9):
                print(board[i][j],end=" ")
            print("")
        return
    for i in range(1,10):
        crow = zero[state][0]
        ccol = zero[state][1]
        board[crow][ccol] = i
        if check(crow,ccol):
            sudoku(state+1)
        board[crow][ccol] = 0

sudoku(0)
if checks:
    print('Not Possible')