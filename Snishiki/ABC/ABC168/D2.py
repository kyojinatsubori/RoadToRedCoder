import queue
import copy
q = queue.Queue()
n,m = map(int,input().split())
route = [0]*n
for i in range(n):
    route[i] = [0]*n
for i in range(m):
    a, b = map(int,input().split())
    route[a-1][b-1] = 1
    route[b-1][a-1] = 1
sign = [0]*(n-1)
q.put(1)
while q.empty:
    now = q.get()
    for i in range(len(route[now-1])):
        if route[now-1][i] == 1:
            route[now-1][i] = 0
            route[i][now-1] = 0
            if sign[i-1] == 0:
                sign[i-1] = copy.deepcopy(now)
                q.put(i+1)
