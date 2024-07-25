T = int(input())
N = []
answers = []
def triangle(n):
    global memo
    if n <= 3:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = triangle(n-3) + triangle(n-2)
    return memo[n]
for i in range(T):
    x = int(input())
    memo = [0 for _ in range(x+1)]
    answers.append(triangle(x))
for i in range(T):
    print(answers[i])