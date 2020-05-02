from collections import deque
N = int(input())
a = list(map(int,input().split()))
a = deque(a)
count = 0
k = 1
for i in range(N):
    if a[0] != k:
        a.popleft()
        count += 1
    else:
        a.popleft()
        k += 1
if k == 1:
    print(-1)
else:
    print(count)

