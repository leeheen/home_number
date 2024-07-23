H = int(input())
dp = [1] + [0 for _ in range(H)]
for i in range(H):
    if i%2 == 0:
        dp[i+1] = dp[i] * 2 - 1
    else:
        dp[i+1] = dp[i] * 2 + 1
print(dp[H-1])