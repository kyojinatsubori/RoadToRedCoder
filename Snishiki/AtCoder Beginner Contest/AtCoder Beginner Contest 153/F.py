N, D, A = map(int, input().split())
XH = [0]*N
count = 0
for i in range(N):
    XH[i] = list(map(int, input().split()))
XH.sort()
while len(XH) > 0:
    if XH[0][1] > 0:
        for i in range(len(XH)):
            if XH[i][0] <= XH[0][0] + 2* D:
                XH[i][1] -= A
        count += 1
    else:
        XH = XH[1::]
print(count)

