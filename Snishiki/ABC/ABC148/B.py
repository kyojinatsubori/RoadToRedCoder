N = int(input())
s,t = map(str,input().split())
ans = ""
for i in range(N):
    ans += s[i]
    ans += t[i]
print(ans)
