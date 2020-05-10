a,b,c,k = map(int,input().split())
ans = 0

if a >= k:
    ans = k
else:
    if a + b >= k:
        ans = a
    else:
        ans = a - (k- a- b)

print(ans)

