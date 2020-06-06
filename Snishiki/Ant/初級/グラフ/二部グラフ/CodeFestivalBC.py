# 2部グラフは特別ケース。
# 2部グラフの時、各ノードは色の違うノードとしか奇数長サイクルを持たない。
# 2部グラフでない時、各ノードは必ず全ノードと奇数長サイクルを持つ。
import queue
from collections import Counter
N,M = map(int,input().split())
ans = [-1]*N
pas = [[] for _ in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    pas[u-1].append(v-1)
    pas[v-1].append(u-1)

q = queue.Queue()
q.put(0)
ans[0] = 0
flag = True
while (not q.empty()):
    now = q.get()
    nowa = ans[now]
    for i in pas[now]:
        if ans[i] == -1:
            if nowa == 0:
                ans[i] = 1
            else:
                ans[i] = 0
            q.put(i)
        else:
            if ans[i] == nowa:
                flag = False

if flag:
    c = Counter(ans)
    zer = c[0]
    one = c[1]
    print(zer*one-M)
else:
    print(N*(N-1)//2-M)
