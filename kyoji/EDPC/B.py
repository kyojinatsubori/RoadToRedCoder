n,k=map(int,input().split())
h=list(map(int,input().split()))
dp=[float('inf')]*n
dp[0]=0
for i in range(0,n):
    for j in range(i+1,min(i+k+1,n)):
        dp[j]=min(dp[i]+abs(h[i]-h[j]),dp[j])
print(dp[n-1])