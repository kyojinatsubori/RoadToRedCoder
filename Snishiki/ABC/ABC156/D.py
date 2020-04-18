n,a,b = map(int,input().split())
ans = 0

for i in range(1 << n):
    for j in range(n):
        count = 0
        if (i >> j) & 1 ==1:
            count += 1
    if count != a and count != b:
        ans += 1
print((ans-1)%(10**9+7))


# 全部０引く
