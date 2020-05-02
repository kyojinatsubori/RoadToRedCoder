import copy
N, K  = map(int, input().split())
h = list(map(int,input().split()))
dp = [0]*N

dp[1] = abs(h[0] - h[1]) 
for i in range(2, N):
    min = float('inf')
    if i <= K:
        for j in range(0, i):
            num = dp[j] + abs(h[i]-h[j])
            if min > num:
                min = copy.deepcopy(num)
    else:
        for j in range(i-K, i):
            num = dp[j] + abs(h[i]-h[j])
            if min > num:
                min = copy.deepcopy(num)
    dp[i] = min
print(dp[N-1])
