x = int(input())

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

if x == 1:
    print(2)
    exit()
i = 0
while True:
    a = prime_factorize(x + i)
    if len(a) == 1:
        print(x + i)
        exit()
    i += 1