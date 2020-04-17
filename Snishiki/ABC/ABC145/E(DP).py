N, T = map(int,input().split())
AB = [0] * N
sum = 0
ans = 0
for i in range(N):
    AB[i] = list(map(int,input().split()))
    AB[i].append(AB[i][1]/AB[i][0])

AB.sort(key=lambda x: x[2])

while T > sum and len(AB) != 0:
    for i in range(1, len(AB)+1):
        if AB[-i][0] < T-sum:
            sum += AB[-i][0]
            ans += AB[-i][1]
            AB.pop(-i)
            break
        if i == len(AB):
            sum += AB[-1][0]
            ans += AB[-1][1]
            AB.pop(-1)
            break
print(ans)