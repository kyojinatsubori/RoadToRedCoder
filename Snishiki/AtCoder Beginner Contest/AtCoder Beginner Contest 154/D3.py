from collections import deque
import copy
N,K = map(int, input().split())
p = list([(i+1)* i/2/i for i in map(int, input().split())])
que = deque([0]* K)
sumM = 0
sumq = 0
E = 0.0

for i in range(N):
    sumq -= que.popleft()
    sumq += p[i]
    que.append(p[i])
    if E < sumq:
        E = sumq
print(E)
