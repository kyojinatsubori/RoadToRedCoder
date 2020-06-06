a,b = map(int,input().split())
first = 1
ans = 0
while first < b:
    first += a-1
    ans += 1
print(ans)