n,wmax=map(int,input().split())
v=[0]*n
w=[0]*n
for i in range(n):
    w[i],v[i]=list(map(int,input().split()))
sv=sum(v)+1
dp=[[float('inf')]*sv for _ in range(n)]
dp[0][v[0]-1]=w[0]
for i in range(n):
    dp[i][0]=0
for i in range(n):
    for j in range(sv):
        dp[i][j]=min(dp[i-1][j],dp[i-1][j-v[i]]+w[i])
ans=float('inf')
for p in range(sv-1,-1,-1):
    if dp[n-1][p]<=wmax:
        ans=p
        break
print(ans)