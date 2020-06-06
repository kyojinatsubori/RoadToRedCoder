# bfs
import queue
N = int(input())
ans = [-1]*N
odd = [[] for _ in range(N)]
even = [[] for _ in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    if w % 2 == 0:
        even[u-1].append(v-1)
        even[v-1].append(u-1)
    else:
        odd[u-1].append(v-1)
        odd[v-1].append(u-1)

q = queue.Queue()
q.put(0)
ans[0] = 0

while (not q.empty()):
    now = q.get()
    nowa = ans[now]
    for i in odd[now]:
        if ans[i] == -1:
            if nowa == 0:
                ans[i] = 1
            else:
                ans[i] = 0
            q.put(i)
    for j in even[now]:
        if ans[j] == -1:
            ans[j] = nowa
            q.put(j)

for i in ans:
    print(i)