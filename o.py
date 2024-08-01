N = int(input())
room = [[0 for _ in range(N+1)]]
for i in range(N):
    room.append([0]+list(map(int,input().split())))
dp = [[[0,0,0] for _ in range(N+1)]for _ in range(N+1)]
rotate = [0,1,2]
dp[1][2][0] = 1
for row in range(1,N+1):
    for col in range(3,N+1):
        for i in rotate:
            if i == 0:
                if room[row][col] != 1:
                    dp[row][col][0] += dp[row][col-1][0] + dp[row][col-1][1]
            if i == 1:
                if room[row-1][col] != 1 and room[row][col-1] != 1 and room[row][col] != 1:
                    dp[row][col][1] += dp[row-1][col-1][0] + dp[row-1][col-1][1] + dp[row-1][col-1][2]
            if i == 2:
                if room[row][col] != 1:
                    dp[row][col][2] += dp[row-1][col][1] + dp[row-1][col][2]
print(sum(dp[N][N]))