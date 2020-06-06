from collections import Counter
N = int(input())

# 因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

a = prime_factorize(N)
c = Counter(a)
ans = 0
for i in c.values():
    j = 1
    while i >= j:
        i -= j
        j += 1
        ans += 1
print(ans)

