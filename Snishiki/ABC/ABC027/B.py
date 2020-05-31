N = int(input())
a = list(map(int,input().split()))
ans = 0
if sum(a)%N == 0:
    count = 1
    base = sum(a)/N
    for i in range(N):
        if a[i]/count == base:
            count = 1
        else:
            count += 1
            ans += 1
            a[i+1] += a[i]
    print(ans)
else:
    print(-1)