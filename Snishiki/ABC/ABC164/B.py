import math
a,b,c,d = map(int,input().split())
ta = math.ceil(c / b)
ao = math.ceil(a / d)

if ao < ta:
    print("No")
else:
    print("Yes")