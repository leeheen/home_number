N = int(input())
honeys = list(map(int,input().split()))
answers = []
dp = [0 for _ in range(N+1)]
dp[0] = honeys[0]
for i in range(1,N):
    dp[i] += honeys[i]+dp[i-1]
dp_reverse = [0 for _ in range(N+1)]
dp_reverse[0] = honeys[N-1]
j = N-2
for i in range(1,N):
    dp_reverse[i] += honeys[j]+dp_reverse[i-1]
    j -= 1
for i in range(1,N-1):
    answers.append((dp[i]-dp[0])+(dp_reverse[N-1-i]-dp_reverse[0]))
for i in range(1,N-1):
    answers.append((dp[N-1]-dp[i])+(dp[N-1]-dp[0]-honeys[i]))
for i in range(1,N-1):
    answers.append((dp_reverse[N-1]-dp_reverse[0]-honeys[N-1-i])+(dp_reverse[N-1]-dp_reverse[i]))
print(answers)