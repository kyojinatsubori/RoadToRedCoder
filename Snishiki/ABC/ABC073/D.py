import itertools
N,M,R = map(int,input().split())
r = list(map(int,input().split()))
p = list(itertools.permutations(r))
dp = [[float('inf')]*N for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
ans = float('inf')
for v in p:
    temp = 0
    for i in range(len(v)-1):
        temp += dp[v[i]-1][v[i+1]-1]
    ans = min(ans,temp)

print(ans)