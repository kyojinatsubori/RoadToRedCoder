a,b,x = map(int,input().split())
keta = 0
for i in range(1,24):
    cx = x - b*(i)
    if cx < a*(10**(i-1)):
        keta = i-1
        break
if keta == 0:
    print(0)
elif keta >= 10:
    print(10**9)
else:
    cx = x - keta*b
    # 原因
    if cx//a >= 10**9:
        if len(str(cx//a)) > keta:
            print(10**(keta)-1)
        else:
            print(10**9)
    else:
        if len(str(cx//a)) > keta:
            print(10**(keta)-1)
        else:
            print(cx//a)