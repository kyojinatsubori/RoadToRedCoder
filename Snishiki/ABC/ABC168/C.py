import math
a,b,h,m = map(int,input().split())
hun = h*60+m
ad = hun*0.5
bd = m*6

if abs(ad-bd) < 180:
    dg = abs(ad-bd)
    cos = math.cos(math.radians(dg))
    cc = a**2+b**2-2*a*b*cos
    print(math.sqrt(cc))
elif abs(ad-bd) == 180:
    print(a+b)
else:
    dg = 360-abs(ad-bd)
    cos = math.cos(math.radians(dg))
    cc = a**2+b**2-2*a*b*cos
    print(math.sqrt(cc))

