import math
h = int(input())
w = int(input())
n = int(input())
if h < w:
    h = w
print(math.ceil(n / h))