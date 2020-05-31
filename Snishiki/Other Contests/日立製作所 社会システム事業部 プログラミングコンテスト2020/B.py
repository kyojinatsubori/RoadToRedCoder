A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = [0]*M
y = [0]*M
c = [0]*M
for i in range(M):
    x[i], y[i], c[i] = map(int, input().split())
price = min(a) + min(b)
for j in range(M):
    cprice = a[x[j]-1] + b[y[j]-1] - c[j]
    if cprice < price:
        price = cprice
print(price)