N, M = map(int,input().split())
H = list(map(int,input().split()))
AB = [0]*M
for i in range(M):
    AB[i] = list(map(int,input().split()))

GD = [0]*N

for A ,B in AB:
    HA = H[A-1]
    HB = H[B-1]
    if HA < HB:
        GD[A-1] -= 1
    elif HA > HB:
        GD[B-1] -= 1
    else:
        GD[A-1] -= 1
        GD[B-1] -= 1

ans = 0
for i in GD:
    if i == 0:
        ans += 1
print(ans)


    