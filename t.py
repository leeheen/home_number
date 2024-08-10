N,H = map(int,input().split())
top_dp = [0 for _ in range(H+1)]
bottom_dp = [0 for _ in range(H+1)]
answers = []
for i in range(N):
    stone = int(input())
    if i % 2 == 0:
        bottom_dp[stone]+=1
    else:
        top_dp[stone]+=1

for i in range(H-1,0,-1):
    bottom_dp[i]+=bottom_dp[i+1]
    top_dp[i]+=top_dp[i+1]
i = 1
j = H
while i <= H:
    answers.append(top_dp[j]+bottom_dp[i])
    i += 1
    j -= 1
print(min(answers),answers.count(min(answers)))