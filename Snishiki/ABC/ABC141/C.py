N ,K , Q = map(int,input().split())
Life = [0]*N
for i in range(Q):
    a = int(input())
    Life[a-1] += 1

for i in range(N):
    if Life[i] <= Q


