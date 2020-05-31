N = int(input())
A = list(map(int,input().split()))
count = [0]*60
ans = 0
for i in A:
    for j in range(60):
        if (i >> j) & 1 == 1:
            count[j] += 1

time = 1
for i in count:
    ans += i*(N-i)*time
    time = time*2
print(ans%(10**9+7))

