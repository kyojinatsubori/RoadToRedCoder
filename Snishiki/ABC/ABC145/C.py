import math
N = int(input())
XY = [0]*N
for i in range(N):
    XY[i] = list(map(int,input().split()))
sum = 0


for i in range(N-1):
    for j in range(i+1, N):
        sum += math.sqrt((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)

ans = sum * 2 / N
print(ans)