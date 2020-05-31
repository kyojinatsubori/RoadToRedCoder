N = int(input())
A = list(map(int,input().split()))
ans = 1
for i in A:
    ans = ans * i

if ans > 10**18:
    print(-1)
else:
    print(ans)