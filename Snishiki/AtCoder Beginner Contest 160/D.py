n, x, y = map(int, input().split())
array = [0]*(n-1)

for i in range(1, n+1):
    for j in range(i+2, n+1):
        array[min(j-i, abs(x-i)+1+abs(y-j), abs(y-i)+1+abs(x-j))-1] += 1

print(n)
for k in range(1, n-1):
    print(array[k])