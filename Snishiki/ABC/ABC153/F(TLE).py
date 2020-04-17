from collections import deque

N, D, A = map(int, input().split())
XH = [0]*N
count = 0
for i in range(N):
    XH[i] = list(map(int, input().split()))
XH.sort()
XHd = deque(XH)
while len(XHd) > 0:
    if XHd[0][1] > 0:
        for i in range(len(XHd)):
            if XHd[i][0] <= XHd[0][0] + 2* D:
                XHd[i][1] -= A
        count += 1
    else:
        XHd.popleft()
print(count)

