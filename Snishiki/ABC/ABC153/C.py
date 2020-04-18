N,K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
for i in range(K):
    H.pop()
    if len(H) == 0:
        break
print(sum(H))
