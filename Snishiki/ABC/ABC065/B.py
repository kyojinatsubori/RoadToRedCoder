N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
ans = 0
light = 0
for i in range(10**6):
    light = a[light]-1
    ans += 1
    if light == 1:
        print(ans)
        exit()
print(-1)