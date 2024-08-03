n,k = map(int,input().split())
degree = list(map(int,input().split()))
mid = 0
hap = 0
for i in range(k):
    hap += degree[i]
answer = hap
while mid < n-k:
    hap -= degree[mid]
    hap += degree[mid+k]
    if answer < hap:
        answer = hap
    mid += 1
print(answer)
