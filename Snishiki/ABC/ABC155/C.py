import collections as col
N = int(input())
l = [0]*N
for i in range(N):
    l[i] = input()
ans = []

counter = col.Counter(l)
common = counter.most_common()
ans = []
ans.append(common[0][0])

for i in range(len(common)-1):
    if common[i][1] == common[i+1][1]:
        ans.append(common[i+1][0])
        i += 1
    else:
        break

ans.sort()
for i in range(len(ans)):
    print(ans[i])

