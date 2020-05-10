def memo(x):
    if dp[x-1]:
        return dp[x-1]
    else:
        dp[x-1]=memo(y-1)+1
        return dp[x-1]

n,m=map(int,input().split())
xy=[[0,0] for i in range(m)]
for i in range(m):
    xy[i][0],xy[i][1]=map(int,input().split())
dp=[0]*n
for i in range(m):
    x=xy[i][0]
    y=xy[i][1]
    print(dp)
    print(x)
    print(y)
    memo(x)
print(max(dp))