s = input()
t = input()
lens = len(s)+1
lent = len(t)+1
dp = [0]*lens
for i in range(lens):
    dp[i] = [0]*lent
dpm = [0]*lens
for i in range(lens):
    dpm[i] = [0]*lent
for i in range(lent):
    dpm[0][i] = [0,i]
for i in range(lens):
    dpm[i][0] = [i, 0]


for i in range(1,lens):
    for j in range(1,lent):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            dpm[i][j] = [i-1, j-1]
        else:
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                dpm[i][j] = [i-1, j]
            else:
                dp[i][j] = dp[i][j-1]
                dpm[i][j] = [i, j-1]

ans = ""
i = lens-1
j = lent-1
while len(ans) != dp[lens-1][lent-1]:
    if i - dpm[i][j][0] == 1 and j - dpm[i][j][1] == 1:
        ans += t[j-1]
    i = dpm[i][j][0]
    j = dpm[i][j][1]

print(dp)
print(dpm)
print(ans)

