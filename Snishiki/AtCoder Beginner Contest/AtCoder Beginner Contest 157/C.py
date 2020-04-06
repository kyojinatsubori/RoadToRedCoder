N,M = map(int,input().split())
sc = [0]*M
for i in range(M):
    sc[i] = list(map(int, input().split()))
ans = [0]*N
l = []

for s, c in sc:
    if s in l:
        print("-1")
        exit()
    ans[-s] = c
    l.append(s)

if 0 in ans[0:N:] 