# 辞書型初めて使った
# AtCoderのPython3.4では辞書型の順番が固定されないらしい（無能）
# なのでKeyで出力しましょう
from collections import deque
N = int(input())
ab = {}
abl = []
path = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)
    abl.append((a-1,b-1))
    ab[(a-1,b-1)] = 0
color = [0]*N
color[0] = -1
q = deque([])
q.append(0)
max = 0

while len(q)>0:
    cn = q.popleft()
    ccolor = color[cn]
    ncolor = 1
    for i in path[cn]:
        if color[i] == 0:
            if ccolor != ncolor:
                color[i] = ncolor
                ab[(cn,i)] = ncolor
                ncolor += 1
            else:
                color[i] = ncolor+1
                ab[(cn,i)] = ncolor+1
                ncolor += 2
            if color[i] > max:
                max = color[i]
            q.append(i)
print(max)
for i in abl:
    print(ab[i])