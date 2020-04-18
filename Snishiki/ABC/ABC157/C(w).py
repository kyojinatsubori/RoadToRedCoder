N,M = map(int,input().split())
sc = [0]*M
for i in range(M):
    sc[i] = list(map(int, input().split()))
ans = [0]*N
l = []
ansa = ""

if M == 0:
    if N > 1:
        ansa = "1"
        for i in range(N-1):
            ansa += "0"
        print(ansa)
        exit()
    else:
        print(0)
        exit()

for s, c in sc:
    if s == 1 and c == 0 and N > 1:
        print("-1")
        exit()
    if s in l and ans[s-1] != c:
        print("-1")
        exit()
    if len(ans) >= s:
        ans[s-1] = c
        l.append(s)
    else:
        print("-1")
        exit()

if 0 == ans[0]:
    ans[0] = 1

print(''.join(map(str,ans)))
