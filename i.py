N = int(input())
triangle = [[0 for _ in range(N+1)]for _ in range(N+1)]
i = 0
j = 0
k = 0
triangle[0][0] = 1
while i < N+1:
    for n in range(1,j+1):
        for r in range(1,k+1):
            triangle[n][r] = triangle[n-1][r] + triangle[n-1][r-1]
    i += 1
    j += 1
    k += 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(triangle[i][j],end=" ")
    print()