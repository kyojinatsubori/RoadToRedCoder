n=int(input())
act=[0]*n
for i in range(n):
    act[i]=list(map(int,input().split()))
dp=[[0]*3 for _ in range(n)]
dp[0]=[act[0][0],act[0][1],act[0][2]]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][1],dp[i-1][2])+act[i][0]
    dp[i][1]=max(dp[i-1][2],dp[i-1][0])+act[i][1]
    dp[i][2]=max(dp[i-1][0],dp[i-1][1])+act[i][2]
print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))