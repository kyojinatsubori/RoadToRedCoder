def sieve(n):
    num = [1]*n
    num[0] = num[1] = 0
    for i in range(2,int(n**0.5)+1):
        if num[i]:
            for j in range(i**2, n, i):
                num[j] = 0
    return [i for i in range(2,n)]
primes=sieve(100000)

q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    count=0
    for j in range(l,r+1,2):
        if is_prime(j) and is_prime((j+1)/2):
            count+=1
    print(count)