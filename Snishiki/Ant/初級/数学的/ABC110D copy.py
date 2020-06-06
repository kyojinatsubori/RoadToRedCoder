from collections import Counter
import math
mod = 10**9+7
N,M = map(int,input().split())
factors = []
f = 2
while M%f==0:
    M//=2
    factors.append(f)
f = 3
while f*f<=M:
    if M%f==0:
        M//=f
        factors.append(f)
    else:
        f+=2
if M!=1:
    factors.append(M)
count = Counter(factors)

def choose(n,k):
    # 重複組み合わせ
    return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))
ans = 1
for v in count.values():
    ans *= choose(N+v-1,N-1)
    ans %= mod
print(ans)