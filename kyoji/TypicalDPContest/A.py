n=int(input())
p=list(map(int,input().split()))
maximum=sum(p)
dp=[[False]*(maximum+1) for _ in range(n+1)]
dp[0][0]=True
for i in range(1,n+1):
    for j in range(0,maximum+1):
        if dp[i-1][j]:
            dp[i][j]=True
        elif dp[i-1][j-p[i-1]]:
            dp[i][j]=True
        else:
            dp[i][j]=False
print(dp[n].count(True))