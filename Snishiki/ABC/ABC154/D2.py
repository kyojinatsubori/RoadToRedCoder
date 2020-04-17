from collections import deque
import copy
N,K = map(int, input().split())
p = list(map(int, input().split()))
que = deque([0]* K)
Max = deque([0]* K)
sumM = 0
sumq = 0
E = 0.0

for i in range(N):
    sumq -= que.popleft()
    sumq += p[i]
    que.append(p[i])
    if sumM < sumq:
        Max = copy.deepcopy(que)
        sumM = sumq
for num in Max:
    E += (num+1)* num //2/num
print(E)
