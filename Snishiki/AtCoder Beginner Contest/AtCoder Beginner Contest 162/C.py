import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)

K = int(input())
count  = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            count += gcd(a,b,c)

print(count)