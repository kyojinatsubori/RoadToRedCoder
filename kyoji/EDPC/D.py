n,maxw=map(int,input().split())
nap=[0]*n
for i in range(n):
    nap[i]=list(map(int,input().split()))
dp=[[0]*(maxw+1) for _ in range(n)]
for i in range(n):
    for j in range(maxw+1):
        if nap[i][0]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-nap[i][0]]+nap[i][1])
print(dp[n-1][maxw])