n,m = map(int,input().split())
visited = [[-1 for i in range(m)]for j in range(n)]
candies = []
for i in range(n):
    candies.append(list(map(int,input().split())))
def f(row,col):
    ret = candies[row][col]
    if row == 0 and col == 0:
        return ret
    if visited[row][col] == -1:
        if row==0:
            ret+=f(row,col-1)
            visited[row][col] = ret
        elif col==0:
            ret+=f(row-1,col)
            visited[row][col] = ret
        else:
            ret+=max(f(row-1,col),f(row,col-1))
            visited[row][col] = ret
    else:
        return visited[row][col]
    return ret
print(f(n-1,m-1))