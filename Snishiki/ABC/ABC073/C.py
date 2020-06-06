from collections import Counter
N = int(input())
A = []
ans = 0
for i in range(N):
    A.append(int(input()))

c = Counter(A)
v = list(c.values())
for i in v:
    if i % 2 == 1:
        ans += 1
print(ans)

