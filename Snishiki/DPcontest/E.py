N,W = map(int,input().split())

v = [0] * N
w = [0] * N
for i in range(N):
    w[i],v[i] = map(int,input().split())
sumv = sum(v)+1
dp = [[float('inf')] * (sumv) for _ in range(N+1)]
for i in range(N):
    dp[i][0] = 0
for i in range(1, N+1):
    for j in range(1, sumv):
        if v[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j],w[i-1]+dp[i-1][j-v[i-1]])
ans = 0
for i in range(1, sumv+1):
    if dp[N][-i] <= W:
        ans = sumv - i
        break
print(ans)