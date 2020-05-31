from fractions import gcd
from functools import reduce
N,M = map(int,input().split())
a = list(map(int,input().split()))

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

lcm = lcm_list(a)
test = a[0]
count = 0
while test%2 ==0:
    test = test//2
    count += 1
for i in range(N):
    if (a[i]//2**count)%2 == 0:
        print(0)
        exit()
print((M+lcm//2)//lcm)