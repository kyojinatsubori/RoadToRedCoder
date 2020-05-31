# プリム法
# 愚直にやるとO(N**2)
import heapq
N = int(input())
townX = []
townY = []
for i in range(N):
    x,y = map(int,input().split())
    townX.append((x-1, i))
    townY.append((y-1, i))
townX.sort()
townY.sort()
edge = [[] for i in range(N)]
for i in range(N-1):
    x, nowTown = townX[i]
    xx, nextTown = townX[i+1]
    edge[nowTown].append((xx-x, nextTown))
    edge[nextTown].append((xx-x, nowTown))
for i in range(N-1):
    y, nowTown = townY[i]
    yy, nextTown = townY[i+1]
    edge[nowTown].append((yy-y, nextTown))
    edge[nextTown].append((yy-y, nowTown))
q = []
used = [0]*N
used[0] = 1
ans = 0
# 頂点どれでもいいので根を0とする
# ダイクストラやプリムではheapqを使用するので、取り合えず枝全部入れてよし
for i in edge[0]:
    heapq.heappush(q, i)
while len(q)>0:
    price, nowTown = heapq.heappop(q)
    if used[nowTown] == 0:
        used[nowTown] = 1
        ans += price
        for p,j in edge[nowTown]:
            if used[j] == 0:
                heapq.heappush(q, (p, j))
print(ans)
