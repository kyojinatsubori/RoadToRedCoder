# ダイクストラ法。スタートとゴールの両方からダイクストラを行う。
# また最後の回答について、両替所がたくさんある状態から減らすのではなく、
# 未来（両替所一つしかない）状態から増やしてminする考え方重要
# ちなみにリストからtupleに変えたらTLE解消した
import heapq
n,m,s,t = map(int,input().split())
edgeY = [[] for _ in range(n)]
edgeS = [[] for _ in range(n)]
for i in range(m):
    u,v,a,b = map(int,input().split())
    edgeY[u-1].append((a, v-1))
    edgeY[v-1].append((a, u-1))
    edgeS[u-1].append((b, v-1))
    edgeS[v-1].append((b, u-1))
costY = [float('inf')]*n
costS = [float('inf')]*n
costY[s-1] = 0
costS[t-1] = 0

# 円の時
q = []
for i in edgeY[s-1]:
    heapq.heappush(q, i)
while len(q):
    nowEdge = heapq.heappop(q)
    if costY[nowEdge[1]] == float('inf'):
        costY[nowEdge[1]] = nowEdge[0]
        for i in edgeY[nowEdge[1]]:
            heapq.heappush(q , (i[0]+costY[nowEdge[1]], i[1]))

# スヌークの時
q = []
for i in edgeS[t-1]:
    heapq.heappush(q, i)        
while len(q):
    nowEdge = heapq.heappop(q)
    if costS[nowEdge[1]] == float('inf'):
        costS[nowEdge[1]] = nowEdge[0]
        for i in edgeS[nowEdge[1]]:
            heapq.heappush(q , (i[0]+costS[nowEdge[1]], i[1]))
cost = []
ans = []
first = 10**15
minCost = 10**15
for i in range(n-1,-1,-1):
    nowCost = costY[i]+costS[i]
    if minCost > nowCost:
        minCost = nowCost
    ans.append(minCost)
for i in range(n-1,-1,-1):
    print(first- ans[i])


