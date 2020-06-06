N,M,Q = map(int,input().split())
S = []
score = [[] for _ in range(N)]  
point = [N]*M
for i in range(Q):
    S.append(list(map(int,input().split())))

for s in S:
    if s[0] == 1:
        ans = 0
        for i in score[s[1]-1]:
            ans += point[i]
        print(ans)
    else:
        score[s[1]-1].append(s[2]-1)
        point[s[2]-1] -= 1
