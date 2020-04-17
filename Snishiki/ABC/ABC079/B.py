N = int(input())
memo = []
for i in range(N+1):
    if i == 0:
        memo.append(2)
    elif i == 1:
        memo.append(1)
    else:
        memo.append(memo[i-1] + memo[i-2])

print(memo[N])
