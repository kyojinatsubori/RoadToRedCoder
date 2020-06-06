# 1個だけWA解消できず
from collections import Counter
from math import factorial
N,M = map(int,input().split())

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

# 重複組み合わせ
# フェルマーの小定理nHk≡(n+k−1)!⋅(k!)M−2⋅((n−1)!)M−2(modM)
def comb(n,k,p):
    """power_funcを用いて(nCk) mod p を求める"""
    if n<=0 or k<0 or n<k: return 0
    if n==1 or k==0: return 1
    a=factorial(n+k-1) %p
    b=factorial(k) %p
    c=factorial(n-1) %p
    return (a*pow(b,p-2,p)*pow(c,p-2,p))%p

a = prime_factorize(M)
c = Counter(a)
l = []
ans = 1
for i in c.values():
    # それぞれの余りがわかっている時、その積の余りを求める時は以下
    ans *= comb(N,i,10**9+7)
    ans %= 10**9+7

print(ans%(10**9+7))