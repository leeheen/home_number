import math
import sys
input = sys.stdin.readline
N = int(input())
dataset = []
answer = 401
team = [0 for _ in range(N)]
for i in range(N):
    dataset.append(list(map(int,input().split())))
def f(idx):
    global answer
    point1 = 0
    point2 = 0
    if idx == N or sum(team) == N//2:
        for i in range(N):
            for j in range(N):
                if i != j:
                    if team[i] == 1 and team[j] == 1:
                        point1 += dataset[i][j]
                    elif team[i] == 0 and team[j] == 0:
                        point2 += dataset[i][j]
        if answer > abs(point1-point2):
            answer = abs(point1-point2)
        return
    for i in range(idx+1,N):
        if team[i] == 0:
            team[i] = 1
            f(i)
        team[i] = 0
f(-1)
print(answer)