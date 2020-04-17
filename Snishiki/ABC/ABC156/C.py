N = int(input())
l = list(map(int, input().split()))
ans = 0
ave = round(sum(l)/N)

for i in l:
    ans += (i-ave)**2

print(ans)