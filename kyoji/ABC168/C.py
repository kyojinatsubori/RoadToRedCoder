import math
a,b,h,m=map(int,input().split())
#毎分5.5度ずつ差が開いていく。
ke=(h*60+m)*5.5/360
ke=(ke-int(ke))*math.pi*2
ans=math.sqrt(a**2+b**2-2*a*b*math.cos(ke))
print(ans)