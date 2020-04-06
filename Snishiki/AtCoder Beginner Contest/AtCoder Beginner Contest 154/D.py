from collections import deque
N,K = map(int, input().split())
p = list(map(int, input().split()))
que = deque([0]* K)
Max = deque([0]* K)
E = 0.0

for i in range(N):
    que.popleft()
    que.append(p[i])
    if sum(Max) < sum(que):
        Max = que
for num in Max:
    E += (num+1)* num //2/num
print(E)
