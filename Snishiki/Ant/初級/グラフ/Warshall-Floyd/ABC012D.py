N,M = map(int,input().split())
dp = [[float('inf')]*N for _ in range(N)]
for i in range(M):
    a,b,t  = map(int,input().split())
    dp[a-1][b-1] =t
    dp[b-1][a-1] =t
for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

fmax = float('inf')
for i in range(N):
    nmax = max(dp[i])
    if fmax > nmax:
        fmax = nmax
print(fmax)
