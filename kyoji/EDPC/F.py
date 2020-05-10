s=input()
t=input()
ls=len(s)+1
lt=len(t)+1
dp=[[0]*lt for _ in range(ls)]
for i in range(1,ls):
    for j in range(1,lt):
        if s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
ans=""
i=ls-1
j=lt-1
while i>0 and j>0:
    if dp[i][j]==dp[i-1][j]:
        i-=1
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    else:
        ans = s[i-1] + ans
        i-=1
        j-=1
print(ans)