from fractions import gcd
import math
a, b = map(int,input().split())
print(math.ceil(a* b / gcd(a, b)))