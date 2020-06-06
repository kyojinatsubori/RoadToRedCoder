import heapq
N = int(input())
shelf = []
for i in range(N):
    shelf.append(list(map(int,input().split())))
M = int(input())
a = list(map(int,input().split()))
# 何個とられたか表す
ind = [0]*N
q1 = []
q2 = []
for i in range(N):
    heapq.heappush(q1, (-shelf[i][1], i))
    heapq.heappush(q2, (-shelf[i][1], i))
    if shelf[i][0] >= 2:
        heapq.heappush(q2, (-shelf[i][2], i))
used = set([])
for i in a:
    if i == 1:
        flag = True
        ans = 0
        where = 0
        while flag:
            ans, where = heapq.heappop(q1)
            if ans not in used:
                flag = False
        print(-ans)
        used.add(ans)
        ind[where] +=1
        k = shelf[where][0]
        if 1+ind[where] <= k:
            heapq.heappush(q1, (-shelf[where][1+ind[where]],where))
        if 2+ind[where] <= k:
            heapq.heappush(q2, (-shelf[where][2+ind[where]],where))
    else:
        flag = True
        ans = 0
        where = 0
        while flag:
            ans, where = heapq.heappop(q2)
            if ans not in used:
                flag = False
        print(-ans)
        used.add(ans)
        ind[where] +=1
        k = shelf[where][0]
        if 1+ind[where] <= k:
            heapq.heappush(q1, (-shelf[where][1+ind[where]],where))
        if 2+ind[where] <= k:
            heapq.heappush(q2, (-shelf[where][2+ind[where]],where))
