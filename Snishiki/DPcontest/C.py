N = int(input())
abc = [0]*N
for i in range(N):
    abc[i] = list(map(int,input().split()))
dp = [0]*N
for i in range(N):
    dp[i] = [0,0,0]
dp[0][0],dp[0][1],dp[0][2]= abc[0][0], abc[0][1], abc[0][2]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + abc[i][0]
    dp[i][1]= max(dp[i-1][0], dp[i-1][2])+ abc[i][1]
    dp[i][2]= max(dp[i-1][1], dp[i-1][0])+ abc[i][2]

print(max(dp[N-1]))
