import copy
n,m,x = map(int,input().split())
ca = [0]*n
for i in range(n):
    ca[i] = list(map(int,input().split()))
ans = 10**8

for i in range(1 << n):
    sum = 0
    result = [0]*m
    for j in range(n):
        if (i >> j) & 1 == 1:
            for k in range(m):
                result[k] += ca[j][k+1]
            sum += ca[j][0]
    if min(result) >= x and ans > sum:
        ans = copy.deepcopy(sum)

if ans == 10**8:
    print(-1)
else:
    print(ans)