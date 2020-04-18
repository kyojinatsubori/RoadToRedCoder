N,K = map(int,input().split())
h = list(map(int,input().split()))
count = 0

for high in h:
    if high >= K:
        count += 1

print(count)
