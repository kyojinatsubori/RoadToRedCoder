import copy
N,Q = map(int,input().split())
S = []
for i in range(Q):
    S.append(list(map(int,input().split())))
ans = [["N"]*N for _ in range(N)]

for i in S:
    if i[0] == 1:
        ans[int(i[1])-1][int(i[2])-1] = "Y"
    elif i[0] == 2:
        a = int(i[1])-1
        for k in range(N):
            if ans[k][a] == "Y":
                ans[a][k] = "Y"
    else:
        a = int(i[1])-1
        al = copy.deepcopy(ans[a])
        for k in range(N):
            if al[k] == "Y":
                for j in range(N):
                    if ans[k][j] == "Y" and j != a:
                        ans[a][j] = "Y"
for i in ans:
    print("".join(i))
