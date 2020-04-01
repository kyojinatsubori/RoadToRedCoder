import math
a, b = map(int, input().split())
if ((a + 1)* 12.5 - 1 - b * 10) * (a * 12.5 - (b + 1) * 10 + 1)> 0:
    print(-1)
    exit()
print(max(math.ceil(a * 12.5), b * 10))