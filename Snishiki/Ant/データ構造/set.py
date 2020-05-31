N = int(input())
d = [0]*N
for i in range(N):
    d[i] = int(input())
ds = set(d)
print(len(ds))