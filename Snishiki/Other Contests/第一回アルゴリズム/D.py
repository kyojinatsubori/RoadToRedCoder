from collections import Counter
N = int(input())
A = []
son = [0]*N
for i in range(N):
    n = int(input())
    A.append(n)
    son[n-1] += 1
j = 0
flag = 0
ans = -1
for i in range(N):
    if son[i] == 0:
        ans = i
c = Counter(A)
if c.most_common()[0][1] == 2:
    print(c.most_common()[0][0], ans+1)
else:
    print("Correct")