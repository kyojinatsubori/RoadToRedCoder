def sieve(n):
    num = [True]*n
    num[0] = num[1] = False
    for i in range(2,int(n**0.5)+1):
        if num[i]:
            for j in range(i**2, n, i):
                num[j] = False
    return [i for i in range(2,n) if num[i]]

print(sieve(100000))