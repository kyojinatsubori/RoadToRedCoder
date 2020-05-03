N ,K = map(int,input().split())
NL = [0]*N
for i in range(K):
    K = input()
    AL = list(map(int,input().split()))
    for j in AL:
        NL[j-1] += 1
ans = 0
for i in NL:
    if i == 0:
        ans += 1
print(ans)
