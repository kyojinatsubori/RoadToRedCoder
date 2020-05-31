N = int(input())
evi = [[] for _ in range(N)]
ans = 0
for i in range(N):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        evi[i].append((x,y))

for i in range(1 << N):
    count = 0
    flag = True
    for j in range(N):
        if (i >> j) & 1 == 1:
            count += 1
            for x,y in evi[j]:
                if (i >> x-1) & 1 != y:
                    flag = False
                    break
            if flag == False:
                break
    if flag:
        if ans < count:
            ans = count
print(ans)


