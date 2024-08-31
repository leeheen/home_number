from collections import deque
board = [0 for _ in range(100+1)]
visited = [False for _ in range(100+1)]
portal = [[]for _ in range(100+1)]
que = deque()
n,m = map(int,input().split())
for i in range(n):
  l1,l2 = map(int,input().split())
  portal[l1].append(l2)
for j in range(m):
    s1,s2 = map(int,input().split())
    portal[s1].append(s2)
que.append(1)
visited[1] = True
while que:
  block = que.popleft()
  for i in range(1,6+1):
    if block+i <= 100:
        if not visited[block+i]:
            board[block+i] = board[block]+1
            if portal[block+i]:
                if not visited[portal[block+i][0]]:
                    board[portal[block+i][0]] = board[block+i]
                    visited[portal[block+i][0]] = True
                    que.append(portal[block+i][0])
                visited[block+i] = True
            else:
                visited[block+i] = True
                que.append(block+i)
print(board[100])