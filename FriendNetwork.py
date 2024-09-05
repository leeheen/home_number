import sys
input = sys.stdin.readline
N = int(input())
def union(a,b):
    a = Find(a)
    b = Find(b)
    if a==b:
        return friend_cnt[a]
    if a<b:
        friends[b] = a
        friend_cnt[a] += friend_cnt[b]
        return friend_cnt[a]
    else:
        friends[a] = b
        friend_cnt[b] += friend_cnt[a]
        return friend_cnt[b]
def Find(node):
    if node == friends[node]:
        return node
    friends[node] = Find(friends[node])
    return friends[node]
for i in range(N):
    friends = {}
    friend_cnt = {}
    F = int(input())
    for j in range(F):
        f1,f2 = input().split()
        if f1 not in friends.keys():
            friends[f1] = f1
            friend_cnt[f1] = 1
        else:
            Find(f1)
        if f2 not in friends.keys():
            friends[f2] = f2
            friend_cnt[f2] = 1
        else:
            Find(f2)
        cnt = union(f1,f2)
        print(cnt)